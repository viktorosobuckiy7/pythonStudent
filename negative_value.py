class NegativeValueError(Exception):

    def __init__(self, product_price, message="Значение стоимости товара не может быть отрицательным"):
        self.product_price = product_price
        self.message = message
        super().__init__(self.message)


product_price = int(input("Введите значение цены"))
if product_price < 0:
    raise NegativeValueError(product_price)
