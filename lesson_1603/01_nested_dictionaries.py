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
# достать второй номер телефона мамы
print(contacts_book['mom']['phone'][1])

for key, value in contacts_book['mom'].items():
    print(key)
    print(value)