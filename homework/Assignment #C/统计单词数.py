word = input().strip().lower()
sentence = input().rstrip().lower()
blank_count = 0
new_start = -1
for i in range(len(sentence)):
    if sentence[i] != " ":
        new_start = i
        break
if new_start == -1:
    print(-1)
    quit()
sentence = sentence[new_start:].split(" ")
while " " in sentence:
    sentence.remove(" ")
result = [0, new_start]
for item in sentence:
    if item == word:
        result[0] += 1
if result[0] != 0:
    word_index = sentence.index(word)
    for i in range(word_index):
        result[1] += len(sentence[i]) + 1
    print(" ".join([str(i) for i in result]))
else:
    print(-1)