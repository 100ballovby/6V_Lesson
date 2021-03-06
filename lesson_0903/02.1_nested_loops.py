'''Вложенные циклы - это когда один цикл вкладывается внутрь другого.
Соответственно верхний цикл повторяет внутренний цикл N раз.
'''

numStars = int(input('Сколько звезд нужно? '))
numLines = int(input('Сколько линий нужно? '))
numBlocks = int(input('Сколько блоков нужно? '))

for block in range(1, numBlocks + 1):  # этот цикл генерирует блоки
    for line in range(1, numLines + 1):  # этот цикл генериует линии
        for star in range(1, numStars + 1):  # этот цикл генерирует звезды
            print('⭐️', end=' ')
        print()
    print()

'''
В данном случае, у вас сначала создается блок из звезд,
затем "рисуется" линия, в линии появляются звездочки.

Так происходит столько раз, сколько повторений есть у цикла 
для генерации блоков.
'''