import random

words = ["python", "java", "javascript", "cplusplus"]

secret_word = random.choice(words)

guessed_letters = []

lives = 6

print("=== TECH HANGMAN GAME ===")
print("Hint: Guess the programming language")

while lives > 0:

    hidden_word = ""

    for character in secret_word:

        if character in guessed_letters:
            hidden_word += character + " "

        else:
            hidden_word += "_ "

    print("\nWord:", hidden_word)
    print("Used Letters:", guessed_letters)

    if "_" not in hidden_word:
        print(f"\nAwesome! You guessed the language: {secret_word}")
        break

    user_guess = input("Guess a letter: ").lower()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if user_guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    if user_guess in secret_word:
        guessed_letters.append(user_guess)
        print("Nice! Correct letter.")

    else:
        lives -= 1
        print("Incorrect guess.")
        print("Remaining Lives:", lives)

if lives == 0:
    print(f"\nGame Over! The correct language was: {secret_word}")