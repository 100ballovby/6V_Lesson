'''Задание 1'''
nums = [14, 21, 565, 18, 33, 20, 102, 108, 167, 891, 400]
for number in nums:
    if number % 2 == 0:
        nums.remove(number)

print(nums)
'''Задание 2'''
sentence = ['The', 'quick', 'brown', 'fox', 'jumps',
            'over', 'the', 'lazy', 'dog']
longer_than_4 = [word for word in sentence if len(word) >= 4]
l_4 = []
print(longer_than_4)
for word in sentence:
    if len(word) >= 4:
        l_4.append(word)
print(l_4)

'''Задание 3'''
kvadrati = []
for number in range(1, 31):
    kvadrati.append(number ** 2)
print(kvadrati)
print('Первые 5 элементов: ', kvadrati[:5])
print('Последние 5 элементов: ', kvadrati[25:])