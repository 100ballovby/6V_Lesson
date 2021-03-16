contacts_book = {
    'mom': {
        'phone': [
            '+375291234567',
            '+375441234567'
        ],
        'email': 'mom@example.com',
        'birth_date': '28.01.1990',
    },
    'father': '+375331234567',
    'granny': '+375251234567',
}

# добавление в словарь новой пары
contacts_book['brother'] = {
    'phone': '+74955550100',
    'email': 'bro@ya.ru'
}
print(contacts_book)
# удаление пары
del contacts_book['father']
print(contacts_book)
# изменение значения ключа
contacts_book['granny'] = '+14956789000'
print(contacts_book)
