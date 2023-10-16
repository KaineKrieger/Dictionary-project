import lore 







User_interest  = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")


if User_interest == "Eldrazi":
    key_list = list(lore.Eldrazi.keys())
    key_list = ", ".join(key_list)
    Second_interest = input("which Eldrazi titan do you wish to know about? " + key_list + "? ")
    if Second_interest == "Emrakul":
        print(lore.Eldrazi["Emrakul"])

    if Second_interest == "Ulamog":
        print(lore.Eldrazi["Ulamog"])

    if Second_interest == "Kozilek":
        print(lore.Eldrazi["Kozilek"])


