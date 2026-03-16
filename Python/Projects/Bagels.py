import random
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

N_NUMBER = 3
G10_GUESSES = 10


def generate():
    numbers = [str(x) for x in range(10)]
    random.shuffle(numbers)
    number = "".join(numbers[:N_NUMBER])
    return number


NUMBER = generate()
attemps = 1


def compare():
    global unumber, NUMBER
    if len(unumber) == len(NUMBER):
        for i in range(N_NUMBER):
            if unumber[i] >= "0" and unumber[i] <= "9":
                if unumber[i] == NUMBER[i]:
                    print("Fermi", end=" ")
                elif unumber[i] in NUMBER and unumber[i] != NUMBER[i]:
                    print("Pico", end=" ")
                else:
                    print("Bagels", end=" ")
            else:
                raise Exception("Only 3 digit numbers can be acepted.")
    else:
        raise Exception(f"You need to have a 3 digit number, you have {len(unumber)}")


print(
    """I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico        One digit is correct but in the wrong position.
Fermi       One digit is correct and in the right position.
Bagels      No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
Type q to quit."""
)
while True:
    print(f"Attemp #{attemps}:")
    try:
        unumber = input("@ ")
        if unumber == NUMBER:
            print("You win, do want to play again? Y/N")
            yes_no = input("@ ")
            if yes_no == "Y":
                attemps = 1
                continue
            elif yes_no == "N":
                print("Thanks for playing")
                break
        elif unumber == "q":
            print("Thanks for playing")
            break
        compare()
        attemps += 1
    except IndexError:
        print("Only 3 digits numbers")
    except KeyboardInterrupt:
        break
    except Exception as err:
        print(err)
    if attemps > G10_GUESSES:
        print(f"\nYou loss, the number is {NUMBER}")
        break
    print()
