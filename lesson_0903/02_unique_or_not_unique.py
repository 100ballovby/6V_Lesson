from random import randint
arr = []
for i in range(10):
    arr.append(randint(1, 15))
# ^ заполняю список случайными числами от 1 до 15 в количестве 10 штук

print(arr)

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print('Есть одинаковые!')
            quit()
