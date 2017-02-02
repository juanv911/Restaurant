from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurant.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(user_id=1, name="Burger King", picture="/static/burgerKing.jpg")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree",picture="/static/lamb_curry.jpg", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree",picture="/static/chicken_marsala.jpg", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer",picture="/static/potstickers.jpg", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", picture="/static/nigiri.jpg", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree",picture="/static/veggie.jpg", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for KOI - Sushi & Hibachi
restaurant1 = Restaurant(user_id=1, name="KOI - Sushi & Hibachi'",picture="/static/KOI.jpg")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Panda Express
restaurant1 = Restaurant(user_id=1, name="Panda Express", picture="/static/pe.png")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()




print "added menu items!"
