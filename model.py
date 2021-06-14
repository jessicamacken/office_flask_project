

def outcome(animal, vacation, food):
    score = 0
    if animal == "bear":
        score += 4
    elif animal == "kitten":
        score += 1
    elif animal == "dog":
        score += 2
    elif animal == "koi":
        score += 3
    else:
        print ("I don't understand the animal")

    if vacation == "jamaica":
        score += 3
    elif vacation == "farm_stay":
        score += 4
    elif vacation == "paris":
        score += 1
    elif vacation == "nba_finals":
        score += 2
    else: 
        print ("I don't understand the vacation")

    if food == "yogurt":
        score += 1
    elif food == "bloomin_onion":
        score += 3
    elif food == "beets":
        score += 4
    elif food == "italian_food":
        score += 2
    else:
        print ("I don't understand the food")

    print(score)

    character={}

    if score <= 4:
        character["name"] = "Pam"
        character["pic"] = "static/images/pam.jpg"
        print(character)
        return character
        # return print("You are Pam!")
    elif score <=7:
        character["name"] = "Jim"
        character["pic"] = "static/images/jim.jpg"
        print(character)
        return character
        # return print("You are Jim!")
    elif score <= 10:
        character["name"] = "Michael"
        character["pic"] = "static/images/michael.jpg"
        print(character)
        return character
        # return print("You are Michael!")
    elif score <=12:
        character["name"] = "Dwight"
        character["pic"] = "static/images/dwight.jpg"
        print(character)
        return character
        # return print("You are Dwight!")
    else:
        return print("You are Toby!")

    



