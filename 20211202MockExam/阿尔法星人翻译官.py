name = input().strip().split(" ")
flag = "+"
language = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty',
            'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', ""]
translator = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 0]
dictionary = dict(zip(language, translator))
if name[0] == "negative":
    name.pop(0)
    flag = "-"
sub_result = ["", "", "", ""]
num_tag = ['hundred', 'thousand', 'million']
check = [0, 0, 0]
if num_tag[2] in name:
    sub_result[2] = name[:name.index(num_tag[2])]
    name = name[name.index(num_tag[2]) + 1:]
    check[2] = 1
if num_tag[1] in name:
    sub_result[1] = name[:name.index(num_tag[1])]
    name = name[name.index(num_tag[1]) + 1:]
    check[1] = 1
if num_tag[0] in name:
    sub_result[0] = name[:name.index(num_tag[0])]
    name = name[name.index(num_tag[0]) + 1:]
    check[0] = 1
if name:
    sub_result[-1] = name
temp1 = 0
temp2 = 0
if num_tag[0] in sub_result[2]:
    temp1 += sum([dictionary[num] for num in sub_result[2][:sub_result[2].index(num_tag[0])]])*100
    sub_result[2] = sub_result[2][sub_result[2].index(num_tag[0]) + 1:]
if num_tag[0] in sub_result[1]:
    temp2 += sum([dictionary[num] for num in sub_result[1][:sub_result[1].index(num_tag[0])]])*100
    sub_result[1] = sub_result[1][sub_result[1].index(num_tag[0]) + 1:]

for i in range(len(sub_result)):
    sub_result[i] = sum([dictionary[num] for num in sub_result[i]])
result = temp1 * 1000000+ temp2*1000 + sub_result[0] * 100 + sub_result[1] * 1000 + sub_result[2] * 1000000 + sub_result[-1]
if flag == "-":
    result = 0 - result
print(result)
