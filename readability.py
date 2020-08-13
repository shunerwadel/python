# Program to determine grade level of the given text using the Coleman-Liau formula

from cs50 import get_string


def main():

    # Ask for text
    text = get_string("Text: ")

    # Declare variables
    letters = 0
    words = 0
    sentences = 0

    # Count spaces, sentence punctuation, and letters in text
    for char in text:
        if char in [' ']:
            words += 1
        elif char in ['.', '?', '!']:
            sentences += 1
        elif (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
            letters += 1

    # Account for last word in text
    words = words + 1

    # Calculate ave letters per 100 words
    L = (letters / words) * 100

    # Calculate ave senences per 100 words
    S = (sentences / words) * 100

    # Calculate grade level index
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print index
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


main()
