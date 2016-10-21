words_file = open('words.txt')

words_list = []

for line in words_file:
    word = line.strip()
    words_list.append(word)

def select_by_length(length, words_list):
    selected_by_length_words = []
    for word in words_list:
        if length == len(word):
            selected_by_length_words.append(word)
    return selected_by_length_words

def select_by_letter(letter, index, words_list):
    selected_by_letter_words = []
    for word in words_list:
        try:
            if letter in word[index]:
                selected_by_letter_words.append(word)
        except IndexError:
            pass
    return selected_by_letter_words

def get_length():
    while True:
        try:
            input_length = int(input("Enter the length of the word:"))
            if input_length <= 20 and input_length >= 2:
                print("Getting words of length", input_length)
                return input_length
            else:
                print("Please input a number between 2 and 20.")
        except ValueError:
            print("Sorry, please input a number between 2 and 20.")
        
def get_lengths():
    pairs = []
    while True:
        try:
            input_letter = input("Enter the letter to search for, or 'done' to finish entering letters:")
            if input_letter == 'done':
                print('Searching for answers...')
                return pairs
            if (isinstance(input_letter, string.ascii_lowercase)) and len(input_letter) == 1:
                input_position = int(input("Enter the position of the letter:"))
                input_position -= 1
                if input_position >= 0 and input_position <= 19:
                    result = (input_letter, input_position)
                    pairs.append(result)
                else:
                        print('something has gone wrong!')
                        pairs = []
            else:
                print('Please enter a single letter.')
        except ValueError:
            print('Please enter a number between 1 and 20')



##a_set = select_by_length(5, words_list)
##b_set = select_by_letter('x', 2, words_list)
##
##results = set.intersection(set(a_set), set(b_set))
##listed_results = sorted(list(results))
##
##print(listed_results)


