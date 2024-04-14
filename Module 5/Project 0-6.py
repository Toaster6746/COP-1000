AllowedVehiclesList = []
with open('F:\School Scripts\Git\COP-1000\Module 6/vehicles.txt', 'r') as file:
    AllowedVehiclesList = [line.strip() for line in file]
def printF():
    print ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for i in AllowedVehiclesList:
        print (i, end=" \n")
    x_function()
def search():
    print ("Please Enter the full Vehicle name:")
    z = str(input())
    if z in AllowedVehiclesList:
        print(z + " is an authorized vehicle")
        x_function()
    else:
        print(z + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
        x_function()
def add():
    print ("Please Enter the full Vehicle name you would like to add:")
    addedVehicle = str(input())
    AllowedVehiclesList.append(addedVehicle)
    with open('F:\School Scripts\Git\COP-1000\Module 6/vehicles.txt', 'w') as file:
        for item in AllowedVehiclesList:
            file.write(item + '\n')
    print("You have added \"" + addedVehicle  + "\" as an authorized vehicle")
    x_function()
def delete():
    print ("Please Enter the full Vehicle name you would like to REMOVE:")
    removedVehicle = str(input())
    print("Are you sure you want to remove \"" + removedVehicle + "\" from the Authorized Vehicles List?")
    yesOrNo = str(input())
    if yesOrNo.lower() == str("yes"):
        AllowedVehiclesList.remove(removedVehicle)
        with open('F:\School Scripts\Git\COP-1000\Module 6/vehicles.txt', 'w') as file:
            for item in AllowedVehiclesList:
                file.write(item + '\n')
        print("You have REMOVED \"" + removedVehicle  + "\" as an authorized vehicle")
        x_function()
    else:
        x_function()
def x_function():
    x = ("********************************\nAutoCountry Vehicle Finder v1.0\n********************************\nPlease Enter the following number below from the following menu:\n \n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit\n********************************")
    print (x)
    y = int(input())
    if y == 1:
        printF()
    if y == 2:
        search()
    if y == 3 :
        add()
    if y == 4 :
        delete()
    else:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
x_function()
