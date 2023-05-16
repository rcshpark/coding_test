# 키패드 누르기

<br>

- 연산자 우선순위 경우의 수 정의

```
perations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),
              ('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
```

- 코드 작성 전, 나눌 수 있는 조건 부터 생각했다. 
1. 정의 된 배열의 인덱스 0값은 우선순위 1 , 1값은 우선순위 2 인 점을 이용
2. 연산자로 split 후 join함수를 이용하여 새로운 리스트 생성 후 eval() 로 string 연산

<br>

- 연산자 배열에서 for문을 돌려서 각 우선순위 1,2 를 a,b에 저장

```
for i in operations:
    a = i[0]
    b = i[1]


```


<br>

- 우선순위1 인 a 로 split하고 이중 for문을 사용하여 2번째 우선순위 b를 기준으로 나뉜 split을 배열에 저장
- 우선순위 2인 연산자를 join하여 빈 리스트에 저장

```
for i in input.split(a): 
        arr = [f'({k})' for k in i.split(b)]
        list.append(f'({b.join(arr)})')
```

<br>


- 우선순위 1인 연산자를 join하여 리스트에 담고 eval()을 이용하여 연산
- 연산 값을 answer 배열에 저장

```
answer.append(abs(eval(a.join(list))))
```

<br>


- max()를 이용하여 최댓값 출력 

```
print(max(answer))
```