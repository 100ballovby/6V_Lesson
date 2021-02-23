'''Списки, циклы и условия'''
sentence = 'The quick brown fox jumped over the lazy dog'
# создать список, состоящий только из гласных букв этого предложения
vowels = [i for i in sentence if i in 'aeiou']

new_vowels = []
for i in sentence:
    if i in 'aeiou':
        new_vowels.append(i)
print(new_vowels)
