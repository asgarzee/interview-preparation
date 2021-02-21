'''
Guess a word 
'''


def play(word):
    word_dashed = '_'*len(word)
    print(word_dashed)

    guessedcharset = set()
    tries = 6
    guessed = False

    while not guessed and tries > 0:
        guess = input("Enter a character to guess... : ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessedcharset:
                print('You havee already guessed this letter. Try again')
            elif guess in word:
                print("Your guess is right!")
                guessedcharset.add(guess)
                # tries -=1
                word_list = list(word_dashed)
                indices = [i for i, value in enumerate(word) if guess == value]
                for i in indices:
                    word_list[i] = guess
                word_dashed = ''.join(word_list)
                print('word now:')
                print(word_dashed)
                if '_' not in word_dashed:
                    guessed = True
            else:
                guessedcharset.add(guess)
                tries -= 1
                print('Guess is worng. try again.')
                print(f'Tries left: {tries}')
        else:
            print('Invalid!!! Enter a valid alphabet.')

    if guessed:
        print(f"You guessed the word: {word}")
        print(f'Tries left: {tries}')

    if tries == 0:
        print("You ran out of tires!!!")


if __name__ == "__main__":
    play("zeeshan")
