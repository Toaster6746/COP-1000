AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]
def x_function():
    x = ("********************************\nAutoCountry Vehicle Finder v0.1\n********************************\nPlease Enter the following number below from the following menu:\n \n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit")
    print (x)
    y = int(input())
    if y == 1:
        print ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for i in AllowedVehiclesList:
            print (i, end=" \n")
        x_function()
    elif y == 2:
        print ("Please Enter the full Vehicle name:")
        z = str(input())
        if z in AllowedVehiclesList:
            print(z + " is an authorized vehicle")
            x_function()
        else:
            print(z + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
            x_function()
    elif y == 3 :
        print ("Please Enter the full Vehicle name you would like to add:")
        addedVehicle = str(input())
        AllowedVehiclesList.append(addedVehicle)
        print("You have added \"" + addedVehicle  + "\" as an authorized vehicle")
        x_function()
    elif y == 4 :
        print ("Please Enter the full Vehicle name you would like to REMOVE:")
        removedVehicle = str(input())
        print("Are you sure you want to remove \"" + removedVehicle + "\" from the Authorized Vehicles List?")
        yesOrNo = str(input())
        if yesOrNo.lower() == str("yes"):
            AllowedVehiclesList.remove(removedVehicle)
            print("You have REMOVED \"" + removedVehicle  + "\" as an authorized vehicle")
            x_function
        else:
            x_function
    else:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
x_function()
