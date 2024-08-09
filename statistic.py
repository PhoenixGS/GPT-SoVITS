import librosa
import os
from tqdm import tqdm


for name in ["陆光", "程小时", "乔玲"]:
    total_duration = 0.0
    path = "data/" + name + "/"

    lis = os.listdir(path)
    for li in tqdm(lis):
        if li.endswith(".wav"):
            y, sr = librosa.load(path + li)
            duration = librosa.get_duration(y=y, sr=sr)
            total_duration += duration

    print(f"{name} total duration: {total_duration}")
    # print(total_duration)