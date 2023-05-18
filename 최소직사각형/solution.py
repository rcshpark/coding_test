# 1. 전체 배열을 오름차순으로 정리 
# 2. 첫번째 인덱스 최댓값과 두번째 인덱스 최댓값 곱해서 리턴 

input = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	
sorted_arr = []

for i in input:
    sorted_data = [min(i),max(i)]
    sorted_arr.append(sorted_data)
    
sorted_arr.sort(key=lambda x:x[0], reverse= True)
h = sorted_arr[0][0]

sorted_arr.sort(key=lambda x:x[1],reverse= True)
w = sorted_arr[0][1]

result = h * w
print(result)