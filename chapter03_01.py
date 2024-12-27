
# chapter 03-1
# 숫자형 

# 파이썬 지원 자료형 

## 
# int 
# float  
# complex
# bool
# str: 문자열(시퀀스)
# list : 리스트(시퀀스)
# tuple : 튜플(시퀀스)
# set : 집합
# dict : 사전
# ## 

# 데이터 타입
str1="python"
bool=False
str2='Anaconda'
float_v=10.0
int_v=7

list=[str1,str2]
print(list)

# 사전 형태
dict={
    "name":"Machine Learning",
    "version": 2.0
}
tuple=(7,8,9)
set={3,5,7}

# 데이터 타입
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자

# +
# -
# *
# /
# %

# abs(x) : 절대값
# pos(x,y) == x ** y 

# 정수 선언
i=77
i2=-14
big_int=7777777777777777799999999999999

print(i)
print(i2)
print(big_int)
print() 

# 실수 출력
f=0.9999
f2=3.141592
f3=-3.9
f4=3/9

print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1=39
i2=939
big_int1=777777777778888889999993343434
big_int2=343238383874747474009999911111
f1=1.234
f2=3.939


print(">>>>>>>+")
print("i1+i2: ", i1+i2)
print("f1+f2 :",f1+f2)
print("big_int1 + big_int2: ",big_int1+big_int2)
print()

# 정수와 실수를 더하면 자동으로 형변환이 이루어짐

print(">>>>>>>*")
print("i1*i2: ", i1+i2)
print("f1*f2 :",f1+f2)
print("big_int1 * big_int2: ",big_int1+big_int2)

# 형 변환 실습
a=3.0
b=6
c=.7
d=12.7

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형 변환 
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(int(False))

print(abs(-7))
x,y=divmod(100,8)
print(x,y) # 몫과 나머지 한번에 출력

print(pow(5,3))

# 외부 모듈
import math
print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 => 6



