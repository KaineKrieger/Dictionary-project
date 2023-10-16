import lore 


def lore_locater(key_list):
    for i in range(len(key_list)):
        if Second_interest == key_list[i]:

            print(lore.phyrexians[key_list[i]])






User_interest  = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")


if User_interest == "Eldrazi":
    key_list = list(lore.Eldrazi.keys())
    key_string = ", ".join(key_list)
    Second_interest = input("which Eldrazi titan do you wish to know about? " + key_string + "? ")
    if Second_interest == "Emrakul":
        print(lore.Eldrazi["Emrakul"])

    if Second_interest == "Ulamog":
        print(lore.Eldrazi["Ulamog"])

    if Second_interest == "Kozilek":
        print(lore.Eldrazi["Kozilek"])


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