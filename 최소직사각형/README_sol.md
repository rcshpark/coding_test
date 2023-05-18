# 최소직사각형

<br>


- 코드 작성 전, 나눌 수 있는 조건 부터 생각했다. 
1. input받은 2차원 배열을 오름차순으로 우선 정리
2. 정리된 배열을 다시한번 인덱스 0,1 기준으로 다시 내림차순으로 정리하면 최소 사이즈 명함 크기 구할 수 있음

<br>


- 전체 배열을 오름차순으로 정리

```
for i in input:
    sorted_data = [min(i),max(i)]
    sorted_arr.append(sorted_data)
```

<br>

- 정리된 배열을 다시 2차원 배열 내의 배열 인덱스 0 과 1 기준으로 내림차순 정렬 후, 각 0번 인덱스를 사용하면 최댓값 사용 가능
- 최댓값을 각 가로 세로 변수에 저장하고 곱하여 리턴

```
sorted_arr.sort(key=lambda x:x[0], reverse= True)
h = sorted_arr[0][0]

sorted_arr.sort(key=lambda x:x[1],reverse= True)
w = sorted_arr[0][1]

result = h * w
print(result)
```