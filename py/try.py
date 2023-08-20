from vosk import Model, KaldiRecognizer
import speech_recognition as sr

model = Model(r"C:\Users\Joel\Documents\Codigo\Restaurant-Call-Helper\py\vosk-model-small-es-0.42")
r = sr.Recognizer()
with sr.Microphone() as mic:

    stream = r.listen(mic)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(f"' {text[14:-3]} '")