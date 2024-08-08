from pydub import AudioSegment
import pydub
from pydub.silence import split_on_silence
import json
import sys
import os

# 获取参数
audio_path = sys.argv[1]
min_silence_len = int(sys.argv[2])
silence_thresh = int(sys.argv[3])
# 创建记过保存目录
folder = os.path.split(audio_path)[0] + "4_voice"
if not os.path.exists(folder):
    os.mkdir(folder)
audio_type = os.path.splitext(audio_path)[-1][1:]
# 切分文件
audio_segment = AudioSegment.from_file(audio_path, format=audio_type)
not_silence_ranges = pydub.silence.detect_nonsilent(audio_segment, min_silence_len=min_silence_len,
                                                    silence_thresh=silence_thresh, seek_step=1)
last_end_position = 0  # 上个非静默音频段结束位置，初始为0
json_dict = {}
for index in range(len(not_silence_ranges)):
    json_dict2 = {}
    current_end_position = round((not_silence_ranges[index][1]))  # 获取当前非静默音频段结束位置
    if index == len(not_silence_ranges)-1:
        new = audio_segment[last_end_position:]
    else:
        new = audio_segment[last_end_position:current_end_position]
    file_name = '%04d.%s' % (index, audio_type)
    save_name = folder+'/'+file_name
    new.export(save_name, format=audio_type)

    last_end_position = current_end_position
    # 获取非静默音频段在当前音频段的开始位置和结束位置，又调用了一次detect_nonsilent方法有点麻烦，暂时没想到更好的方法
    new_no_silence = pydub.silence.detect_nonsilent(new, min_silence_len=min_silence_len, silence_thresh=silence_thresh,
                                                    seek_step=1)
    new_start_position = new_no_silence[0][0]
    new_end_position = new_no_silence[0][1]
    json_dict2["StartPosition"] = new_start_position
    json_dict2["EndPosition"] = new_end_position
    json_dict2["Duration"] = int(new.duration_seconds*1000)
    json_dict[file_name] = json_dict2
res = json.dumps(json_dict, indent=4, ensure_ascii=False)
f_res = open(folder+r"\res.json", "w", encoding='utf8')
f_res.write(res)
