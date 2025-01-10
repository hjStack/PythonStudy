
# Set
# 집합은 순서 x, 중복 x


#선언
a=set()
b=set([1,2,3,4])
c=set([1,4,5,6])
d=set([1,2,'Pen','Apple'])
e={'foo','bar','bax','a'} # 키가 없고 리스트라 나열되듯이 되면 이것도 집합
f={42,'foo',(1,2,3),3.1459}

# print(a) #set()
# print(b)
# print(e)

print('a--',type(a),a)
print('b--',type(b),b)
print('c--',type(c),c)
print('d--',type(d),d)
print('e--',type(e),e)
print('f--',type(f),f)
# => 내부적으로 자체 중복은 제거

# 튜플 변환(set -> tuple)
t=tuple(b)
print('t-',t,type(t))
# 튜플로 바뀔 수 있다는건 인덱싱을 할 수 있는것
print('t--',t[0],t[1:3])

# 리스트 변환(set -> list)
l=list(c)
l2=list(e)

print('l-',l)
print('l2',l2)

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용 

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print('s1 & s2 : ',s1&s2)  # 집합의 교집합
print('s1 & s2 : ',s1.intersection(s2))  # 집합의 교집합

# 합집합
print('s1 | s2: ',s1 | s2) # s1 | s2:  {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2',s1.union(s2))

#차집합
print('s1-s1 : ',s1-s2)
print('s1-s2 : ',s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ',s1.isdisjoint(s2)) # false -> 교집합 원소가 있음

# 부분집합 확인
print('s1.issubset(s2) :',s1.issubset(s2)) # false -> s1이 s2의 부분집합이 아님
print('superset: ',s1.issuperset(s2))  #s1이 s2를 포함하는 집합인지의 여부 

# 추가 & 제거
s1=set([1,2,3,4])
s1.add(5)

print('s1 - ',s1) # {1, 2, 3, 4, 5}

s1.remove(2) 
print('s1 - ',s1) # {1, 3, 4, 5}

s1.discard(3)
print('s1 - ',s1) # {1, 4, 5}

s1.clear() 
print('s1 - ',s1) # set()