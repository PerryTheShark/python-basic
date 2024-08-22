import math

n = int(input())
lst = []
for i in range(1,n+1):
    lst.append(i)

def is_square_number(num):
    num2 = int(math.sqrt(num))
    if num2*num2 == num:
        return True
    else:
        return False

result_filter = list(filter(is_square_number, lst))
tmp = list(map(is_square_number, lst))

print("This is result using filter:", *result_filter)
print("This is result using map: ", end = "")
for i in range(0,n):
    if tmp[i]:
        print(lst[i],end = " ")
