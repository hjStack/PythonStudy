
# chapter04_2
# 파이썬 반복문 

# 코딩의 핵심
# for in <collection>
#     <loop body>

for v1 in range(100):
    print('v1 is',v1)
    
print()

for v2 in range(1,11):
    print('v2 is',v2)

print()

for v3 in range(1,11,2):
    print('v3 is',v3)

print()

sum1=0

for i in range(1,1001):
    sum1 +=i
    
print('sum =',sum1)
print('1 ~ 1000 sum =', sum(range(1, 1001)))
print(type(range(1,11))) # <class 'range'>

print('1부터 1000까지 4의 배수의 합 :',sum(range(1,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전 (딕셔너리)
# Iterables는 모두 for문에서 사용 가능함
# iterable 리턴 함수 : range(),reversed,enumerate,map,zip

names=['kim','park','Cho','Lee','Yoo']

for name in names:
    print('You are',name)
    

# 예제2 
lotto_numbers=[11,19,21,28,36,37]

for n in lotto_numbers:
    print("Current number:",n)
    
    
my_info={
    "name":"lee",
    "age":33,
    "City":"Seoul"
}

for k in my_info:
    print('key: ',my_info[k])

# 딕셔너리의 value를 가져오는것
for v in my_info.values():
    print('value : ',v)
    
for v in my_info.keys():
    print('keys : ',v)


# 예제5 - 대문자는 대문자로, 소문자는 대문자로

name='FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
        
        
# 예제6 - break # 순차 검색 

numbers=[14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 14:
        print('FOUND 14 !')
        break
    else:
        print('not found : ',num)


# continue
# 다시 조건 검사 
# 숫자만 출력하는 경우

lt=["1",2,4,True,4.3,complex(4)]

for v in lt:
    if type(v) is bool:  # 자료형 대조
        continue  # boolean형을 만나면 밑에 print문은 실행되지 않고 다음 4.3검사함 
    print("current type: ",v,type(v))
    print("multiply by 2",v*3)
    

# for - else

numbers1=[14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 3:
        print("found : 3")
        break
else:
    print("not found : 3")

# 구구단 

for i in range(2,10):
    for j in range(1,10):
        # print(f'{i} * {j} = {i*j}')
        print('{:4d}'.format(i *j),end=' ')
    print()

# format() example
# format() : '{인덱스0}, {인덱스1}'.format(값0, 값1)
# s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)

# 변환 예제 
name2='Aceman'

print('Reversed : ',reversed(name2))
print('List로 형변환 :',list(reversed(name2)))
print('tuple로 형변환 :',tuple(reversed(name2)))
print('set로 형변환 :',set(reversed(name2))) # 순서를 중시하지 않으므로 랜덤으로 발생 



