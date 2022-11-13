import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase


def caesar(res, key):
    enc = ''
    for char in res:
        if char.isspace():
            enc += ' '
        elif not char.isalpha():
            enc += char
        elif char.isupper():
            enc += upper[(ord(char)-ord('A')+key)%len(upper)]
        elif char.islower():
            enc += lower[(ord(char)-ord('a')+key)%len(lower)]

    return enc


def crackcaesar(res):
    for i in range(26):
        print(f'Key {i} : {caesar(res,i)}')


while True:
    cipher = input("What do you want to crack : ")
    key = input("Enter key (enter 'idk' if you do not know the key):")
    if key == 'idk':
        crackcaesar(cipher)
    else:
        print(caesar(cipher,int(key)%26))
