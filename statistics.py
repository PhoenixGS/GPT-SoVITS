import librosa
import os
from tqdm import tqdm

total_duration = 0.0

lis = os.listdir("data/陆光")
for li in tqdm(lis):
    if li.endswith(".wav"):
        y, sr = librosa.load("data/陆光/"+li)
        duration = librosa.get_duration(y=y, sr=sr)
        total_duration += duration

print(total_duration)