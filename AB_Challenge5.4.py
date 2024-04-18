# AB Challenge 5.4 
# Improve the Who's Your Daddy program by adding a choice that lets the user enter a name and get back a grandfather. Your program should still only use
# one dictionary of son-father pairs. Make sure to incude several generations in your dictionary so that a match can be found.

def daddy():
    fathers = {"Luke Skywalker":"Anakin Skywalker",
               "Emilio Estevez":"Martin Sheen",
               "Charlie Sheen":"Martin Sheen",
               "Jason Doyle":"Randy Doyle",
               "Justin Doyle":"Randy Doyle",
               "Randy Doyle":"Henry Doyle",
               "Nemo":"Marlin",
               "Ahmed":"Fadlan",
               "Fadlan":"Al-Abbas",
               "Al-Abbas":"Rasid"}
    run = True
    while run:

        print("\tWho's Your Daddy?")
        print("""
        1. Look up a Father
        2. Look up a Grand-Father
        3. Add a new Father/Son Combo
        4. Exit """)

        option = input("\nWhat would you like to do? ")
        
        if option == "1":
            # Check to see if there is a father/son record based on the user's entry.
            son = input("\nWho's father are you looking for? ")
            soncap = son.title()
            if soncap in fathers:
                print("I have the father of ", soncap, " listed as:", fathers.get(soncap))
                print("Is this informaiton correct?")
                update = input("Yes or No? ")
                if update.title() == "No":
                    dad = input("Who is the true father of " + str(soncap) + " ? ")
                    newfather = dad.title()
                    fathers[soncap] = newfather
                    print(fathers.get(soncap))
            # If the record doesn't exist give the option to add it.
            else:
                print("I don't have a father listed for ", soncap)
                print("\nWould you like to add them?")
                add = input("Yes or No? ")
                if add.title() == "Yes":
                    newson = soncap.title()
                    dad = input("Who is the father of " + str(newson) + "? ")
                    newfather = dad.title()
                    fathers[newson] = newfather
                    print("\nI now have the father of ", newson, " listed as ", newfather, ".")
                    input("Press the Enter key to continue.")

        if option == "2":
            son = input("\nWho's Grand-Father are you looking for? ")
            soncap = son.title()
            if soncap in fathers:
                father = fathers.get(soncap)
                if father in fathers:
                    grandfather = fathers.get(father)
                    print("\nMy records indicate that", soncap, "is the son of", father, "who is the son of", grandfather, ". ")
                else:
                    print("I cannot find a Grand-Father record for", soncap, ".")
            else:
                print("\nI have no records for that person. \n")
        
        if option == "3":
            son = input("\nWho is the son that you would like to add? ")
            newson = son.title()
            # Check to see if the son already has a father listed in the dictionary and if so give them the option to update the record.
            if newson in fathers:
                print("I currently have", newson, "'s father listed as", fathers.get(newson))
                print("Would you like to change this record?")
                update = input("Yes or No? ")
                if update.title() == "Yes":
                    truefather = input("Who is the true father of " + str(newson) + "? ")
                    newfather = truefather.title()
                    fathers[newson] = newfather
                    print("I have updated my records to show that", fathers.get(newson), "is the father of", newson, ".")
                    input("\nPress the Enter key to continue.")
            # If there isn't a current record, get the info to add the combo.
            else:
                dad = input("And who would you like to enter as the father of " + newson + " ? ")
                newfather = dad.title()
                fathers[newson] = newfather
                print("\nI now have the father of ", newson, " listed as ", newfather, ".")
                input("Press the Enter key to continue.")


        if option == "4":
            input("Thanks for Playing! Press the Enter key to exit.")
            run = False




if __name__ == "__main__":
    daddy()
