
# 파이썬 02.02_ex1
# 파이썬 완전 기초

# 프린트 3가지 Print Formatting


# 3가지 Format Practices
x=50
y=100
text=308276567
n='Lee'

# 출력1
ex1='n=%s, s=%s, sum=%d' %(n,text,(x+y))
print(ex1)

# 출력2

ex2='n={n},s={s},sum={sum}'.format(n=n,s=text,sum=x+y)
print(ex2)

# 출력3-f string
ex3=f'n={n},s={text},sum={x+y}'
print(ex3)


# 구분기호
m=100000000
print(f'm={m:,}') 
print()

# 정렬
# ^ : 가운데, <:왼쪽, >:오른쪽

t=20
print(f't center={t:^10}') #총 10자리 확보
print(f't left sorting={t:<10}') #총 10자리 확보
print(f't right sorting={t:>10}') #총 10자리 확보

print()
print()

print(f't center = {t:*^10}') #총 10자리 확보
print(f't center = {t:#^10}') #총 10자리 확보



