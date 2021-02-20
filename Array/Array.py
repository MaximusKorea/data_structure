# 1차원 배열 : 파이썬의 경우 list로 구현한다.
data = [1,2,3,4,5]
print(data)
# 2차원 배열
data2 = [[1,2,3],[4,5,6],[7,8,9]]
print(data2)

dataset = ["apple","banana","kiwi","watermelon","peach","orange","grape"]
print(dataset)

# 위의 dataset에서 p는 몇번 들어가있는 지 count해보기

count = 0
for data in dataset:
     for index in range(len(data)):
         if data[index] == 'p':
             count += 1

print(count)

# dataset을 2차원 배열로 봐서 count해준다.