from sistema.assessment import Assessment
from sistema.menu.menu_item import MenuItem

class Restaurant:

    restaurants = []

    def __init__(self, name, category):
 
        self._name = name.title()
        self._category = category
        self._active = False
        self._assessment = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name.ljust(20)} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'\n{"Restaurant".ljust(20)} | {"Category".ljust(20)} | {"Assessment".ljust(20)} | {"Status"}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(20)} | {restaurant._category.ljust(20)} | {str(restaurant.mean_assessment).ljust(20)} | {restaurant.active}')

    @property
    def active(self):
        return 'Active' if self._active else 'Disabled'
    
    def toggle_status(self):
        self._active = not self._active

    def to_receive_assessment(self, customer, notice):
        if 0 <= notice <= 5:
            assessment = Assessment(customer, notice)
            self._assessment.append(assessment)

    @property
    def mean_assessment(self):
        if not self._assessment:
            return 'No reviews'
        sum_of_the_scores = sum(assessment._notice for assessment in self._assessment)
        number_of_banknotes = len(self._assessment)
        mean = round(sum_of_the_scores / number_of_banknotes, 1)
        return mean
    
    def add_to_the_menu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def view_menu(self):
        print(f'\nRestaurant Menu {self._name}\n')
        for i,item in enumerate(self._menu, start=1):
            if hasattr(item, 'description'):
                message_dish = f'{i}. Name: {item._name} | Price: ${item._price} | Description: {item.description}'
                print(message_dish)
            else:
                message_drink = f'{i}. Name: {item._name} | Price: ${item._price} | Size: {item.size}'
                print(message_drink)