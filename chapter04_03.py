
# 파이썬 반복문 
# while(조건):
#    <statement(s)>

# 예제1
n=5
while n>0:
    print(n)
    n=n-1
    
# 에제2
a=['foo','bar','baz']

while a:
    print(a.pop())  #stack - LIFO 

# 예제3
# break,continue

n=5
while n>0:
    n-=1
    if n == 2:
        break  #while문을 빠져나감
    print(n)
    
print('Loop end')

# 예제4
m=5
while m>0:
    m-=1
    if m == 2:
        continue
    print(m)
    
print('Loop end')

# 예제5
# if 중첩

i=1
while i<=10:
    print('i:',i)
    if i == 6:
        break
    i+=1

# 예제7
# while-else

n=10
while n>0:
    n -=1
    print(n)
    if n == 5:
        break
# break문을 만나지 않으면 else문을 만나고 종료 
else:
    print('else out')
    
# 예제8
a=['foo','bar','baz','qux']
s='hj'

while i<len(a):
    if i == s:
        break
    i +=1
else:
    print(s,'not found in list')
    
# 무한 반복 유의
# while True:  -> 이렇게 쓰면 무한 반복이 나옴

# 예제8
# if not a -> false 

a=['foo','bar','baz','qux']

while True:
    if not a:
        break
    print(a.pop())
    