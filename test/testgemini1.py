import google.generativeai as genai
import os
import chardet  # type: ignore

genai.configure(api_key=os.environ["API_KEY"])
dificult = "Легко"
language = "cpp"
topic = "functions" 
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

promt = f"Можешь придумать задачу на языке {language} на {dificult} сложности, по теме {topic}. Раздели ответ на 3 модуля: 1 модуль: Пример другой задачи с её кодом вводом и выводом, 2 модуль: текст задачи ,Опционально ввод, Ожидаемый вывод, 3 модуль: код задачи для решения\n"
tutor = f"tutorial_{language}_{topic}.md"
with open(tutor, "r", encoding='utf-8') as f:
    tutorial_text = f.read()

promt = promt + tutorial_text

response = model.generate_content(promt) 
print(response.text)