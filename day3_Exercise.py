# Q1
def is_palindrome(str):
    # Determine if a given string str is a palindrome or not
    length = len(str)
    for i in range(length // 2):
        if str[i] != str[length - 1 - i]:
            return False
    return True


# print('Q1'.center(100, '='))
# print(is_palindrome("radar"))
# print(is_palindrome("string"))


# Q2
def is_even(num):
    #     Determine if a number is even or not
    if num % 2 == 0:
        return True
    else:
        return False

#
# print('Q2'.center(100, '='))
# print(is_even(2))
# print(is_even(5))
# print(is_even(19))


# Q3
def reverse_string(str):
    s = ""
    for x in reversed(str):
        s += x
    return s

#
# print("Q3".center(100, "="))
# print(reverse_string("Vanier"))


# Q4
def num_of_occurences(c, str):
    num = 0
    for x in str:
        if x.lower() == c.lower():
            num += 1
    return num


# print("Q4".center(100, '='))
# print(num_of_occurences('S', 'String s characters'))



def main():
    while True:
        print('\nSelect one option from the menu shown below please: ')
        print(
            "1 - Palindrome check\n2 - Even or Odd check\n3 - reverse a string\n4 - Number of Occurrences check\n5 - "
            "Exit")
        num = input("Select by enter corresponding number please: ")
        if num == '1':
            str_check = input("Enter the string you want check please: ")
            print(str_check, " is a palindrome" if is_palindrome(str_check) else " is NOT a palindrome!")
        if num == '2':
            while True:
                number = input("Enter the number you want to check please: ")
                try:
                    n = float(number)
                    break
                except ValueError:
                    print("Input Error: Enter digits only please!")
            print(number, " is an even number" if is_even(n) else " is an Odd number!")
        if num == '3':
            str_reverse = input("Enter the string you want to reverse please: ")
            print("Revers of ", str_reverse, "is ", reverse_string(str_reverse))
        if num == '4':
            char_to_check = input("Enter the character you want check please: ")
            str_to_check = input("Now enter the string please: ")
            print(f"{char_to_check} occurs {num_of_occurences(char_to_check, str_to_check)} times in {str_to_check}")
        if num == '5':
            break;


main()
