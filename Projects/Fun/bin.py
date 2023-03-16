# Returns the birthday in binary

class Birthday:
    def __init__(self) -> None:
        self.year = int(input('Set the year: '))
        self.month = int(input('Set the month: '))
        self.day = int(input('Set the day: '))
    
    def binrep(self): # binary representation of the numerical values
        return str(bin(self.year)[2:]) + ' - ' + str(bin(self.month)[2:]) + ' - ' + str(bin(self.day)[2:])


# instancias
person = Birthday().binrep()

def run():
    print(person)

if __name__ == "__main__":
    run()