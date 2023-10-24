import lore 


def lore_locater(key_list):

    for i in range(len(key_list)):
        if Second_interest == key_list[i]:

            print(lore.Second_interest[key_list[i]])
            Answer = input("Would you like to know more?(yes/no)")

            print(lore.key_list[i])


def lore_locater_extended():
    if Second_interest == "Emrakul":
        print(lore.Emrakul)

    if Second_interest == "Kozilek":
        print(lore.Kozilek)

    if Second_interest == "Ulamog":
        print(lore.Ulamog)

    if Second_interest == "Elesh_Norn":
        print(lore.Elesh_Norn)

    if Second_interest == "Urabrask":
        print(lore.Urabrask)

    if Second_interest == "Vorinclex":
        print(lore.Vorinclex)

    if Second_interest == "Sheoldred":
        print(lore.Sheoldred)
    
    if Second_interest == "Jin_Gitaxis":
        print(lore.Jin_Gitaxis)

    if Second_interest == "Gix":
        print(lore.Gix)

    if Second_interest == "Gideon":
        print(lore.Gideon)

    if Second_interest == "Chandra":
        print(lore.Chandra)

    if Second_interest == "Nissa":
        print(lore.Nissa)

    if Second_interest == "Jace":
        print(lore.Jace)

    if Second_interest == "Liliana":
        print(lore.Liliana)

    else:
        print("error occured, please restart")


x = True

while x == True:
    # User_interest  = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")
    User_interest = "Eldrazi"

    if User_interest == "Eldrazi":
        details = lore.Eldrazi
        titans = list(details.keys())
        key_string = ", ".join(titans)
        # Second_interest = input("which Eldrazi titan do you wish to know about? " + key_string + "? ")
        Second_interest= "Emrakul"
        for titan in titans:
            if Second_interest == titan:
                card = details.get(Second_interest).get("card")
                
                answer = input("Would you like to know more?(yes/no)")

                if answer == "yes":
                    lore_locater_extended()
    



    if User_interest == "Gatewatch":
        key_list = list(lore.Gatewatch.keys())
        key_string = ", ".join(key_list)
        Second_interest = input("which Gatewatch Planeswalker do you wish to know about? " + key_string+ "? ")
        
        for i in range(len(key_list)):
            if Second_interest == key_list[i]:
                print(lore.Gatewatch[key_list[i]])





    if User_interest == "Phyrexians":
        key_list = list(lore.Phyrexians.keys())
        key_string = ", ".join(key_list)
        Second_interest = input("which Phyrexian Praetor do you wish to know about? " + key_string + "? ")
        for i in range(len(key_list)):
            if Second_interest == key_list[i]:
                print(lore.Phyrexians[key_list])
                Answer = input("Would you like to know more?(yes/no)")

                print(lore(Second_interest))
    
    while x == True:
        cycler = input("would you like to know about a different group?(yes/no): ")
        if cycler == "yes":
           break
        elif cycler == "no":
            x = False
        else:
            print("error please only answer yes or no")


































