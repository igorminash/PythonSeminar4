
n = int(input("Введите кол-во первого множества: "))

my_list = []

for i in range(n):
    i = int(input())
    my_list.append(i)

m = int(input("Введите кол-во второго множества: "))

my_list2 = []

for j in range(m):
    j = int(input())
    my_list2.append(j)

print(my_list)
print(my_list2)

new_list = []

for i in my_list:
    for j in my_list2:
        if i == j and i not in new_list:
            new_list.append(i)
            new_list.sort()
print(new_list)

# ВТОРОЙ СПОСОБ

# n = int(input("Введите кол-во первого множества: "))

# my_list = set()

# for i in range(n):
#     i = int(input())
#     my_list.add(i)

# m = int(input("Введите кол-во второго можества: "))

# my_list2 = set()

# for j in range(m):
#     j = int(input())
#     my_list2.add(j)

# print(my_list)
# print(my_list2)

# new_list = my_list.intersection(my_list2)

# print(sorted(new_list))







