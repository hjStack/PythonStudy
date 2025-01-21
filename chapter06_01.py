
# OOP
# 파이썬 클래스
# self, 인스턴스 메소드, 인스턴스 변수 

# 클래스 and 인스턴스 차이 이해
# 예제1

class Dog(object): #object 상속
    # 클래스 속성
    species='FirstDog'
    
    # 초기화/인스턴스 생성 -> 생성자 개념
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
# 인스턴스는 객체에 포함 
print(Dog)

# 인스턴스화
# 인스턴스 : 클래스의 객체를 코드로 구현한 시점, 어떤 변수로 활용할 수 있는 대상
a=Dog("휴지",5);
b=Dog("마리",4);
c=Dog("마리",4);

print(a == b,id(a),id(b),id(c)) # False 4336638608 4336333392 4336333712

# 네임스페이스 : 객체를 인스턴스화할때 저장된 공간
print('dog1',a.__dict__)
print('dog2',b.__dict__)
# 결과 
# dog1 {'name': '휴지', 'age': 5}
# dog2 {'name': '마리', 'age': 4}

# 클래스 변수: 직접 접근 가능, 공유 
# 인스턴스 변수: 객체마다 별도로 존재 

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name,a.age,b.name,b.age)) # 휴지 is 5 and 마리 is 4

if a.species == 'FirstDog':
    print('{0} is a {1}'.format(a.name,a.species))
    
print(Dog.species) #FirstDog
print(a.species) # FirstDog
print(b.species) # FirstDog