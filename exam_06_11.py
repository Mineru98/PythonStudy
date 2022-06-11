# 조건문 : 일정한 조건에 해당되어야지만 동작하는 것
# 반복문 : 동작을 반복적으로 하게 만드는 것
# while, for

# while : ~ 할때

count = 0

# while(True): # 무한 반복
while(count < 100): # count가 100보다 작을 때 동안만 반복
    print("카운트 : " + str(count))
    count = count + 1 # count += 1

while(True):
    if count >= 100:
        break
    print("카운트 : " + str(count))
    count = count + 1

대기표 = [1, 4, 5, 6, 9, 10]
for 대기손님 in 대기표:
    print(str(대기손님) + "번 손님 1번 창구로 와주세요")

for i in range(2, 9 + 1):
    print(i)

# [] 배열
# () while조건, 튜플, 함수 등등
# i: 전형적인 for문에서 쓰는 변수명
# for 변수명(원소) in 배열(or 튜플, 문자열이 들어갈 수 있음):
범위 = [1, 3, 5, 7, 9]
for i in 범위:
    print(i)
for i in range(1, 9 + 1, 2):
    print(i)
for i in range(1, 9 + 1):
    if i % 2 == 1:
        print(i)

# 중첩 for문 : 하위 반복문이 끝나야 상위반복문이 진행이 된다 그리고 하위반복문은 상위반복문이 시작되게 되면 다시 처음부터 시작
for i in range(1, 3 + 1):
    for j in range(1, 3 + 1):
        for k in range(1, 3 + 1):
            print(i, j, k)

# 구구단을 외자! (2단부터 9단까지) 출력
for i in range(2, 9 + 1):
    for j in range(1, 9 + 1):
        print(f"{i} x {j} = {i*j}")
