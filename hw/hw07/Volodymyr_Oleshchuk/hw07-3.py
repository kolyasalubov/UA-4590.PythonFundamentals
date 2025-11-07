def count_characters(s):
    return {char: s.count(char) for char in set(s)}

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(count_characters(string))