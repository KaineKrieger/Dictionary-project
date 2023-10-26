import lore 


def lore_locater(details):
    persons = list(details.keys())
    for person in persons:
        if Second_interest == person:
            print(details.get(Second_interest).get("card"))
            answer = input("Would you like to know more?(yes/no): ")
            if answer == "yes":
                print(details.get(Second_interest).get("lore"))


x = True

while x == True:
    User_interest  = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")
    
    if User_interest == "Eldrazi":
        details = lore.Eldrazi
        titans = list(details.keys())
        key_string = ", ".join(titans)
        Second_interest = input("which Eldrazi titan do you wish to know about? " + key_string + "? ")
        
        lore_locater(details)
        

    if User_interest == "Gatewatch":
        details = lore.Gatewatch
        walkers = list(details.keys())
        key_string = ", ".join(walkers)
        Second_interest = input("which Gatewatch Planeswalker do you wish to know about? " + key_string+ "? ")
        
        lore_locater(details)
        

    if User_interest == "Phyrexians":
        details = lore.Phyrexians
        praetors = list(details.keys())
        key_string = ", ".join(key_list)
        Second_interest = input("which Phyrexian Praetor do you wish to know about? " + key_string + "? ")
        
        lore_locater(details)
    
    while x == True:
        cycler = input("would you like to know about a different group?(yes/no): ")
        if cycler == "yes":
           break
        elif cycler == "no":
            x = False
        elif cycler != "yes" or "no":
            print("error please only answer yes or no")


































