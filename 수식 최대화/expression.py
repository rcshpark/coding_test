input = "100-200*300-500+20"

# 연산자 정의 
operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),
              ('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]

# 리턴 값 배열 생성
answer = []

for i in operations:
    # 우선순위 1
    a = i[0]

    # 우선순위 2 
    b = i[1]

    # 빈 리스트 생성
    list = []

    # 우선순위1 연산자로 split
    for i in input.split(a):

        # 컴프리헨션으로 우선순위2 로 분리 후 리스트에 저장 
        arr = [f'({k})' for k in i.split(b)]
        #
        list.append(f'({b.join(arr)})')
    print(arr)    
    
    print(list)
    print('==============================')        

    answer.append(abs(eval(a.join(list))))

print(max(answer))