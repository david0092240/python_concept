'''
list1 = ['abc', 'dfg', 'hij', 123, 456]
list1[1]='park'
print(list1)


arr1=[]
a=1
while True:
    if a==100: break
    arr1.append(4*a)
    a=a+1
print(arr1)
'''
'''
arr=[12,134,6143,4,241]
size=len(arr) #리스트의 크기 변수
print(size)

idx=0 #인덱스 변수
while True:
    idx1=idx+1
    if idx1==size : break
    if arr[idx] > arr[idx1]:
        tmp=arr[idx] #tmp : 임시 변수
        arr[idx]=arr[idx1]
        arr[idx1]=tmp
    idx=idx+1
    print(arr)
print('---'*10)
arr.sort()
print(arr)
arr.reverse()
print(arr)
'''
'''
# 내 생일 요일 찾기
import datetime
today=datetime.datetime.now()
print(f'오늘은 {today.year}년도 입니다.')
print(f'오늘은 {today.month}월 입니다.')
print(f'오늘은 {today.day}일 입니다.')

if today.weekday() == 6 or today.weekday() == 5:
    print('주말')
else:
    print('평일')

print('---'*10)

print('태어난 날의 요일 맞추기')
y=int(input('년 입력:'))
m=int(input('월 입력:'))
d=int(input('일 입력:'))

date=datetime.datetime(y,m,d)

if date.weekday()==0:print('월')
elif date.weekday()==1:print('화')
elif date.weekday()==2:print('수')
elif date.weekday()==3:print('목')
elif date.weekday()==4:print('금')
elif date.weekday()==5:print('토')
elif date.weekday()==6:print('일')
'''

import random
while True:
    #컴퓨터
    com=random.choice('RSP')
    user=input('R, S, P 중 하나 고르세요:')

    if user==com:
        print('비김')
    elif (com=='R' and user=='P') or (com=='S' and user=='R') or (com=='P' and user=='S'):
        print('이김')
        break
    else:
        print('짐')

    print(f'컴퓨터 : {com}, 인간 : {user}')
