
# Chapter02_1
# 파이썬 기초

# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print()
print('''Python Start! ''')
print("""Python Start! """)

print()


#Separater() option
print('P','Y','T','H','O','N',sep='')
print('010','7777','1234',sep='-')
print('python','google.com',sep='@')

print()


# end 옵션
print('welcome to ',end=' ')
print('IT News',end='')
print('Web site')
print()

# file 옵션
import sys
print()
print('Learn python',file=sys.stdout)

#format 사용(d,s,f)
# d=digit s=string f=float

print('%s %s' %('one','two'))  # 정석
print('{0} {1}'.format('1','two')) # 가독성 증가  
print('{1} {0}'.format('one','two'))

print('{1} {3} {2}'.format('2','5','10','15'))
# format앞은 인덱스 번호 

print()

print('%-10s' %('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
# 중앙정렬
print('{:^10}'.format('nice'))

print('%5s' %('pythonstudy'))
print('%.5s' %('pythonstudy')) #5개 공간에서 5개만 절삭
print('{:10.5}'.format('pythonstudy')) #10개의 공간에서 5개의 글자만 출력

print()

#%d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))
print('%4d' %(42,))
print('{:4d}'.format(42))

print()

# %f
print('%f' %(3.14159687890))
print('{:f}'.format(3.14159278780))

print('%06.2f'%(3.141592653589793)) # 총 8자리
print('{:06.2f}'.format(3.14159265359876))

print()