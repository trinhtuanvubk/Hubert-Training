import os
import re
chars_to_ignore = r'[,?.!\-;:"“%\'�]'
# number_dict = {'0':'không', '1':'một', '2':'hai', '3':'ba', '4':'bốn', '5':'năm', '6':'sáu', '7':'bảy', '8':'tám', '9':'chín', '10':'mười'}
common_dict = []
with open("common_dict.txt", 'r') as d:
    dict_ = d.readlines()
    for line in dict_:
        char, num = line.split(" ")
        common_dict.append(char)
    common_dict.append(" ")

def contains_char_not_in_dict(text, char_dict):
    for char in text:
        if char not in char_dict:
            print(char)
            return True
    return False

with open("/home/sangdt/research/voice/hubert/vivos/train/prompts.txt", "r") as tsv:
    data = tsv.readlines()

with open("ltr_dir/train.ltr", 'w') as ltr:
    for line in data:
        # print(line)
        path, text = line.split(" ", 1)
        path = path.strip()
        text = text.strip()
        text = re.sub(chars_to_ignore, '', text)

        # only hot fix for vivos
        text = text.replace("4", "BỐN")

        text = text.upper()
        if contains_char_not_in_dict(text.strip(), common_dict):
            print(text)
        
        print(" ".join(list(text.replace(" ", "|"))) + " |", file=ltr)


