import google.generativeai as genai
import os
import chardet  # type: ignore

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
dificult = "Легко"
language = "C++"
topic = "функции" 
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

promt = f"Можешь придумать задачу на языке {language} на {dificult} сложности, по теме {topic}. Раздели ответ на сектора: Пример другой задачи с её кодом вводом и выводом, текст задачи ,Опционально ввод, Ожидаемый вывод\n"

with open("tutorial_cpp.md", "r", encoding='utf-8') as f:
    tutorial_text = f.read()

promt = promt + tutorial_text

response = model.generate_content(promt) 
print(response.text)
