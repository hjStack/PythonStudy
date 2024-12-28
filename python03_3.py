
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
print('c*3 ',c*3)
print(" 'test' + c[0] : ", 'Test' +str(c[0]))