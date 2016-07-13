dic = []
n = map(int, input().split(" "))
for i in range(n[0]):
    dic.append(list(input().split())) 
string = input()
temp = ''
out = ''
l = 0
s = ''
for i in range(n[1]):
    if n[1] > l:
        for j in range(n[0]):
            if string.startswith(dic[j][1], l):
                temp = dic[j][0]
                s = dic[j][1]
        l += len(s)
        out += temp[0]
    else:
        break
print (out) 
