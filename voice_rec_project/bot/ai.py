import json
import os
import subprocess

from vosk import KaldiRecognizer, Model



async def wav_to_text(path: str):
    print(os.listdir("./vosk-model-ru-0.42"))
    model = Model(model_path="./vosk-model-ru-0.42")
    rec = KaldiRecognizer(model, 16000)
    with open (path, "rb") as wf:
        wf.read(44)
        sesh = ""
        while True:
            data = wf.read(4000)
            if len(data) == 0:
                   break
            if rec.AcceptWaveform(data):
                 res = json.loads(rec.Result())
                 sesh += res["text"]

        res = json.loads(rec.FinalResult())
        sesh += res["text"]
        print("The result of recognition!!!")
        print(sesh)
        print(res)
        return sesh