import abc

class Pizza (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass

#Concrete Pizzas

class Small(Pizza):
    __pizza_price = 10

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Small:"

class Medium(Pizza):
    __pizza_price = 15

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Medium:"

class Large(Pizza):
    __pizza_price = 20

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Large:"

class PizzaDecorator(Pizza):   #aggregation

    def __init__(self, pizza):
        self.pizza = pizza   #object recursion

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()

class Tomato(PizzaDecorator):

    def __init__(self, pizza):
        super(Tomato, self).__init__(pizza)
        self.__tomato_price = 5.0

    @property
    def price(self):
        return self.__tomato_price

    def get_price(self):
        return super(Tomato, self).get_price() + self.__tomato_price

    def get_status(self):
        return super(Tomato, self).get_status() + " Tomato"

class Mushroom(PizzaDecorator):

    def __init__(self, pizza):
        super(Mushroom, self).__init__(pizza)
        self.__mushroom_price = 4.0

    @property
    def price(self):
        return self.__mushroom_price

    def get_price(self):
        return super(Mushroom, self).get_price() + self.__mushroom_price

    def get_status(self):
        return super(Mushroom, self).get_status() + " Mushroom"

class Black_olive(PizzaDecorator):

    def __init__(self, pizza):
        super(Black_olive, self).__init__(pizza)
        self.__black_olive_price = 4.0

    @property
    def price(self):
        return self.__black_olive_price

    def get_price(self):
        return super(Black_olive, self).get_price() + self.__black_olive_price

    def get_status(self):
        return super(Black_olive, self).get_status() + " Black olive"


class Pepper(PizzaDecorator):

    def __init__(self, pizza):
        super(Pepper, self).__init__(pizza)
        self.__pepper_price = 5.0

    @property
    def price(self):
        return self.__pepper_price

    def get_price(self):
        return super(Pepper, self).get_price() + self.__pepper_price

    def get_status(self):
        return super(Pepper, self).get_status() + " Pepper"


class Pepperoni(PizzaDecorator):

    def __init__(self, pizza):
        super(Pepperoni, self).__init__(pizza)
        self.__pepperoni_price = 7.5

    @property
    def price(self):
        return self.__pepperoni_price

    def get_price(self):
        return super(Pepperoni, self).get_price() + self.__pepperoni_price

    def get_status(self):
        return super(Pepperoni, self).get_status() + " Pepperoni"


class Chicken(PizzaDecorator):

    def __init__(self, pizza):
        super(Chicken, self).__init__(pizza)
        self.__chicken_price = 8.0

    @property
    def price(self):
        return self.__chicken_price

    def get_price(self):
        return super(Chicken, self).get_price() + self.__chicken_price

    def get_status(self):
        return super(Chicken, self).get_status() + " Chicken"


class Tuna(PizzaDecorator):

    def __init__(self, pizza):
        super(Tuna, self).__init__(pizza)
        self.__tuna_price = 9.0

    @property
    def price(self):
        return self.__tuna_price

    def get_price(self):
        return super(Tuna, self).get_price() + self.__tuna_price

    def get_status(self):
        return super(Tuna, self).get_status() + " Tuna"


class Spinach(PizzaDecorator):

    def __init__(self, pizza):
        super(Spinach, self).__init__(pizza)
        self.__spinach_price = 3.0

    @property
    def price(self):
        return self.__spinach_price

    def get_price(self):
        return super(Spinach, self).get_price() + self.__spinach_price

    def get_status(self):
        return super(Spinach, self).get_status() + " Spinach"

class PizzaBuilder:

    def __init__(self, pizza_type):
        self.pizza_type = pizza_type
        self.pizza = eval(pizza_type)()
        self.extension_list = []

    def add_extension(self, extension):
        self.pizza = eval(extension)(self.pizza)
        self.extension_list.append(extension)

    def remove_extension(self, extension):
        if extension in self.extension_list:
            self.extension_list.remove(extension)

        temp = eval(self.pizza_type)()
        for ex in self.extension_list:
            temp = eval(ex)(temp)

        self.pizza = temp

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()
