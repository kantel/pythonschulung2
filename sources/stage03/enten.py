suffix = "ack"
praefixe = "JKLMNOPQ"
for praefix in praefixe:
    if praefix == "O" or praefix == "Q":
        print(praefix + "u" + suffix)
    else:
        print(praefix + suffix)