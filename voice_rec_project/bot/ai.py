import json
import os
import wave
import math
import json
import numpy as np
from vosk import KaldiRecognizer, Model, SpkModel

def cosine_dist(x, y):
    nx = np.array(x)
    ny = np.array(y)
    return 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)

def find_speaker(vector):
    minimum_sim = math.inf
    speaker_name = ''
    with open('speakers.json', 'r') as file:
        data = json.load(file)
    for i in data:
        if abs(cosine_dist(vector, i['Vector'])) < minimum_sim:
            speaker = i["Name"]
            minimum_sim = cosine_dist(vector, i['Vector'])
    return speaker, minimum_sim

async def wav_to_text(path: str):
    print(os.listdir("./vosk-model-ru-0.42"))
    spk_model = SpkModel(model_path="./vosk-model-spk-0.4")
    model = Model(model_path="./vosk-model-ru-0.42")
    rec = KaldiRecognizer(model, 16000)
    rec.SetSpkModel(spk_model)
    preds = []
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
                 print(res)
                 if "spk" in res:
                     speaker_name, cosd = find_speaker(res["spk"])
                     preds.append(speaker_name)

        res = json.loads(rec.FinalResult())
        if "spk" in res:
            speaker_name, cosd = find_speaker(res["spk"])
            preds.append(speaker_name)
        sesh += res["text"]
        print(preds)
        result = np.unique(preds, return_counts = True)
        print(result)
        name = result[0][np.argmax(result[1])]
        print("The result of recognition!!!")
        print(sesh)
        print(name)
        return name, sesh