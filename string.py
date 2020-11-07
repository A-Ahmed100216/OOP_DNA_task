# Create class
class DNA_Parse:
    # Initialise class
    def __init__(self):
        # Take user input for string and convert to upper case.
        self.s=input("Please enter your string: \n").upper()

    # Create letter function
    def letters(self):
        # For each letter in the string
        for let in self.s:
            # Return the count of A,C,G,T in a formatted string.
            return "{} {} {} {} ".format(self.s.count("A"),self.s.count("C"),self.s.count("G"),self.s.count("T"))
