# 문자열
sentence = 'hello world'
print(sentence)
sentence2 = """
    hello world
    hello python
"""
print(sentence2)

# slicing
jumin = "920531-1234567"
print("주민번호: " + jumin)
print("성별: " + jumin[7])
print("년도: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("뒤에서부터 출력: " + jumin[-7:]) #뒤에서부터 7자리 출력

# 문자열 처리 함수
python = "Hello World"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

index = python.index('o')
print(index)
index2 = python.index('o', index+1)
print(python.find("Hello"))
print(python.count('l'))

# 문자열 포맷
print("나는 %d살 입니다" % 30)
print("내가 배우는 언어는 %s 입니다." %'python')
print("Apple은 %c로 시작합니다" %'A')
print("나는 %s와 %s를 할 줄 알아요." %("java","python"))

print("나는 {}살 입니다.".format(20))
print("나는 {}와 {}를 할 줄 알아요.".format("java","python"))
print("나는 {1}와 {0}를 할 줄 알아요.".format("java","python"))
print("나는 {age}살이고 {language}를 할 줄 알아요".format(age=30, language="python"))

# python 3.6 이상부터 가능
age=20
language="C++"
print(f"나는 {age}살이고 {language}를 할 줄 알아요")

# 탈출문자
print("안녕하세요. 줄바꿈\n \"python\"")
print("\\ 이건 역슬레시")
print("red Apple\r \\r은 커서 맨 앞으로 이동")
print("\\b는 삭제\b제")
print("\\t 는\ttab")

# 퀴즈
# 사이트 비밀번호 만들기
# ex) https://naver.com
# 규칙
# - https:// 제외
# - '.' 이후 제외
# - 남은 글자중 앞 3글자 + 글자개수 + 글자내 e 개수 + !

url = 'https://naver.com'
tempStr = url[url.index('/') + 2 : url.index('.')]
password = tempStr[0:3] + str(len(tempStr)) + str(tempStr.count('e')) + '!'
print(password)



