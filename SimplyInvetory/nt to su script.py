import os

def replace():
    file = open("Website/new.html", "r")
    text = file.read()
    file.close
    newlist = text.split("nt")

    print(newlist[0])

    finallist = ""

    for i in range(len(newlist)):
        finallist = finallist + newlist[i] + "su"
        print(finallist)

    file = open("Website/new.html", "w")
    file.write(finallist)
    file.close

    return

replace()