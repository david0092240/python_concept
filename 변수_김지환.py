#2023_05_12(FRI)

#1

'''
a=float(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
'''

#2
'''
a=int(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))

print('a=%d 입니다, b=%d입니다'%(a,b))
'''

#3

name=input('이름을 입력하세요:')
age=int(input('나이를 입력하세요:'))
height=float(input('키를 입력하세요:'))
print('제 이름은 %s입니다. \n 나이는 %d살, 키는 %fcm.'%(name,age,height))

hope=float(input('희망하는 키를 작성해라:'))
print('제 이름은 %s입니다. \n나이는 %d살, 희망키는 %fcm.'%(name,age,hope))

tmp=hope-height

print('그럼 앞으로 %fcm 만큼 커야겠네요 ㅋㄷ' %(hope-height))
