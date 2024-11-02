# TODO  Напишите функцию count_letters

def count_letters(text):
    new_text = text.lower()
    text_dict = {}
    DEFAULT = 0
    for simbol in new_text:
        if simbol.isalpha():
            text_dict[simbol] = text_dict.get(simbol, DEFAULT) + 1
    return text_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(text_dict):
    frequency_dict = {}
    summ_ = sum(text_dict.values())
    for letter, count_ in text_dict.items():
        frequency_dict[letter] = count_ / summ_
    return frequency_dict

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
result = count_letters(main_str)
result2 = calculate_frequency(result)

for letter, count in result2.items():
    print(f"{letter}: {count:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
