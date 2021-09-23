animal_num, sentence_num = [int(item) for item in input().split(' ')]
data = []
count = 0
kind1 = set()
kind2 = set()
kind3 = set()
for i in range(sentence_num):
    kind, a1, a2 = [int(item) for item in input().split(' ')]
    if a1 > animal_num or a2 > animal_num:
        count += 1
        continue
