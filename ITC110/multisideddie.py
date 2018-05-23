import random
from time import sleep

class MultiSidedDie:
    value = 1

    def __init__(self, sides=None):
        if sides is None:
            raise Exception('You must specify number of sides for die.')
        else:
            try:
                self.sides = int(sides)
            except Exception:
                raise Exception('You must enter a valid number of sides.')

    def roll(self):
        roll_value = random.randint(1, self.sides)
        self.setValue(roll_value)

    def setValue(self, value):
        try:
            value = int(value)
        except Exception:
            raise Exception('The die cannot be set to a non-integer value.')
        if value >= 1 and value <=self.sides:
            self.value = value
        else:
            raise Exception('The die can only be set from 1 to', self.sides)

    def getValue(self):
        return self.value

if __name__ == '__main__':
    main()
    print('Red vs. Blue')

    print('Highest Number')

    redDie = MultiSidedDie(6)
    blueDie = MultiSidedDie(6)

    print('Red die rolling....')
    sleep(2)
    redDie.roll()
    print('The value is:', redDie.getValue())

    print('Blue die rolling....')
    sleep(2)
    blueDie.roll()
    print('The value is:', blueDie.getValue())

    print('First to roll a double.')
    redDie2 = MultiSidedDie(6)
    blueDie2 = MultiSidedDie(6)
    while True:
        print('Red is rolling')
        redDie.roll()
        print(redDie.getValue(), '....')
        sleep(1)
        redDie2.roll()
        print(redDie2.getValue())

        if redDie.getValue() == redDie2.getValue():
            print('Red team wins!')
            break

        print('Blue is rolling')
        blueDie.roll()
        print(blueDie.getValue(), '....')
        sleep(1)
        blueDie2.roll()
        print(blueDie2.getValue())

        if blueDie.getValue() == blueDie2.getValue():
            print('Blue team wins!')
            break
