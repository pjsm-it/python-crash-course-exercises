from random import randint as r

STOP = 'no'
PLAYAGAIN = 'yes'


def guessing_game():
    my_number = r(1, 1000)
    guess = int(input(
        "I'm thinking of a number (1-1000)!\n"
        "Try to guess the number I'm thinking of: "
        ))
    while True:
        if guess < my_number:
            guess = int(input('Too low! Guess again: '))
        elif guess > my_number:
            guess = int(input('Too high! Guess again: '))
        else:
            print("That's it!")
            play_gain = input('Would you like to play again? (yes/no) ')
            if play_gain.lower() == STOP:
                print('Thanks for playing!')
                break
            if play_gain.lower() == PLAYAGAIN:
                guessing_game()


def main():
    guessing_game()


if __name__ == "__main__":
    main()
