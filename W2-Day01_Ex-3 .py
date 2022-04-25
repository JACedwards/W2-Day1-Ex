age = input("How old are you? ")

age = int(age)

if age < 18:
    print(f'The age of {str(age)} is classified as a "kid."')

elif age < 66:
    print(f'The age of {str(age)} is classified as an "adult."')
else:
    print(f'The age of {str(age)} is classified as an "old fart."')

