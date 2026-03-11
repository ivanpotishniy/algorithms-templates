def list_superset(list_set_1, list_set_2):
    def is_subset(subset, superset):
        """Проверяет, является ли subset подмножеством superset
        (используя только списки)"""
        for item in subset:
            if item not in superset:
                return False
        return True

    # Проверяем, является ли list_set_1 супермножеством для list_set_2
    is_1_superset_of_2 = is_subset(list_set_2, list_set_1)
    # Проверяем, является ли list_set_2 супермножеством для list_set_1
    is_2_superset_of_1 = is_subset(list_set_1, list_set_2)

    # Определяем результат на основе проверок
    if is_1_superset_of_2 and is_2_superset_of_1:
        # Наборы равны — содержат одинаковые элементы (порядок не важен)
        return "Наборы равны."
    elif is_1_superset_of_2:
        # list_set_1 — супермножество для list_set_2
        return f"Набор {list_set_1} - супермножество."
    elif is_2_superset_of_1:
        # list_set_2 — супермножество для list_set_1
        return f"Набор {list_set_2} - супермножество."
    else:
        # Ни один список не является супермножеством для другого
        return "Супермножество не обнаружено."


# Примеры для проверки функции
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))  # Набор [1, 3, 5, 7] - супермножество.
print(list_superset(list_set_2, list_set_3))  # Набор [5, 3, 7, 1] - супермножество.
print(list_superset(list_set_1, list_set_3))  # Наборы равны.
print(list_superset(list_set_2, list_set_4))  # Супермножество не обнаружено.
