num1 = input("숫자를 입력해주세요>")
num2 = input("다시 숫자를 입력해주세요>")

num3 = int(num1) + int(num2)
print(num3)

num = input("숫자를 두개를 입력해 주세요(예시: 2,3)>")

num1 = num.split(",")[0]
num2 = num.split(",")[1]

num3 = int(num1) + int(num2)
print(num3)

명단 = ['홍길동', '향단이', '신민경', '임근석']
print(명단[2])
명단[0] = '춘향이'
print(명단)

지출방법 = input('지출방법을 입력하세요')
# # == : 일치
# # != : 불일치
# # > < =< =>
if 지출방법 == '현금':
    print("개인")
elif 지출방법 == '카드':
    print("법인")
else:
    print("에러")

#  if, elif, else 하나의 블럭, 구분을 하려면 한줄 띄우기
# and, or

# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 0 ~ 60

성적점수 = int(input('성적점수를 입력해 주세요'))
if 90 < 성적점수 and 성적점수 <= 100:
    print('A')
elif 80 < 성적점수 and 성적점수 <=90:
    print('B')
elif 70 < 성적점수 and 성적점수 <=80:
    print('C')
elif 60 < 성적점수 and 성적점수 <= 70:
    print('D')
elif 0 <= 성적점수 and 성적점수 <= 59:
    print('F')
else:
    print("에러")

