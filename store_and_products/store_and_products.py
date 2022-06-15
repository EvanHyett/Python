from classes.store import Store
from classes.products import Product

safeway = Store("Safeway")

redbull = Product("Red Bull", 3, "Drink")
reeses = Product("Reeses", 32, "Candy")
apple = Product("Apple", 1, "Fruit")

# safeway.add_product(redbull).add_product(reeses).add_product(apple).set_clearance("fruit", 0.1).print_info()

apple.update_price(.02, 1)

apple.print_info()