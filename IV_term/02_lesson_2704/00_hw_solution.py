# simple
message1 = input('Input smth: ')
num1 = []
for letter in message1:
    if letter.isnumeric():
        num1.append(letter)

print(num1)

# middle
message2 = input('Input smth: ')
num2 = []
for letter in message2:
    try:
        num2.append(int(letter))
    except:
        pass
print(num1)

# hard
import string
numbers = string.digits  # 0123456789
message3 = input('Input smth: ')
num3 = []

for i in range(len(message3)):
    if message3[i] in numbers:
        num3.append(message3[i])

print(num3)
