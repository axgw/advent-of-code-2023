# 1st draft
# l = []
# n = []
# total = 0
# for i in range(len(doc)):
#     l = []
#     for j in range(len(doc[i])):
#         if doc[i][j].strip().isdigit():
#             l.append(int(doc[i][j]))
#     if len(l) == 1:
#         n.append(l[0] * 10 + l[0])
#     else:
#         n.append(l[0] * 10 + l[-1])
# for k in range(len(n)):
#     total += n[k]

# cleaned up
def trebuchet(input_file):
    final = []
    with open(input_file, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            num = [int(char) for char in line if char.rstrip().isdigit()]
            final.append(num[0] * 10 + num[0]) if len(num) == 1 else final.append(num[0] * 10 + num[-1])
        total = sum(final[k] for k in range(len(final)))
    return total
