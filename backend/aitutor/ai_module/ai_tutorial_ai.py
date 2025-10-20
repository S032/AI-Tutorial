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


class GeneratedPracticalTask:
    """
    A comprehensive class to represent a structured AI-generated practical task.
    with multiple sections and tasks.
    """
    class Module:
        """
        Represents a single module within the practical task with its specific components.
        """
        def __init__(self, name: str = ''):
            self.name = name
            self.code: str = ''
            self.task_text: str = ''
            self.input: str = ''
            self.output: str = ''
            self.input_requirements: str = ''
            self.output_requirements: str = ''

    def __init__(self):
        """
        Initialize the practical task with predefined sections.
        """
        self.example_task = self.Module(name='Example Task')
        self.practical_task = self.Module(name='Practical Task')
        self.practical_task_answer = self.Module(name='Practical Task Answer')

    def parse_response(self, response: str):
        """
        Parse the neural network response and populate practical task sections.
        
        Args:
            response (str): Full text response from the neural network.
        """
        # Parsing patterns for each section
        parsing_patterns = [
            (self.example_task, {
                'task_text': r'\[Текст задачи 1\]:(.*?)(?=\[Код 1\]:|$)',
                'code': r'\[Код 1\]:(.*?)(?=\[Ввод 1\]:|$)',
                'input': r'\[Ввод 1\]:(.*?)(?=\[Вывод 1\]:|$)',
                'output': r'\[Вывод 1\]:(.*?)(?=\[2 Модуль\]:|$)'
            }),
            (self.practical_task, {
                'task_text': r'\[Текст задачи 2\]:(.*?)(?=\[Ввод 2\]:|$)',
                'input_requirements': r'\[Ввод 2\]:(.*?)(?=\[Вывод 2\]:|$)',
                'output_requirements': r'\[Вывод 2\]:(.*?)(?=\[3 Модуль\]:|$)'
            }),
            (self.practical_task_answer, {
                'input': r'\[Ввод 3\]:(.*?)(?=\[Вывод 3\]:|$)',
                'output': r'\[Вывод 3\]:(.*?)$'
            })
        ]

        # Iterate through sections and parse
        for section, patterns in parsing_patterns:
            for attr, pattern in patterns.items():
                match = re.search(pattern, response, re.DOTALL)
                if match:
                    setattr(section, attr, match.group(1).strip())
                else:
                    raise ValueError(f"Failed to parse {attr} in section {section.name}")

    def to_dict(self) -> Dict[str, Dict[str, str]]:
        """
        Convert the practical task to a dictionary for easy serialization.
        
        Returns:
            Dict containing all practical task sections and their attributes.
        """
        return {
            'example_task': vars(self.example_task),
            'practical_task': vars(self.practical_task),
            'practical_task_answer': vars(self.practical_task_answer)
        }

    def __repr__(self) -> str:
        """
        Provide a string representation of the practical task.
        
        Returns:
            str: A readable summary of the practical task contents.
        """
        return f"GeneratedPracticalTask(\n" \
               f"  Example Task: {self.example_task.name}\n" \
               f"  Practical Task: {self.practical_task.name}\n" \
               f"  Practical Task Answer: {self.practical_task_answer.name}\n" \
               f")"


class AITutorialGenerator:
    def __init__(self, difficulty: Difficulty = Difficulty.MEDIUM, max_attempts: int = 10, api_request_delay: int = 10):
        self.difficulty = difficulty
        self.max_attempts = max_attempts
        self.model = None
        self.tutorial_text = ""
        
        self.api_request_delay = api_request_delay
        
        self._setup_gemini()


    def _setup_gemini(self) -> None:
        """Initialize the Gemini API and model."""
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel(model_name="gemini-pro-latest")

    def _open_promt_file(self) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))    
        with open(os.path.join(current_dir, "promt.txt"), "r") as promt_file:
            return promt_file.read()


    def _create_prompt(self) -> str:
        """Generate the prompt for the AI model."""
        return (
            self._open_promt_file() +
            "\n\n" +         
            self.tutorial_text
        )


    def generate_tutorial(self, topic: str = "НЕ УКАЗАНО", tutorial_text: str = "") -> Dict[str, Dict[str, str]] | None:
        """Generate a complete tutorial with all modules."""
        self.topic = topic
        
        if tutorial_text:
            self.tutorial_text = tutorial_text

            attempt = 0
            attempt += 1
            prompt = self._create_prompt()
            
            # Add a delay before making the APIrequest
            if attempt > 1:
                time.sleep(self.api_request_delay)
            
            response = self.model.generate_content(prompt)
            practical_task = GeneratedPracticalTask()
            practical_task.parse_response(response.text)

            print(response.text)
            print("------------------------------------")
            print(practical_task.example_task.task_text)
            print(practical_task.example_task.code)
            print(practical_task.example_task.input)
            print(practical_task.example_task.output)

            print(practical_task.practical_task.task_text)
            print(practical_task.practical_task.input_requirements)
            print(practical_task.practical_task.output_requirements)

            print(practical_task.practical_task_answer.input)
            print(practical_task.practical_task_answer.output)



            
            return practical_task.to_dict()


def main():
    # Example usage
    generator = AITutorialGenerator(Difficulty.EASY, 10)
    
    generator.generate_tutorial()

if __name__ == "__main__":
    main()
