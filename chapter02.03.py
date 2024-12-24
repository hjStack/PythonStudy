
n=700

print(n)
print(type(n))

x=y=z=700
print(x,y,z)

var=75
var="Change Value"

print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력 

# 예) 
print(300)
print(int(300))

# 예2)
# n -> 777
n=777

m=800
n=655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
# => 이건 m,n의 값이 똑같기 때문에 하나의 오브젝트를 두개의 값이 참조 
# 파이썬의 엔진의 성능을 위한것임 
# id(identity) 확인 : 객체의 고유값 확인
# 둘중 하나의 값이 달라진다면 그때 값이 다르므로 각자 오브젝트를 생성해서 id값이 다르게 나오는 것을 알 수 있음 

m=800
n=800

print(id(m))
print(id(n))

print(id(m) == id(n))

# 다양한 변수 선언 방법
# CamelCase : numberOfCollegeGraduates -> Method 
# Pascal Case : NumberOfCollegeGraduates -> Class
# snake case : number_of_college_graduates : 파이썬에서 변수를 선언할때 많이 사용가능 

# 허용하는 변수 선언 
age=1
Age=1
aGe=3
AGE=1

a_g_e=5
_age=5
age=6
age=7
_age_=7

# 예약어는 변수명으로 불가능 
