from modelos.restaurants import Restaurant
from modelos.menu.drink import Drink
from modelos.menu.dish import Dish

restaurant_square = Restaurant('Square', 'Gourmet')
restaurant_square.to_recive_assessment('Thiago', 5)
drink_juice = Drink('Watermelon Juice', 5.0 , 'Big')
drink_juice.apply_discount()
dish_bread = Dish('Bread', 2.0 , 'Best bread in town')
dish_bread.apply_discount()
restaurant_square.add_to_the_menu(drink_juice)
restaurant_square.add_to_the_menu(dish_bread)
restaurant_square.toggle_status()

def main():
    restaurant_square.view_menu

if __name__ == '__main__':
    main()