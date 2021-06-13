print("Hi! This is a unit converter that converts kilometers into miles.")

while True:
    print("Please enter a number that you would like to convert!")

    km = input("Km: ")

    km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

    miles = km * 0.62

    print("{0} km is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break