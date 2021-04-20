'''Task 2. Определить, является ли слово палиндромом.
Палиндром - это слово, которое одинаково читается
с обеих сторон.

радар
асса
aboba
ишак ищет у тещи каши
'''
message = input('Введите что-то: ').strip().lower()

print(message == message[::-1])

reverse = ''
for symbol in range(len(message)-1, -1, -1):
    reverse += message[symbol]
print(message == reverse)

