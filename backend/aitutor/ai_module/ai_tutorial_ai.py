import google.generativeai as genai
import os
import re
from typing import Optional, Dict, List, Any
import time

from enum import Enum

class Difficulty(Enum):
    EASY = "легкая"
    MEDIUM = "средняя"
    HARD = "сложная"


class AITutorialGenerator:
    def __init__(self, difficulty: Difficulty = Difficulty.EASY, max_attempts: int = 10, api_request_delay: int = 10):
        self.difficulty = difficulty
        self.max_attempts = max_attempts
        self.model = None
        self.tutorial_text = ""
        
        # Store parsed content
        self.example_task_description = ""
        self.example_task_code = ""
        self.example_task_input = ""
        self.example_task_output = ""
        
        self.practical_task_description = ""
        self.practical_task_input = ""
        self.practical_task_output = ""
        
        self.input_output_validation_content = ""
        self.input_output_validation_input = ""
        self.input_output_validation_output = ""
        
        self.api_request_delay = api_request_delay
        
        self._setup_gemini()
        self._load_tutorial()


    def _setup_gemini(self) -> None:
        """Initialize the Gemini API and model."""
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")


    def _load_tutorial(self) -> None:
        """Load tutorial content from the corresponding markdown file."""
        tutorial_file = f"tutorial_cpp.md"
        try:
            with open(tutorial_file, "r", encoding="utf-8") as f:
                self.tutorial_text = f.read()
        except Exception as e:
            print(f"Error loading tutorial file: {e}")
            self.tutorial_text = ""


    def _create_prompt(self) -> str:
        """Generate the prompt for the AI model."""
        return (
            f"Можешь придумать практическую задачу ориентируясь на текст туториала по языку программирования, сложность - {self.difficulty},"
            f"тема {self.topic}. Язык узнаешь по тексту туториала. \n" +
            "При ответе, не используй символы разметки markdown, отвечай просто текстом. \n" +
            "Будь внимателен с подструктурой [Ввод] и [Вывод], Пользователь не будет знать правильный Вывод, поэтому старайся сделать их просто значениями, которые будет легко проверить, без сложных форматов Вывода. \n" +
            "Будь внимателен с подструктурой [Ввод] и [Вывод], если Ввод или Вывод содержат несколько значений, указывай их в одной строке, разделяя каждое значение пробелом. \n" +
            "При ответе, внимательно следуй этой структуре, не нарушая ее.  \n" +
            "Раздели ответ на 3 модуля: \n" +
            "[1 Модуль]: Пример другой задачи с её кодом вводом и выводом. Подструктура: [Текст задачи 1]:, [Код 1]:, [Ввод 1]:, [Вывод 1]:;\n" +
            "[2 Модуль]: Текст задачи, требованния к вводу и  к выводу. Подструктура: [Текст задачи 2]:, [Ввод 2]:, [Вывод 2]:\n" +
            "[3 Модуль]: Ввод и вывод задачи из 2 модуля(Важно! вывод будет использоваться для проверки правильности выполненной задачи.). Подструктура: [Ввод 3]:, [Вывод 3]:\n" +
            "Текст туториала: \n" +
            self.tutorial_text
        )


    def generate_tutorial(self, topic: str = "НЕ УКАЗАНО", tutorial_text: str = "") -> Dict[str, 'PracticalTask']:
        """Generate a complete tutorial with all modules."""
        attempt = 0
        valid_content = False
        result = None
        self.topic = topic
        
        if tutorial_text:
            self.tutorial_text = tutorial_text

        while attempt < self.max_attempts and not valid_content:
            attempt += 1
            prompt = self._create_prompt()
            
            # Add a delay before making the API request
            if attempt > 1:
                time.sleep(self.api_request_delay)
            
            response = self.model.generate_content(prompt)
            tutorial = self._parse_response(response.text)
            
            # Store parsed content in instance variables
            if tutorial and "example_task" in tutorial:
                example_parts = self.parse_module1_content(tutorial["example_task"].get_content())
                self.example_task_description = self._clean_text(example_parts["task"]).replace("**Текст задачи:**", "").strip()
                self.example_task_code = example_parts["code"]
                self.example_task_input = example_parts["input"]
                self.example_task_output = example_parts["output"]
            
            if tutorial and "practical_task" in tutorial:
                practical_parts = self.parse_module2_content(tutorial["practical_task"].get_content())
                self.practical_task_description = practical_parts["task"]
                self.practical_task_input = practical_parts["input"]
                self.practical_task_output = practical_parts["output"]
            
            if tutorial and "input_output_validation" in tutorial:
                self.input_output_validation_content = tutorial["input_output_validation"].get_content()
                numbers = self.get_input_output_numbers(self.input_output_validation_content)
                self.input_output_validation_input = numbers["input"]
                self.input_output_validation_output = numbers["output"]
            
            # Validate content
            if self._validate_content():
                valid_content = True
                result = tutorial

        return result if valid_content else None


    def _parse_response(self, response_text: str) -> Dict[str, 'PracticalTask']:
        """Parse the AI response into separate modules."""
        print(response_text)
        print("------------------------------------------------------")
        return {}
        try:
            # Split into modules
            _, rest = response_text.split("## Модуль 1: Пример другой задачи с кодом, вводом и выводом", 1)
            example_content, rest = rest.split("## Модуль 2: Текст задачи", 1)
            practical_content, validation_content = rest.split("## Модуль 3: Пример ввода и вывода без кода", 1)
            return {
                "example_task": PracticalTask(example_content.strip()),
                "practical_task": PracticalTask(practical_content.strip()),
                "input_output_validation": PracticalTask(validation_content.strip())
            }
        except ValueError as e:
            print(f"Error parsing response: {e}")
            return {}


    @staticmethod
    def extract_digits(text: str) -> List[str]:
        """Extract single digits from text."""
        return re.findall(r'\d', text)


    @staticmethod
    def extract_numbers(text: str) -> List[str]:
        """Extract complete numbers from text."""
        return re.findall(r'\d+', text)


    @staticmethod
    def extract_numbers_from_section(text: str, section_marker: str) -> List[str]:
        """Extract numbers (including decimals) from a specific section (input or output)."""
        try:
            # Find the section
            parts = text.split(section_marker)
            if len(parts) < 2:
                return []
            
            # For input, take until next section or end
            section_text = parts[1].split("**")[0] if "**" in parts[1] else parts[1]
            
            # Extract both integer and decimal numbers
            return re.findall(r'-?\d*\.?\d+', section_text)
        except Exception:
            return []


    def get_input_output_numbers(self, module3_content: str) -> Dict[str, str]:
        """Get separated input and output numbers from module 3 as strings."""
        clean_content = self._clean_text(module3_content)
        return {
            "input": " ".join(self.extract_numbers_from_section(clean_content, "[ Ввод 3]:")),
            "output": " ".join(self.extract_numbers_from_section(clean_content, "[ Вывод 3]:"))
        }


    def _clean_text(self, text: str) -> str:
        """Remove extra whitespace and unnecessary markers."""
        if not text:
            return ""
        # Remove extra whitespace
        text = " ".join(text.split())
        # Remove markdown markers if they exist
        text = text.replace("```", "")\
                  .replace("**Код:**", "")\
                  .replace("**Задача:**", "")\
                  .replace("**Ожидаемый вывод:**", "")\
                  .replace("**Ожидаемый ввод:**", "")\
                  .replace("**Опциональный ввод:**", "")\
                  .replace(", опционально ввод, ожидаемый вывод", "")\
                  .replace(", **Текст задачи:**", "")\
                  .replace(", ввод", "")\
                  .replace(", вывод", "")\
                  .strip()
        return text


    def _clean_code(self, code: str) -> str:
        """Clean code while preserving formatting."""
        if not code:
            return ""
        # Remove language markers if they exist
        code = code.replace("cpp", "").replace("python", "").strip()
        return code


    def parse_module1_content(self, content: str) -> Dict[str, str]:
        """Parse module 1 content into text, code, input, and output."""
        try:
            # Split content by code block markers
            parts = content.split("```")
            
            # Get task text (everything before first code block)
            task_text = self._clean_text(parts[0])
            
            # Get code (first code block)
            code = self._clean_code(parts[1].strip()) if len(parts) > 1 else ""
            
            # Get input and output
            input_output = "".join(parts[2:]) if len(parts) > 2 else ""
            input_text = ""
            output_text = ""
            
            if len(input_output.split("**Ввод:**")) > 1:
                output_parts = input_output.split("**Ввод:**")[1].split("**Вывод:**")
                input_text = self._clean_text(output_parts[0])
                if len(output_parts) > 1:
                    output_text = self._clean_text(output_parts[1])
            
            return {
                "task": task_text,
                "code": code,
                "input": input_text,
                "output": output_text
            }
        except Exception as e:
            print(f"Error parsing module 1: {e}")
            return {
                "task": self._clean_text(content),
                "code": "",
                "input": "",
                "output": ""
            }


    def parse_module2_content(self, content: str) -> Dict[str, str]:
        """Parse module 2 content into task text, input, and output."""
        try:
            # Split by text references
            parts = content.split("[Ссылка на текст]")
            if len(parts) < 2:
                parts = content.split("[Текст]")
            
            task_text = parts[0] if parts else content
            input_text = ""
            output_text = ""
            
            # If we found text reference, try to find input/output in the remaining text
            if len(parts) > 1:
                remaining_text = parts[1]
                # Try to split by input markers
                for marker in ["**Ожидаемый ввод:**", "**Ввод:**", "**Опциональный ввод:**",
                             "Ожидаемый ввод:", "Ввод:", "Опциональный ввод:","**Текст задачи:**"]:
                    if marker in remaining_text:
                        io_parts = remaining_text.split(marker)
                        if len(io_parts) > 1:
                            rest = io_parts[1]
                            # Try to split by output markers
                            for out_marker in ["**Ожидаемый вывод:**", "**Вывод:**",
                                             "Ожидаемый вывод:", "Вывод:", "**Текст задачи:**"]:
                                if out_marker in rest:
                                    final_parts = rest.split(out_marker)
                                    input_text = final_parts[0]
                                    if len(final_parts) > 1:
                                        output_text = final_parts[1]
                                    break
                            if input_text:  # If we found input, stop looking for more markers
                                break
            
            return {
                "task": task_text.strip(),
                "input": input_text.strip(),
                "output": output_text.strip()
            }
            
        except Exception as e:
            print(f"Error parsing module 2: {e}")
            return {
                "task": content,
                "input": "",
                "output": ""
            }


    def _validate_content(self) -> bool:
        """Validate that all necessary content is present and in correct format."""
        # Check example task
        if not all([self.example_task_description, self.example_task_code, 
                   self.example_task_input, self.example_task_output]):
            return False
            
        # Check practical task
        if not self.practical_task_description:
            return False
            
        # Check that input/output contain only numbers when present
        if not self._contains_only_numbers(self.practical_task_input) or \
           not self._contains_only_numbers(self.practical_task_output):
            self.practical_task_input = ""
            self.practical_task_output = ""
            return False
            
        # Check input/output validation
        if not all([self.input_output_validation_content, 
                   self.input_output_validation_input, 
                   self.input_output_validation_output]):
            return False
            
        return True


    def _contains_only_numbers(self, text: str) -> bool:
        """Check if text contains only numbers and spaces."""
        if not text:
            return True  # Empty text is considered valid
        # Remove all whitespace
        cleaned = "".join(text.split())
        # Check if there are any numbers
        numbers = re.findall(r'-?\d*\.?\d+', cleaned)
        if not numbers:
            return False
        # Join all found numbers without spaces
        numbers_text = "".join(numbers)
        # Text should contain only what we extracted as numbers
        return cleaned == numbers_text


    @staticmethod
    def parse_input_output(text: str) -> Optional[List[str]]:
        """Parse input and output sections from text."""
        try:
            input_parts = text.split("**Ввод:**")
            if len(input_parts) < 2:
                return None
            output_parts = input_parts[1].split("**Вывод:**")
            if len(output_parts) < 2:
                return None
            return output_parts[0].split("```")
        except Exception:
            return None


class PracticalTask:
    """Represents a single module of the tutorial task."""
    
    def __init__(self, content: str):
        self._content = content.strip()
        self._metadata: Dict[str, Any] = {}
    
    def get_content(self) -> str:
        """Get the task content."""
        return self._content
    
    def set_content(self, content: str) -> None:
        """Update the task content."""
        self._content = content.strip()
    
    def add_metadata(self, key: str, value: Any) -> None:
        """Add metadata to the task."""
        self._metadata[key] = value
    
    def get_metadata(self, key: str) -> Any:
        """Retrieve metadata by key."""
        return self._metadata.get(key)


def main():
    # Example usage
    generator = AITutorialGenerator(Difficulty.EASY, 10)
    
    result = generator.generate_tutorial()

if __name__ == "__main__":
    main()