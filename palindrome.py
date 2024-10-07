number = int(input("Enter a number: "))

num_str = str(number)

reversed_str = num_str[::-1]

if num_str == reversed_str:
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")