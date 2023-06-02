#2023_05_26

#1 (계산기 프로그램)

#조건문
# if 조건 :
# elif 조건 :
# else :
'''
a=float(input("a를 입력하세요:"))     #input () 은 문자열을 입력받는다.
b=float(input("b를 입력하세요:"))
op=input("연산자를 입력하세요:")
if op=='+':
    c=a+b
    print(f'a+b={c}')
elif op=='-':
    c=a-b
    print(f'a-b={c}')
elif op=='*':
    c=a*b
    print(f'a*b={c}')
elif op=='/':
    c=a/b
    print(f'a/b={c}')
elif op=='//':
    c=a//b
    print(f'a//b={c}')
else:
    print('연산자 오류')
'''

#2 (음수 양수 판별 프로그램)
'''
c=int(input('숫자를 입력하세요:'))
if c>0 :
    print('양수')
elif c==0 :
    print('0')
else :
    print('음수')
'''

#3 (반복문 복습)
#117 pg
'''
money=3000
card=True
if money>=3600 and card:
    print('택시타고 가라')
else:
    print('걸어 가라')
'''


#4 (성적 관리 프로그램)
#A : 100~91
#B : 90~81
#C : 80~71
#D : 70~61
#F : 60~
#입력 : 점수, 출력 : 등급
'''
score=int(input('점수를 입력하세요: '))
if 100>=score and 90<score :
    grade='A'
elif 90>=score and 80<score :
    grade='B'
elif 80>=score and 70<score :
    grade='C'
elif 70>=score and 60<score :
    grade='D'
elif 0==score :
    grade='빵점'
else:
    grade='F'
print(f'---------------------------------------------\n점수 = {score}\n등급 = {grade}')

if grade=='빵점':
    print('재수강 하세요.')
elif grade=='F':
    print('재수강 하세요.')
else:
    print('잘했어요.\n---------------------------------------------')
'''

#5 (게임)

import random # random 패키지 사용
num = int(input('숫자를 입력하세요:'))
f = random.randrange(1, 1000) # 1 이상 1000 미만의 숫자를 랜덤 생성
if f==num:
    print('정답')
else:
    print('오답')
print(f'정답은{f}입니다.')










