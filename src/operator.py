# 연산자
print(1+2)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(8%3)
print(10//3)

print(1 != 3)
print(not(1 != 3))

print((3>0) and (3<5))
print((3>0) & (3<5))
print((3>0) or (3<5))
print((3>0) | (3<5))

# 숫자처리 함수
print(abs(-5))  #5
print(pow(4,2)) #16
print(max(1,5))
print(min(1,5))
print(round(3.14))

from math import *

number = 4.99
print("원본: " + str(number))
print("내림: " + str(floor(4.99)))
print("올림: " + str(ceil(4.99)))
print("16의 제곱근: " + str(sqrt(16)))

# 랜덤함수
from random import *

print(random()) # 0.0~1.0 random 값
print(random()*10) # 0.0~10.0 random 값
print(int(random()*10)) #0~10
print(int(random()*10))
print(int(random()*10) + 1) #1~10

print(randrange(1, 46))  #1~45
print(randint(1, 45))   #1~45

#Quiz
# 월 4회 스터디 진행
# 3회는 온라인으로, 1회는 오프라인으로 
# 오프라인 스터디 일자를 구해라
# 조건
# 1. 일자 랜덤생성
# 2. 각 월별 일자는 28일까지 있다고 가정
# 3. 1~3일은 제외
day = randint(4, 28)
print("오프라인 스터디 날짜는 매월 " + str(day) +"일로 선정")


