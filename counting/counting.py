from collections import defaultdict
import re

document = []
pattern = '[^\w\s]'
repl = ''

word_counts = defaultdict(int)
file = open('word_count.txt', 'r', encoding = 'utf-8')
for line in file:
    line = re.sub(pattern=pattern, repl=repl, string=line)
    for Word in line.split(' '):
        document.append(Word)
for word in document:
    word_counts[word] += 1

for key, value in word_counts.items():
    print(key, value, '\n')
