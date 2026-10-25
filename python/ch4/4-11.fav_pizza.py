pizzas = ["pepperoni", "hawaiian", "bbq chicken"]
friend_pizzas = pizzas[:]

pizzas.append("cheese")

friend_pizzas.append("veggie")

for pizza in pizzas:
    print(f"my favourite pizzas are: {pizza}")

for pizza in friend_pizzas:
    print(f"my friend's favourite pizzas are: {pizza}")