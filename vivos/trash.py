import os


with open("w2v2_dict.txt", 'r') as f, open("common_dict.txt", 'w')as o:
    data = f.readlines()

    for line in data:
        char, num = line.split(" ")
        char = char.upper()

        o.write(f"{char} {num}")