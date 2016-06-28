import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjective = ["Mild", "Salty", "Sweet", "Spicy", "Tangy", "Strong", "Fruity", "Tropical", "Fresh", "Fizzy", "Frozen"]
noun = ["Kitten", "Bunny", "Dog", "Coconut", "Apple", "Pear", "Grapefruit", "Banana", "Orange", "Snake", "Lizard"]

def style_of_drink():
    preferences = {
        "strong" : False,
        "salty" : False,
        "bitter" : False,
        "sweet" : False,
        "fruity" : False,
    }
    
    strong = input(questions["strong"])
    if strong == "y" or strong =="yes":
        preferences["strong"] = True
    
    salty = input(questions["salty"])
    if salty == "y" or salty == "yes":
        preferences["salty"] = True
        
    bitter = input(questions["bitter"])
    if bitter == "y" or bitter == "yes":
        preferences["bitter"] = True
        
    sweet = input(questions["sweet"])
    if sweet == "y" or sweet == "yes":
        preferences["sweet"] = True
        
    fruity = input(questions["fruity"])
    if fruity == "y" or fruity == "yes":
        preferences["fruity"] = True
        
    return preferences
    
def construct_drink(preferences):
    drink = []
    if preferences["strong"] == True:
        drink.append(random.choice(ingredients["strong"]))
    if preferences["salty"] == True:
        drink.append(random.choice(ingredients["salty"]))
    if preferences["bitter"] == True:
        drink.append(random.choice(ingredients["bitter"]))
    if preferences["sweet"] == True:
        drink.append(random.choice(ingredients["sweet"]))
    if preferences["fruity"] == True:
        drink.append(random.choice(ingredients["fruity"]))
        
    return drink
    
def drink_name():
    name = random.choice(adjective) + " " + random.choice(noun)
    return name
        
        
if __name__ == '__main__':
    more = True
    
    while more == True:
        preferences = style_of_drink()
        drink = construct_drink(preferences)
    
        print ("One {} coming right up! The recipe is: ".format(drink_name()))
    
        for ingredient in drink:
            print("A {}".format(ingredient))
        
        answer = input("\nDo you want another drink? ")
        if answer != "y" and answer != "yes":
            more = False
        