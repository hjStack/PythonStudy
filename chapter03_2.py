
# chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1="I am python"
str2='python'

str3="""How are you?"""
str4='''Thank you !'''

print(type(str1))
print(type(str2))

print(len(str1),len(str2),len(str4))

# 빈 문자열 
str_t1=''
str_t2=str() # 빈 문자열 생성

print(type(str_t2),len(str_t2))

print('I\'m a boy')

escape_str1="Do you have a \"retro games\"?"
print(escape_str1)

# Raw String
raw_s1=r'D:\python\test' # 드라이버 경로 복사
print(raw_s1)


# 역슬래시를 사용해서 멀티라인 입력
multi_str=\
'''
문자열
멀티라인 입력
테스크
'''

print(multi_str)

# 문자열 연산 
str_o1='python'
str_o2='apple'
str_o3='How are you doing ?'
str_o4='Seoul Daejeon Busan Jinju'

print(str_o1*3)
print(str_o1+str_o2)

# str : 문자열(시퀀스)
# list : 리스트(시퀀스)
# tuple : 튜플(시퀀스)

print('y' in str_o1)

# 문자열 형 변환
print()

# 문자열 함수 

print("Capitalize :", str_o1.capitalize()) # 첫번째 글자를 대문자로 바꿔주는 함수 
print("endswidth : ", str_o2.endswith("e")) # 마지막 문자를 체크하는 함수
print("replace : ",str_o1.replace("thon",'good'))
# thon -> good으로 변경 

print("sorted : ",sorted(str_o1))
print("split : ", str_o4.split(' '))
# 특정 단어 단위로 구분 

# 반복 (시퀀스 - 순서가 있는 배열 형태)

im_str="Good boy"
print(dir(im_str)) # __iter__ 

# 출력 
for i in im_str:
    print(i) 
# 문자열은 시퀀스이기에 슬라이싱이 가능 

# 슬라이싱
str_s1="Nice Python"
print(str_s1[0:3])
print(str_s1[5:]) # [5:11]
print(str_s1[:len(str_s1)])
print(str_s1[-5:])
print(str_s1[::2]) #처음부터 끝까지 가져오는데 2개씩 가져옴 
print(str_s1[::-2]) # 처음부터 끝까지 가져오는데 역순으로 가져오기 

# 아스키 코드 (또는 유니코드)

a='z'
print(ord(a)) # 문자 -> 아스키코드
print(chr(122)) # 아스키코드 -> 문자