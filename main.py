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
    user_interest = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")
    user_interest = user_interest.lower()

    if user_interest == "eldrazi":
        details = lore.eldrazi
        titans = list(details.keys())
        key_string = ", ".join(titans)
        Second_interest = input("which Eldrazi titan do you wish to know about? " + key_string + "? ")
        
        lore_locater(details)
        

    if user_interest == "gatewatch":
        details = lore.gatewatch
        walkers = list(details.keys())
        key_string = ", ".join(walkers)
        Second_interest = input("which Gatewatch Planeswalker do you wish to know about? " + key_string+ "? ")
        
        lore_locater(details)
        

    if user_interest == "phyrexians":
        details = lore.phyrexians
        praetors = list(details.keys())
        key_string = ", ".join(praetors)
        Second_interest = input("which Phyrexian figure/praetor do you wish to know about? " + key_string + "? ")
        
        lore_locater(details)
    
    while x == True:
        cycler = input("would you like to know about a different group?(yes/no): ")
        if cycler == "yes":
           break
        elif cycler == "no":
            x = False
        elif cycler != "yes" or "no":
            print("error please only answer yes or no")


































