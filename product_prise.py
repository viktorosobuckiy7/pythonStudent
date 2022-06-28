try:
    product_prise = int(input('Введите значение цены'))
    assert product_prise > 0
except AssertionError:
    print("Значение цены должно быть положительным числом")
except ValueError:
    print("Значением цены должно быть числом")