# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    print("Program to process text")
    word_list = []

    new_word = input('Please enter some text: ')
    word_list.append(new_word)
    while new_word != '-1':
        new_word = input('Please enter some text (type -1 to exit) : ')
        if new_word == '-1':
            break
        word_list.append(new_word)

    print("===============Values Table===================")
    print('Word', 'Value', 'Running Total',  sep='\t')

    word_list_sum = 0
    for word in word_list:
        word_value = compute_value(word)
        word_list_sum += word_value
        print(f'{word}', f'{word_value}\t', f'{word_list_sum}', sep='\t')

    average_word_val = word_list_sum / len(word_list)
    average_in_decimal = "{:.2f}".format(average_word_val)

    print (f'Total value of words is: {word_list_sum}')
    print(f'Average value per words is: {average_in_decimal}')

    # confirm that the user wants to start again
    yes_list = ["yes", "y", "yeah"]
    restart = input("Do you want to start again?").lower()
    if restart in yes_list:
        main()
    else:
        exit()


def compute_value(word):
    word_sum = 0
    word_sum += check_vowel(word)
    word_sum += check_consonant(word)
    word_sum += check_numeric(word)
    return word_sum


def check_vowel(word):
    add_five = ['a', 'e', 'i', 'o', 'u']
    char_sum = 0
    for char in word.lower():
        if char in add_five:
            char_sum += 5
    return char_sum


def check_consonant(word):
    add_two = ['r', 's', 't', 'l']
    char_sum = 0
    for char in word.lower():
        if char in add_two:
            char_sum += 2
    return char_sum


def check_numeric(word):
    add_nine = ['3', '4', '5', '6', '7']
    char_sum = 0
    for char in word.lower():
        if char in add_nine:
            char_sum += 9
    return char_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
