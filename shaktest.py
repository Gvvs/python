#!/usr/bin/env python

import re
import msvcrt

ff7 = open("Family Feud2.txt", "r")
question = []
ans = [[]]
q = 0
a = 0

for line in ff7:
    if re.match("^[A-Z][a-z].*?", line):
        # print(line, end=" ")

        question.append(line)

        q = q + 1
        a = 0
        ans.append([])
    elif re.match("(^\d{1,2})\t(.*?)", line):

        m = re.search('^(\d{1,2})\t(.*)$', line)
        dict = int(m.group(1)), m.group(2)

        ans[q - 1].append(dict)

        a += 1

ff7_output = open("Family Feud2_output.txt", 'w')
for q in range(len(question)):
    print(question[q])
    for t in sorted(ans[q], reverse=True):
        print(t[0],  "\t",   t[1])
    print("Want to keep it? (y/n)")
    c = msvcrt.getch()

    c = c.decode('utf-8')
    print(c)
    if c == 'n':
        del(question[q])
        del(ans[q])
        print('Deleted')
    else:

        ff7_output.write("\n" + question[q])
        for p in sorted(ans[q], reverse=True):
            ff7_output.write(p[1] + "\t" + str(p[0]) + "\n")
