def count_letters(string_input):
    counts = {}
    string_input = string_input.upper()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        num = string_input.count(letter)
        if num > 0:
            counts[letter] = num
    return counts

if __name__ == "__main__":
    print(count_letters("karaoke 233 fio2 qar93"))