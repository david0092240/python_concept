# 1 (구구단 1~9단 출력)
'''
for j in range(1,20,1):
    for i in range(1,10,1):
        mul=j*i        # mul 선언
        print(f'{j} x {i} = {mul}')
    print('==='*15)
'''

#2 (for문 문제)
'''
#1부터 100까지 홀수만 출력
#case 1
for i in range(1,101,2):
    print(i)
    
#case 2
for i in range(1,101,1):
    if i%2==1:
        print(i)
'''
#5부터 100까지 5의 배수 출력
'''
for i in range (5,101,5):
    print(i)
'''
#10000까지의 제곱수를 출력
'''
#case 1
for i in range(1,101,1):
    a=i*i
    print(a)

#case2
for i in range(1,101,1):
    print(i**2)
'''
#세제곱
'''
for i in range(1,11,1):
    print(i**3)
'''

#p.146 문제 (1)
'''
a='Life is too short, you need python'

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
'''
#p.146 문제(2)

#case1 (while문)
result = 0
i = 1
while i <= 1000:
    if i%3==0 :
        result = result+i
    i = i+1

print(result)

#case2 (for문)
result=0
for i in range (1,1001,1):
    if i%3 == 0:
        result += i
    i+=1
print(result)







