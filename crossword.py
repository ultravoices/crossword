words_file = open('words.txt')

words_list = []

for line in words_file:
    word = line.strip()
    words_list.append(word)


def select_by_length(length, wordlist):
    selected_by_length_words = []
    for wordz in wordlist:
        if length == len(wordz):
            selected_by_length_words.append(wordz)
    return selected_by_length_words


def select_by_letter(letter, index, wordlist):
    selected_by_letter_words = []
    for item in wordlist:
        if letter in item[index]:
            selected_by_letter_words.append(item)
    return selected_by_letter_words


def get_length():
    while True:
        try:
            input_length = int(input("Enter the length of the word:"))
            if 20 >= input_length >= 2:
                print("Getting words of length", input_length)
                return input_length
            else:
                print("Please input a number between 2 and 20.")
        except ValueError:
            print("Sorry, please input a number between 2 and 20.")


def get_letters():
    pairs = []
    while True:
        try:
            input_letter = input("Enter the letter to search for, or 'done' to finish entering letters:")
            if input_letter == 'done':
                print('Searching for answers...')
                return pairs
            if (isinstance(input_letter, str)) and len(input_letter) == 1:
                input_position = int(input("Enter the position of the letter:"))
                input_position -= 1
                if 0 <= input_position <= 19:
                    result = (input_letter, input_position)
                    pairs.append(result)
                else:
                    print('something has gone wrong!')
                    pairs = []
        except ValueError:
            print('Please enter a number between 1 and 20')


def main():
    length_var = get_length()
    length_list = select_by_length(length_var, words_list)
    search_pairs = get_letters()
    counter = 0
    for i, j in search_pairs:
        if counter is 0:
            search_by_letter_list_1 = select_by_letter(i, j, length_list)
            set_a = set(search_by_letter_list_1)
            counter += 1
        if counter is not 0:
            search_by_letter_list_2 = select_by_letter(i, j, length_list)
            set_b = set(search_by_letter_list_2)
            set_a = set.intersection(set_a, set_b)
    results = sorted(list(set_a))
    print(results)

main()

