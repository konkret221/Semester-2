def is_palindrome(input_string):
    input_string = input_string.lower()
    input_string = ''.join(e for e in input_string if e.isalnum())
    
    if input_string == input_string[::-1]:
        return True
    else:
        return False

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("Данная строка является палиндромом.")
else:
    print("Данная строка не является палиндромом.")