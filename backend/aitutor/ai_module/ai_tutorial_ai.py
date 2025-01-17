import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
dificult = "Легко"
language = "cpp"
topic = "functions" 
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

promt = f"Можешь придумать задачу на языке {language} на {dificult} сложности, по теме {topic}." \
 "Раздели ответ на 3 модуля : 1 модуль: Пример другой задачи с её кодом вводом и выводом," \
 "2 модуль: текст задачи ,Опционально ввод, Ожидаемый вывод, 3 модуль: Пример ввода и вывода без её кода\n"
tutor = f"tutorial_{language}.md"
with open(tutor, 'rb') as f:
  raw_data = f.read()
with open(tutor, "r", encoding="utf-8") as f:
    tutorial_text = f.read()

promt = promt + tutorial_text

response = model.generate_content(promt) 

promtspliter:str = response.text
promtspliter = promtspliter.split("## Модуль 1: Пример другой задачи с кодом, вводом и выводом")
promtsplited1 = promtspliter[1].split("## Модуль 2: Текст задачи")
promtsplited2 = promtsplited1[1].split("## Модуль 3: Пример ввода и вывода без кода")

class Practical_task:
    def __init__(self, modul:str):
        self._module = modul

        self._metadata = {}
    def set_text(self, modul:str):  
        self._module = modul
    def get_text(self):
        return self._module
promt1 = Practical_task(promtsplited1[0])#1модуль
print(promt1.get_text())
promt2 = Practical_task(promtsplited2[0])#2модуль
print(promt2.get_text())
promt3 = Practical_task(promtsplited2[1])#3модуль
print(promt3.get_text())
#для вывода в консоль
