word = input("Hello. Enter the desired word: ").lower()
res = {}

def count_letters(word):
    for item in word:
        if item not in res:
            res[item] = 1
        else:
            res[item] += 1

count_letters(word)
print(res)