# 테스트 input 
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

# 키패드 딕셔너리 형으로 선언
pad = {0:(1,0),1:(0,3),2:(1,3),3:(2,3),4:(0,2),5:(1,2),6:(2,2),7:(0,1),8:(1,1),9:(2,1)}

left , right = (0,0) , (2,0)

result = ''

for i in numbers:
    # 1,4,7 일때는 왼손
    if i in [1,4,7]:
        result += "L"
        left = pad[i]
        print(i,'#######', left)
    # 3,6,9 일때는 오른손
    elif i in [3,6,9]:
        result += "R"
        right = pad[i]
    # 2,5,8,0 일때
    else:
        # 왼손과 오른손의 거리 계산
        left_dis = abs(left[0] - pad[i][0]) + abs(left[1] - pad[i][1])
        right_dis = abs(right[0] - pad[i][0]) + abs(right[1] - pad[i][1])

        # 왼손과 더 가까울 경우
        if left_dis < right_dis:
            result += "L"
            left = pad[i]
        
        # 오른손과 더 가까울 경우
        elif left_dis > right_dis:
            result += "R"
            right = pad[i]
        # 거리가 똑같을 경우
        else:
            # input hand 값에 따라 구분 
            if hand == "right":
                result += "R"
                right = pad[i]

            else:
                result += "L"
                left = pad[i]
print(result)