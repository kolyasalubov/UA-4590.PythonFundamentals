### --- Task 3 ---
"""
Write a function that calculates the number of characters included in a given string.
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}
"""
word = str(input("Enter the word: ")).lower()

def calc_unique_letters(word):

    letters = []
    num_letters = []

    for ch in word.lower():
        if ch not in letters and ch.isalpha():
            letters.append(ch)
            num_letters.append(word.count(ch))

    result = dict(zip(letters, num_letters))
    return result

print(calc_unique_letters(word))
