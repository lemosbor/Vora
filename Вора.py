import speech_recognition as sr
import pyttsx3
import webbrowser
from pydub import AudioSegment
from pydub.playback import play # подключаем библиотеку для воспроизведения mp3

text = 'какой-нибудь текст'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate-57)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)



def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
        if text == "привет":
            tts.say("Добрый вечер, Илья Васильевич")
            tts.runAndWait()
        if text == "как дела":
            tts.say("Всё замечательно.")
            tts.runAndWait()
        if text == "терпсихора":
            tts.say("Слушаю и повинуюсь")
            tts.runAndWait()
        if text == "кто такой":
            tts.say("Ми")
            tts.runAndWait()
        if text == "она хорошая":
            tts.say("проанализированные мною данные позволяют с уверенностью сказать, что Инесса хорошая на 134 процента")
            tts.runAndWait()
        if text == "обновить музыку":
            tts.say("Начинаю обновление музыки")
            tts.runAndWait()
            import Парсер
        if text == "как зовут мою девушку":
            tts.say("Я хотела бы быть вашей девушкой, но это пока невозможно. Вашу девушку зовут Инесса.")
            tts.runAndWait()        
        if text == "включи новую песню":
            tts.say("Включаю. Но скоро я сама научусь петь")
            tts.runAndWait()
            song = AudioSegment.from_mp3("01.mp3")
            play(song)
        if text == "покажи погоду":
            tts.say("С вами всегда тепло и солнечно, создатель. Загружаю погоду.")
            tts.runAndWait()
            webbrowser.open("https://yandex.ru/pogoda/moscow/maps/nowcast?via=mmapw")
        if text == "баста":
            global и
            и = 1
    except:
        print('Error')
и = 0
while и == 0:
    record_volume()