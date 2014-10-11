from random import choice

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

stock = {
    "glug of rum":10, "slug of whisky":10, "splash of gin":10, 
"olive on a stick":10, "salt-dusted rim":10, "rasher of bacon":10, 
"shake of bitters":10, "splash of tonic":10, "twist of lemon peel":10, 
"sugar cube":10, "spoonful of honey":10, "spash of cola":10, 
"slice of orange":10, "dash of cassis":10, "cherry on top":10
}

nouns = ["Chinchilla","Sea-Dog","Animated","Happiness","Octolana","Bear","Dangerzone","Cyril"]
adjectives = ["Fluffy","Salty","Tyrion","Furry","Turnt","Mustached"]

customers = {}
# ---------------------------------------------------------------------------- #
# Procedure to ask a customer what his or her preference is regarding ingredients
# ---------------------------------------------------------------------------- #
# Input: Questions dictionary
# Output: List containing customer's preferences (True = Yes, I want that or False = No)

def drink():
    """I give you the best drink to try based on your tasting preference""" 
    taste = {}
    for key in questions:
        print questions[key]
        # Check customer's answer when a question is asked
        if raw_input() in ["y","yes"]:
            taste[key] = True
        else:
            taste[key] = False
    return taste

# ---------------------------------------------------------------------------- #
# Procedure to chose ingredientes based on customer's preferences.
# ---------------------------------------------------------------------------- #
# Input: List of tastes from customer and a dictionary containing stocks of different ingredients
# Output: Return a list containing only ingredients from the categories marked as True.

def make_drink(taste,stock):
    drink = []
    # Iterate through taste list
    for ingredient in taste:
        if taste[ingredient] == True:
                drink.append(choice(ingredients[ingredient]))
    return drink

# ---------------------------------------------------------------------------- #
# Procedure to check whether a certain ingredient is available
# ---------------------------------------------------------------------------- #
# Input: A list containing the desired ingredients
# Output: A True/False list with answer about stock (True = available or False = out of stock.

def check_stock(drink):
    available = {}
    for ingredient in drink:
        if stock[ingredient] > 0:
            stock[ingredient] =- 1
            available[ingredient] = True
        else:
            stock[ingredient]
            available[ingredient] = False
    return available

# ---------------------------------------------------------------------------- #
# MAIN BODY
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    customer_name = ""
    while True:
        drinking = ""
        if not customer_name: 
            customer_name = raw_input("What's your name? ").title()
        if customer_name in customers:
            drinking = choice(customers[customer_name].keys())
            customer_answer = raw_input("Do you want a {}? ".format(drinking))
            if customer_answer in ["y","yes"]:
                print("Here is your drink!")
            else:
                print("Ok! Let's give you something new")
                drinking = ""
        else:
            customers[customer_name] = {}
            print("Alright {}!".format(customer_name))
            print("Let\'s prepare you something special!")
        
        if not drinking:
            drinking = make_drink(drink(),stock)
        
            drink_name = "{} {}".format(choice(adjectives) , choice(nouns))
        
            if drinking == 0:
                print("Sorry pal, I cannot offer you anything")
                break
            elif len(drinking) < 2:
                print "Here is the {}. It is me with made with {}".format(drink_name,drinking[0])
            else:
                print "Here is the {}. It is me with {} and {}".format(drink_name,", ".join(drinking[:-1])," ".join(drinking[-1:]))
            customers[customer_name][drink_name] = drinking
            print customers
        print("Do you want another drink?")
        customer_answer = raw_input("> ")
        if customer_answer in ["y","yes"]:
            continue
        else:
            print("Are you sure you don't want anything else?")
            customer_answer = raw_input("> ")
            print "Alright!",
            if customer_answer in ["y","yes"]:
                print("Thanks for coming! Cheers!")
                break
            else:
                print("Let's give you something new!\n")
            
      