import os
import glob
import soundfile as sf

data_wavs = glob.glob("/home/sangdt/research/voice/hubert/vivos/test/waves/*/*.wav")

with open("valid.tsv", 'w') as full:
    full.write("/home/sangdt/research/voice/hubert/vivos\n")
    for wav_path in data_wavs:
        sub_path = wav_path.split("vivos/")[-1]
        y, fs = sf.read(wav_path)
        full.write(sub_path + "\t" + str(len(y)) + "\n")
