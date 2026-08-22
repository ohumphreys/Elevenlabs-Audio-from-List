import csv
import os

word_set = set()

with open('input/real_two_syllable.csv', newline='') as f:
    for row in csv.reader(f):
        word = row[0].lower()
        if word in word_set:
            print(f"Duplicate detected: {word}")
        word_set.add(word)
        
print(len(word_set))

folder = 'output/WNM/real/two syllable'
existing = {name.lower() for name in os.listdir(folder) if name.lower().endswith('.mp3')}

for word in word_set:
    expected = f"{word.lower()}.mp3"
    if expected not in existing:
        print(f"found no matching for {word}")

