from functools import reduce
my_list = [1,2,3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(my_list)
print(reduce(accumulator, my_list, 0))
print()

print(reduce(accumulator, my_list, 10))


