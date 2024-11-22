# TODO  Напишите функцию count_letters
def count_letters(tekst):
    slovar_count_letters={}
    for simvol in tekst.lower():
        if simvol.isalpha():
            if simvol in slovar_count_letters:
                slovar_count_letters[simvol]+=1
            else:
                slovar_count_letters[simvol] = 1
    return slovar_count_letters








# TODO Напишите функцию calculate_frequency
def calculate_frequency(slovar_count_letters):
    new_slovar={}
    sum_bukv=sum(slovar_count_letters.values())
    for letter, count in slovar_count_letters.items():
        new_slovar[letter]=count/sum_bukv
    return new_slovar


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
slovar=calculate_frequency(count_letters(main_str))
for letter, frequency in slovar.items():
        print(f"{letter}: {frequency:.2f}")