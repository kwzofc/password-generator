import random
from characters import letters, numbers, symbols

print('Welcome to the Password Generator!')

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = ''
all_chars = [letters, numbers, symbols]
password_length = nr_letters + nr_symbols + nr_numbers

if __name__ == '__main__':
  for _ in range(password_length):
    chars_list = random.randint(0, len(all_chars)-1)
    password += all_chars[chars_list][random.randint(0, len(all_chars[chars_list])-1)]

    if all_chars[chars_list] == letters:
      nr_letters -= 1

      if nr_letters == 0:
        all_chars.pop(chars_list)
        continue

    if all_chars[chars_list] == numbers:
      nr_numbers -= 1
      
      if nr_numbers == 0:
        all_chars.pop(chars_list)
        continue

    if all_chars[chars_list] == symbols:
      nr_symbols -= 1
      
      if nr_symbols == 0:
        all_chars.pop(chars_list)
        continue

  print(f'Password is: {password}')
