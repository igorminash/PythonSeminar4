n = int(input("Введите кол-во высаженных кустов: "))

num_blueberries = []

for i in range(n):
    blueberries = int(input("Введите кол-во черники на каждом кусте: "))
    num_blueberries.append(blueberries)
print(num_blueberries)

max_sum = 0

for i in range(0, len(num_blueberries)-1):
    summa = num_blueberries[i] + num_blueberries [i+1] + num_blueberries[i-1]
    print(summa)
    if summa > max_sum:
        max_sum = summa
    if  num_blueberries[0] + num_blueberries[-1] + num_blueberries[-2] > max_sum:
        max_sum = num_blueberries[0] + num_blueberries[-1] + num_blueberries[-2]
        print(max_sum)

print(f"Максимальное кол-во ягод: {max_sum}")





    
    
