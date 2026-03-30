from collections import Counter

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def get_money(cost):
    quaters = (int(input("how many quaters? "))*25)/100
    dimes = (int(input("how many dimes? "))*10)/100
    nickels = (int(input("how many nickels? "))*5)/100
    pennies = int(input("how many pennies? "))/100
    total = quaters + dimes + nickels + pennies
    print(total)
    print(cost)
    if total < cost:
        return False,None
    elif total > cost:
        change = total - cost
        return True, change
    else: return True,None

def make_coffee(coffee, ingredients):
    money, change = get_money(ingredients["cost"])
    if money and change != None:
        print(f"Here is ${change} in change.")
        print(f"here is your {coffee} enjoy!.")
    elif money :
        print(f"Here is your {coffee} enjoy!.")
    else: print("Sorry,that's not enough money. Money refunded")

def resource_indicator(ingredients,resources):
    old_keys = set(ingredients.keys())
    og_resource = resources
    resources = dict(Counter(resources)-Counter(ingredients))
    new_keys = set(resources.keys())
    disappeared = old_keys - new_keys
    if disappeared:
        print(f"there is no enough {disappeared} resources to make a coffee.")
        return  False, og_resource
    else:
        return True, resources

def get_coffee(menu,resource):
    getting_coffee = False
    while not getting_coffee:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_type == "report":
            print(f"water : {resource["water"]} ml\ncoffee : {resource["coffee"]} g\nmilk : {resource["milk"]} ml\n")
        elif coffee_type == "off":
            getting_coffee = True
        else:
            resource_available, resource = resource_indicator(menu[coffee_type]["ingredients"],resource)
            if resource_available:
                coffee = make_coffee(coffee_type,menu[coffee_type])

get_coffee(MENU,resources)
