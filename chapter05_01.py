
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

# *args, **kwargs

# *args(언팩킹) -> 튜플형태
def args_func(*args):  #매개변수가 자유 # 매개변수가 가변인자를 사용할 수 있도록 해주는 것임 
    for i,v in enumerate(args):
        print('Result : {}'.format(i),v)
    print('-------------')

args_func('Lee') 
args_func('Lee','Park')
args_func('Lee','Park','Kim')
# 동적으로 유연하게 투플형태로 보내줌   

# **kwargs(언팩킹) -> 딕셔너리 형태
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v),kwargs[v])
    print('-----')
    
kwargs_func(name1='Lee')
kwargs_func(name1='Lee',name2='HJ')
kwargs_func(name1='Lee',name2='HJ',name3='Cho')

# 전체 혼합 
def example(args_1,args_2,*args,**kwargs):
    print(args_1,args_2,args,kwargs)
    
example(10,20,'Lee','Kim','Park',age1=20,age2=20,age3=30)
# -> 10 20 ('Lee', 'Kim', 'Park') {'age1': 20, 'age2': 20, 'age3': 30}

# 중첩 함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In Func')
    func_in_func(num+100)
    
nested_func(100)
# func_in_func(100) : is not defined 

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결 
# 함수는 객체를 생성하고 리소스 할당
# 람다는 즉시 실행함수(Heap 초기화) -> 메모리 초기화 
# 남발시 오히려 가독성 감소 

def mul_func(x,y):
    return x*y

q=mul_func(10,50)
print(q)

# 람다 함수-> 할당
lambda_mul_func=lambda x,y:x*y
print(lambda_mul_func(50,50))

# 같은 결과 

def func_final(x,y,func):
    return x*y*func(100,100)

print(func_final(10,20,lambda_mul_func) )