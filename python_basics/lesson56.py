
phrase = 'Olha só que, coisa interessante'
phrase_list = phrase.split()
print(phrase_list)

phrase_01 = 'Olha só que, coisa interessante'
phrase_list_01_init = phrase_01.split(',')
phrase_list_01 = []
print(phrase_list_01_init)


for i, phrase in enumerate(phrase_list_01_init):
    phrase_list_01.append(phrase_list_01_init[i].strip())


for i, phrase in enumerate(phrase_list_01):
    print(phrase_list_01[i].lstrip())


phrase_02 = 'Olha só que, coisa interessante'
phrase_list_02 = phrase_02.split(',')
print(phrase_list_02)


for i, phrase in enumerate(phrase_list_02):
    print(phrase_list_02[i].rstrip())


uni_phrases = '-'.join('abc')
print(uni_phrases)

uni_phrases_01 = ', '.join(phrase_list)
print(uni_phrases_01)