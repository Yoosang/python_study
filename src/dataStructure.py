# list
sample_list = [10, 'a', "list"]
print(sample_list)

subway = ["a", "b", "c"]
print(subway.index("b"))
subway.append("z")
print(subway)
subway.insert(1,"d",)
print(subway)
print(subway.pop())
print(subway)
subway.append("a")
print(subway)
print(subway.count("a"))
subway.sort()
print(subway)
subway.reverse()
print(subway)
subway.clear()
print(subway)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


# dictionary
sample_dic = {1:"a", 30:"b", 17:"z"}
print(sample_dic.get(2))
print(sample_dic[30])
print(sample_dic.get(2, "new"))
print(2 in sample_dic)

cabinet = {"a-3":"아메리카노", "b-40":"카페라떼"}
cabinet["c-10"] = "카푸치노"
print(cabinet)

cabinet["a-3"] = "디카페인"
print(cabinet)

del cabinet["b-40"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()


# tuple(변경불가, 속도가 list보다 빠름)
sample_tuple = ("아메리카노", "4100원")
print(sample_tuple[0])
print(sample_tuple[1])

(menu, price, name) = ("아메리카노", "4100", "스타벅스")
print(menu, price, name)


# set (중복없고 순서없음)
sample_set = {1,2,3,1,2}
print(sample_set)

set1 = {"java", "python", "go", "swift"}
set2 = set(["C++", "java", "c", "go"])
print(set1 & set2)
print(set1.intersection(set2))
print(set1 | set2)
print(set1.union(set2))
print(set1-set2)
print(set1.difference(set2))
set1.add("kotlin")
print(set1)
set1.remove("go")
print(set1)


# 자료구조 변경
dataStructure = {"list", "dictionary", "set"}
print(type(dataStructure))
dataStructure = list(dataStructure)
print(type(dataStructure))
dataStructure = tuple(dataStructure)
print(type(dataStructure))


# Quiz
from random import *
users = list(range(1, 21))
shuffle(users)
print("user list: " + str(users))

winners = sample(users, 4)
print("winners: " + str(winners))
print("1등: {0}".format(winners[0]))
print("나머지: {0}".format(winners[1:4]))


