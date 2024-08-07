import os
import playsound

def play_sound(file_path):
    playsound.playsound(file_path, block=False)

if __name__ == "__main__":
    output_path = "data"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    path_0 = "data/陆光"
    if not os.path.exists(path_0):
        os.makedirs(path_0)

    path_1 = "data/程小时"
    if not os.path.exists(path_1):
        os.makedirs(path_1)

    with open("fixed/voice.list", "r") as f:
        voice_list = f.readlines()

    idx_0 = 0
    idx_1 = 0

    lis = os.listdir("data/陆光")
    for li in lis:
        if li.endswith(".wav"):
            idx_0 += 1

    lis = os.listdir("data/程小时")
    for li in lis:
        if li.endswith(".wav"):
            idx_1 += 1

    for i, voice in enumerate(voice_list):
        voice = voice.strip()
        voice = voice.split("|")
        voice_path = voice[0]
        text = voice[3]
        if text != "":
            print(text)
            play_sound(voice_path)
            while True:
                try:
                    select = int(input("0: 陆光, 1: 程小时, 2: 跳过, 3: 退出"))
                    assert select in [0, 1, 2, 3]
                    break
                except Exception as e:
                    if isinstance(e, KeyboardInterrupt):
                        os._exit(0)
                    print("Invalid input")
            if select == 0:
                os.copy(voice_path, f"{path_0}/陆光_{idx_0}.wav")
                idx_0 += 1
                with open(f"{path_0}/陆光_{idx_0}.lab", "w") as f:
                    f.write(text)
            elif select == 1:
                os.copy(voice_path, f"{path_1}/程小时_{idx_1}.wav")
                idx_1 += 1
                with open(f"{path_1}/程小时_{idx_1}.lab", "w") as f:
                    f.write(text)
            elif select == 3:
                break
            print("Done")
        
        with open("fixed/voice.list", "w") as f:
            f.write("\n".join(voice_list[i+1:]))
