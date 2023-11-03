import random
import datagen as gen

def get_start():
    word_list = gen.get_words()
    record = 0

    while True:
        word = word_list.pop(random.randrange(len(word_list)))
        print("■" * len(word))

        v = input("Угадал?\n1. Да\n2. Нет\n3.Конец игры ")

        if v == "1":
            record += 1
        elif v == "2":
            print("Попробуйте ещё раз. -1 жизнь...")
        elif v == "3":
            print("Конец игры!")
            break
        else:
            print("Введеное значение некорректно!")

        if not(word_list):
            break
    if record == gen.get_records(record):
        print("\n\nПоздравляем! Вы установили новый рекорд!")
    print(f"\n\nВы набрали: {record} очков.\nРекорд: {gen.get_records(record)}")

if __name__ == "__main__":
    get_start()

