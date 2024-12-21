import json
import os
import subprocess

from vosk import KaldiRecognizer, Model



async def wav_to_text(path: str):
    model = Model(lang="ru")
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