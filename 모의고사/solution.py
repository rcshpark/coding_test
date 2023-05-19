# 1 2 3 4 5 ....
# 2 1 2 3 2 4 2 5 ....
# 33 11 22 44 55 .... 

# 배열 반봅
answer = [1,3,2,4,2]	

a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

a_result = 0
b_result = 0
c_result = 0

result = []

for i in range(len(answer)):
    if answer[i] == a[i%5]:
        a_result += 1
    if answer[i] == b[i%8]:
        b_result += 1
    if answer[i] == c[i%10]:
        c_result += 1

max = max(a_result,b_result,c_result) 

if max == a_result:
    result.append(1)
if max == b_result:
    result.append(2)
if max == c_result:
    result.append(3)

print(result)