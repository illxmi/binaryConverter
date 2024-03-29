from os import system

def bToD():
    bits = int(input("How many bits in your number? ")) # Recieve amount of bits
    # Set Arrays
    number = [0]*bits
    powers = [0]*bits
    counter = 1

    # Create Bits
    for i in range(bits):
        powers[i] = 2**(bits - counter)
        counter += 1

    # Displays bits 
    print(bits)
    print(powers)

    print("Please type your binary number one number at a time:") # Recieve Binary
    # Puts binary into an array
    for i in range(bits):
        number[i] = str(input())
    
    # Calculate and convert to decimal
    output = 0
    for i in range(bits):
        if number[i] == "1":
            output += powers[i]
        else:
            output += 0

    return output


def dToB():
    number = 0
    binary = [0]
    powers = [1]
    addedPower = 0
    number = int(input("Please type your decimal number to be converted:")) # Recieve Decimal Number

    while not powers[0] >= number: # So the highest power has to be >= the specified number
        addedPower = powers[0]*2 # The highest power is timesed by 2
        powers.insert(0, addedPower) # It is then inserted to the start of the array and will shift the rest of the powers along 1

    binary = [0]*len(powers) # Sets the required length

    # Converting to Binary
    for i in range(0, len(powers)):
        if powers[i] <= number:
            binary[i] = 1
            number = number - powers[i]
        else:
            binary[i] = 0
    if binary[0] == 0:
        output = binary[1:len(binary)]
    else:
        output = binary

    return output

def hToD():
    hexdecimal = ""
    hexcal = []
    decimal = 0
    
    hexdecimal = input("Enter the Hexidecimal to be converted here: ")
    hexcal = list(hexdecimal)
    hexbinary = []
    
    # Converting to Binary
    for i in range(0, len(hexcal)):
        if hexcal[i] == "1":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "2":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "3":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "4":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "5":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "6":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "7":
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "8":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "9":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "A" or hexcal[i] == "a":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "B" or hexcal[i] == "b":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "C" or hexcal[i] == "c":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "D" or hexcal[i] == "d":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
        if hexcal[i] == "E" or hexcal[i] == "E":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 0)
        if hexcal[i] == "F" or hexcal[i] == "f":
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)
            hexbinary.insert(len(hexbinary), 1)

    powers = [0]*len(hexbinary)
    counter = 1

    # Create Bits
    for i in range(0, len(hexbinary)):
        powers[i] = 2**(len(hexbinary) - counter)
        counter += 1

    # Converting to Binary
    for i in range(0, len(hexbinary)):
        if hexbinary[i] == 1:
            decimal = decimal + powers[i]
            
    return(decimal)

# Main Program
system('title Converter')
stop = ""
while not stop == "stop":
    setting = ""
    setting = input("Binary - Decimal (B) \nDecimal - Binary(D) \nHex - Decimal (H) \nPlease choose an option: ")
    setting = setting.upper() # in case u do lower case

    if setting == "B":
        output = bToD()
        print("")
        print(output)

    if setting == "H":
        output = hToD()
        print("")
        print(output)

    if setting == "D":
        output = dToB()
        print("")
        print(output)

    if setting == "DH":
        output = dtoH()
        print("")
        print(output)
    
    print("")
    stop = input("Press enter to continue or type 'stop' to exit the program: ")
    stop = stop.lower() # not case sensitive
    system('cls')
