import os
import glob
import soundfile as sf
import time

data_wavs = glob.glob("/home/sangdt/research/voice/hubert/vivos/train/waves/*/*.wav")

# with open("valid.tsv", 'w') as full:
#     full.write("/home/sangdt/research/voice/hubert/vivos\n")
#     for wav_path in data_wavs:
#         sub_path = wav_path.split("vivos/")[-1]
#         y, fs = sf.read(wav_path)
#         full.write(sub_path + "\t" + str(len(y)) + "\n")


with open("valid.ltr", 'w') as full:
    with open("/home/sangdt/research/voice/hubert/vivos/train/prompts.txt") as tr:
        text = tr.readlines()

    # full.write("/home/sangdt/research/voice/hubert/vivos\n")
    for wav_path in data_wavs:
        sub_path = wav_path.split("vivos/")[-1]
        print(wav_path)
        time.sleep(1)
        
        # full.write(wav_path + "\t" + str(len(y)) + "\n")