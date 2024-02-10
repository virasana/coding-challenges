from itertools import product

input1 = "1 2 3"
input2 = "4 5 6"
# list1 = list(map(int, input1.split()))
# list2 = list(map(int, input2.split()))
list1 = [int(x) for x in input1.split()]
list2 = [int(x) for x in input2.split()]

print(*product([1, 2, 3], [4, 5, 6]))

