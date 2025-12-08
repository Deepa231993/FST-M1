tuple_num = input("Enter list of numbers : ")

tuple_num = tuple(int(n) for n in tuple_num.split(","))

print("Numbers divisible by 5:")
for num in tuple_num:
    if num % 5 == 0:
        print(num)
