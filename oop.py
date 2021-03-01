class Product:
    def __init__ (self, name, price, stock=0, discount=0,max_discount=0):
        self.name = name.strip()
        if len(self.name)<2:
            raise ValueError('Название товара должно быть более 2 символов')
        self.price = abs(float(price)) 
        self.stock = abs(int(stock)) 
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount >99:
            raise ValueError('Cлишком большая скидка')
        if self.discount> self.max_discount:
            self.discount = self.max_discount
    def discounted(self):
        return self.price - self.price * self.discount/100
    def get_color(self):
        raise NotImplementedError
    def __repr__(self):
        return f'Наименование продукта:{self.name},цена{self.price},колличество{self.stock}'
    
class Phone(Product):
    def __init__ (self, name, price, color, stock=0, discount=0,max_discount=0):
        super().__init__(name, price, stock, discount,max_discount)
        self.color = color 
    def get_color(self):
        return f'Цвет корпуса: {self.color}'
    def __repr__(self):
        return f'Наименование телефона:{self.name},цена{self.price},колличество{self.stock}'
class Sofa(Product):
    def __init__ (self, name, price, color,texture, stock=0, discount=0,max_discount=0):
        super().__init__(name,price, stock, discount,max_discount)
        self.color = color 
        self.texture = texture
    def get_color(self):
        return f'Цвет обивки:{self.texture}'
    def __repr__(self):
        return f'Наименование дивана:{self.name},цена{self.price},колличество{self.stock}'





my_product = Product('Iphone',100,3,4,5)
my_producе2 = Phone('Samsung',20,'Желлтый')
my_product3 = Sofa('Диван',1000,'Белый','Замша')
print(my_producе2)


print(my_producе2.get_color())
print(my_product3)
print(my_product3.get_color())