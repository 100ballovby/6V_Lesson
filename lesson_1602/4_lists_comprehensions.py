squares = []  # список, в котором я буду хранить квадраты чисел
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

#########################################################

squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)
