from sistema.menu.menu_item import MenuItem

class Dessert(MenuItem):
    def __init__(self,name, price, type_, size, description):
        super().__init__(name,price)
        self.type_ = type_
        self.size = size
        self.description = description

        def __str__(self):
            return self._name

    def apply_discount(self):
        pass