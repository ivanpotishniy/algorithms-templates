def olympus_barometer(generation):
    # Базовые случаи: поколения 0 и 1 выполняют по 1 измерению в секунду
    if generation == 0 or generation == 1:
        return 1
    # Рекурсивный случай: количество измерений = сумма измерений двух предыдущих поколений
    else:
        return olympus_barometer(generation - 1) + olympus_barometer(generation - 2)


# Чтение ввода и вывод результата
if __name__ == '__main__':
    generation = int(input())
    print(olympus_barometer(generation))
