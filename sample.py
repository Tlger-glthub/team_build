import random

kana_list = [
        'あ', 'い', 'う', 'え', 'お',
        'か', 'き', 'く', 'け', 'こ',
        'さ', 'し', 'す', 'せ', 'そ',
        'た', 'ち', 'つ', 'て', 'と',
        'な', 'に', 'ぬ', 'ね', 'の',
        'は', 'ひ', 'ふ', 'へ', 'ほ',
        'ま', 'み', 'む', 'め', 'も',
        'や', 'ゆ', 'よ',
        'ら', 'り', 'る', 'れ', 'ろ',
        'わ', 'を', 'ん'
]


word_1 = random.choice(kana_list)
word_2 = random.choice(kana_list)
word_3 = random.choice(kana_list)
word_4 = random.choice(kana_list)
word_5 = random.choice(kana_list)


print(word_1 + ":")
print(word_2 + ":")
print(word_3 + ":")
print(word_4 + ":")
print(word_5 + ":")
