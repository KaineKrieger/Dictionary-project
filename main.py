

Eldrazi = {"Emrakul" : "the aeons torn" ,
           "Kozliek" : "the great distortion",
            "Ulamog" : "the Ceaseless Hunger"}


User_interest  = input("which group do you wish to know about? Phyrexians Eldrazi or Gatewatch?: ")


if User_interest == "Eldrazi":
    key_list = list(Eldrazi.keys())
    key_list = ", ".join(key_list)
    Second_interest = input("which Eldrazi titan do you wish to know about? " + key_list + "? ")




