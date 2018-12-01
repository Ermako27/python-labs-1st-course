f = open('f1.txt','a')
f.write('\n')
f.close

f = open('f2.txt','w')
f.close()

with open("f1.txt") as f:
    for line in f:
        f2 = open('f2.txt')
        if line not in f2:
            f2.close()
            f2 = open('f2.txt','a')
            f2.write(line + '\n')
            f2.close()


f2 = open('f2.txt')
fr = f2.read()
print(fr)
f2.close()
