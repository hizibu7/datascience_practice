import math

data = []

#s 입력전까지 data리스트에 계속 한개씩 넣음
input_type = input()
if input_type == 'all':
    data = list(map(int, input().split()))
    print(data)
else:
    while True:
        a = input()
        if a == 's':
            break
        else:
            data.append(int(a))
            print(data)

data = sorted(data)

average = sum(data)/len(data)

if len(data)%2 == 1:
    median = data[len(data)//2]
else:
    median = (data[len(data)//2 - 1] + data[len(data)//2]) / 2

new_data = [(i-average)**2 for i in data]
var = sum(new_data)/len(new_data)
sta = math.sqrt(var)

print('평균값: ', average)
print('중앙값: ', median)
print('데이터 범위: ', max(data)-min(data))
print('분산: ', var)
print('표준편차: ', sta)
