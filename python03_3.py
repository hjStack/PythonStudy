
# chapter03_03.py
# 파이썬 리스트
# 자료구조에서 중요

# 리스트 자료형(순서o, 중복o, 수정O, 삭제O)

# 선언 
a=[]
print(type(a))

b=list()
c=[70,75,80,85]
print(len(c))
d=[1000,10000,'Ace','Base','Captain'] # 파이썬은 서로 다른 자료형일지라도 리스트에 담을 수 있음
e=[1000,10000,['Ace','Base','Captain']]
f=[21.42,'footbar',3,4,False,3.141592]


# 인덱싱 - 원하는 데이터를 꺼내는 과정
print('>>>>')
print('d ----  ',type(d),d)
print('d ---',d[1])
print('d ---',d[-1])
print('d ---',d[-2])
print('d ---',d[-3])

print('e --',e[-1][1]) # 맨 끝에서부터 -1 -2 -3 
# 문자열은 시퀀스
print('e --',list(e[-1][1])) # 결과 : e -- ['B', 'a', 's', 'e']

print('d -- ',d[0:3])
print('d -- ',d[2:])

# 리스트 연산 
# 리스트 + 리스트 = 리스트

print('c+d',c+d)
print(" 'test' + c[0] : ", 'Test' +str(c[0]))

print(c == c[:3]+c[3:])
print(c)
print(c[:3])
print(c[3:])

# identity(id)
# 리스트도 하나의 주소를 공유
temp=c 
print(temp,c)
print(id(temp))
print(id(c))

print()

# 리스트 수정 삭제
c[1:2]=['a','b','c']
print('c =',c)

c[1]=['a','b','c']
print('c --',c)

c[1:3]=[]
print('c -- ',c)
# 공백으로 만들기

# 리스트 요소 삭제
del c[2]
print('c --',c)

# 리스트 함수
a=[5,2,3,1,4]
a.append(10) # 리스트 마지막에 데이터를 삽입하는 함수
print('a = s',a)

a.sort()
print('a -',a)

a.reverse()
print('a =',a)

print('a=',a[3])

a.insert(2,7) # 특정 위치에 값을 추가 
print(a)

# 리스트의 요소를 제거할때는 remove()
a.remove(10)
print('a =',a)
# 리스트의 요소를 제거할때는 인덱스로 하면 특정 값의 인덱스를 알아야 하므로
# pop() : 마지막 index에 해당화는 원소를 가져오고 나머지 원소들로 리스트 재구성

# stack #queue

print('a =',a.count(4))

# 반복문 활용

while a:
    data=a.pop()
    print(data)
# 끝에서부터 데이터를 하나씩 가져옴 
