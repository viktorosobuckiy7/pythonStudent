class PriceTypeError(Exception):

    def __init__(self, product_price, message="Значение цены должно быть цифровым"):
        self.product_price = product_price
        self.message = message
        super().__init__(self.message)


product_price = int(input("Введите значение цены"))
try:
    print(product_price)
except ValueError:
    print('Это не число. Выходим.')
