
# chapter05-01
# 함수 
# 파이썬 함수식 및 람다

# 함수 정의 방법
# 예제1
def first_func(w):
    print("Hello, ",w)
    
word="Good boy"
first_func(word)  # 이 함수 자체가 파이썬의 객체 

print(first_func) # <function first_func at 0x1025294e0>

# 예제2

def return_func(w1):
    return "Hello, "+ str(w1)

x=return_func('Good girl')
print(x)

# 예제3 - 다중반환 

def func_mul(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return y1,y2,y3

# 언팩킹 
x,y,z=func_mul(10)

print(x,y,z)

# 튜플리턴
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return (y1,y2,y3)

q=func_mul2(20)
print(type(q),q) # <class 'tuple'> (200, 400, 600)

print(type(q),q,list(q))

# 리스트 리턴
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return [y1,y2,y3] #  <class 'list'> [300, 600, 900]

p=func_mul2(30)
print(type(p),p) # <class 'tuple'> (200, 400, 600)

# 딕셔너리 리턴 
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return {'v1' : y1,'v2':y2,'v3' : y3} #  <class 'list'> [300, 600, 900]

d=func_mul2(30)
print(type(d),d,d.keys(),d.items(),d.get('v2')) # <class 'dict'> {'v1': 300, 'v2': 600, 'v3': 900}
