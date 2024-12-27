
# chapter04-1 
# 파이썬 실습
# if 실습

# 관계 연산자 실습
# 논리 연산자 실습
# 일반 조건문
# 다중 조건문
# 중첩 조건문
 
 
 # 기본 형식
print(type(True)) # 0이 아닌 수 , "abc", [1,2,3,],(1,2,3.... )....
print(type(False)) # 0, " ",[],(),{} ... 비어있으면 False

# 예제1
if True:
   print('Good')

if False:
    print('Bad')

# 예제2
if True:
   print('Bad!')
else:
    print('Good !')
    
    
# 관계 연산자
# >, >=, <, <=, ==, !=

x=15
y=10

# 양 변이 같은 경우 참 
print(x==y)
# 양 변이 다를 경우 참 
print(x != y)

# 왼쪽이 클때 참 
print(x>y)
# 왼쪽이 크거나 같을때 참 
print(x>=y)
# 오른쪽이 클 때 참
print(x<y)
# 오른쪽이 크거나 같을때 참 
print(x<=y) 

# 예제3
city=""  
if city:
   print('you are in: ',city)

else:
    print('please enter your city')
    
# 예제4
city="Seoul"  
if city:
   print('you are in:',city)

else:
    print('please enter your city')
    
    
# 논리 연산자 (중요)
# and,or,not

a=75
b=40
c=10

print('and :', a>b and b>c)
print('or :', a>b or b>c)
print('not', not a>b)
print('not', not b>c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선 순위
# 산술 -> 관계 -> 논리 순서 
print('e1 : ',3+12 > 7+3)
print('e2 : ', 5+10 * 3  > 7+3*20)
print('e3: ', 5+10>3 and 7+3==10)
print('e4: ', 5+10 > 0 and not 7+3 == 10) # == False
# and는 둘다 true여야 TRUE 

score1=85
score2='A'

# 복수의 조건이 모두 참일경우 실행 

if score1>=90 and score2 == 'A':
   print('PASS')
   
else:
   print('Fail')
   

# 예제 5

id1='vip'
id2='admin'
grade='platinum'

if id1=='vip' or id2=='admin':
   print('관리자 입장')

if id2=='admin' and grade=='platinum':
   print('최상위 관리자')


# 예제6

num=50

if num >=90:
   print('Grade: A')

elif num >= 80:
    print('Grade: B')
    
elif num >= 70:
    print('Grade: C')
    
else:
   print('Grade: FAIL')  
   
# 예제7 - 중첩 조건문 
   
grade='A'
total=88

if grade == 'A':
   if total >= 90:
      print('장학금 100%')
   elif total >=80:
      print('장학금 80%')
   else:
      print('장학금 50%')

else:
   print('장학금 없음 ')

# in, not in
a=[10,20,30]
w={70,80,90}
e={"name" : "LEE", "CITY" : "SEOUL", "GRADE " : "A"}
r=(10,12,14)

print("name" in e)
print("SEOUL" in e.values()) # 딕셔너리에서 값을 가져옴

