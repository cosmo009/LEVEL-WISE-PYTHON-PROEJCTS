"""
* This program is a temperatur converter using a menu system
* author gaurang mane
* date 25.04.2026
"""
choice = 0
while (True and choice!=3):
    print("\n---TEMPERATURE CONVERTER---")
    print("1. Fahrentheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

    success = False
    while not success:
        try:
            choice = int(input("\nEnter choice: "))
            success = True
        except ValueError:
            print("That's not a valid choice. Please try again.")

    if choice == 1:
        success = False
        while not success:
            try:
                fahrenheit = float(input("\nEnter fahrenheit temperature: "))
                success = True
            except ValueError:
                print("INVALID TEMPERATURE. Please try again.")

        celsius = (fahrenheit-32)*5/9
        print(f"\nFahrenheit : {fahrenheit}F\nCelsius :{celsius} ºC")

    elif choice == 2:
        success = False
        while not success:
            try:
                celsius = float(input("\nEnter celsius temperature: "))
                success = True
            except ValueError:
                print("INVALID TEMPERATURE. Please try again.")

        fahrenheit = celsius*9/5 + 32
        print(f"\nCelsius :{celsius}ºC\nFahrenheit : {fahrenheit} F")

    elif choice == 3:
        print("\nExiting")