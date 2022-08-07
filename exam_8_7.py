# from datetime import datetime, timedelta
#
# def 내일_날짜_요일(today):
#     today = datetime.strptime(today, '%Y-%m-%d')
#     today += timedelta(days=1)
#     days = ["월", "화", "수", "목", "금", "토", "일"]
#     return days[today.weekday()]
#
# print(내일_날짜_요일("2022-10-29"))

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


num1 = int(input('첫번째 숫자를 입력하세요(0~9까지):'))
num2 = input('특수문자를 입력하세요(+, -, *, /):')
num3 = int(input('두번째 숫자를 입력하세요(0~9까지):'))

num1CheckSum = True
num2CheckSum = True
num3CheckSum = True

if not (0 <= num1 and num1 <= 9):
    print('첫번째 숫자를 잘못 입력하셨습니다.')
    num1CheckSum = False
if not (0 <= num3 and num3 <= 9):
    print('두번째 숫자를 잘못 입력하셨습니다.')
    num3CheckSum = False
# if not (num2 = '+','-','*','/'):
if num2 != '+' and num2 != '-' and num2 != '*' and num2 != '/':
    print('특수문자를 잘못 입력하셨습니다.')
    num2CheckSum = False

if num1CheckSum == True and num2CheckSum == True and num3CheckSum == True:
    if num2 == '+':
        print(add(num1, num3))
    elif num2 == '-':
        print(sub(num1, num3))
    elif num2 == '*':
        print(mul(num1, num3))
    elif num2 == '/':
        print(div(num1, num3))
else:
    print("에러")

# 입력 되는 내용의 조건
# 숫자 : 0 ~ 9 까지만, 이말은 한자리 수만 입력 받을 것.
# 특수문자 : +, -, *, / 만 허용하고 그 외의 값이 입력 되는 경우에는 전부 에러 처리를 할 것.

# 첫번째 방법 : input 함수를 세번 사용해서 계산기를 완성
# 두번째 방법 : input 함수를 단 한번만 사용해서 계산기를 완성
