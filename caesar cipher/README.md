Caesar cipher is one of the classical ciphering schemes. It is done by taking each character and adding a shift using a key. For example, if the key was 1, 'A' becomes 'B'. You can read up more about [Caesar cipher here](https://en.wikipedia.org/wiki/Caesar_cipher)

I will show step by step how I created my own decrypter for this caesar cipher.

Import string module to make life easier to access alphabets, both uppercase and lowercase.

```py
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
```

Now, that we have access to uppercase and lowercase characters, let's create a function that accepts ciphered string, and a shift key.

```py
def caesar(res, key):
    enc = ''
```

We need to be able to catch spaces and non-alphabetical characters first.

```py
def caesar(res, key):
    enc = ''
    for char in res:
        if char.isspace():
            enc += ' '
        elif not char.isalpha():
            enc += char
```

So now that we will only be dealing with alphabets, we can shift each character by the key. Using the ord() function, we can minus of the offset of ord('A'), add the shift key, and modulus by 26 in case it becomes larger than 26, and access the correct unciphered char.

```py
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
```

And there we have a function that caesar (de)ciphers a string. What if we do not know the key? Let's create a simple function that brute forces each key.

```py
def crackcaesar(res):
    for i in range(26):
        print(f'Key {i} : {caesar(res,i)}')
```

Ok, now let's create a while loop and a input prompt to clean things up.

```py
while True:
    cipher = input("What do you want to crack : ")
    key = input("Enter key (enter 'idk' if you do not know the key):")
    if key == 'idk':
        crackcaesar(cipher)
    else:
        print(caesar(cipher,int(key)%26))
```

Lets test this out!

```
What do you want to crack : Caesar cipher is very cool!
Enter key (enter 'idk' if you do not know the key):12
Omqemd oubtqd ue hqdk oaax!
What do you want to crack : Omqemd oubtqd ue hqdk oaax!
Enter key (enter 'idk' if you do not know the key):idk
Key 0 : Omqemd oubtqd ue hqdk oaax!
Key 1 : Pnrfne pvcure vf irel pbby!
Key 2 : Qosgof qwdvsf wg jsfm qccz!
Key 3 : Rpthpg rxewtg xh ktgn rdda!
Key 4 : Squiqh syfxuh yi luho seeb!
Key 5 : Trvjri tzgyvi zj mvip tffc!
Key 6 : Uswksj uahzwj ak nwjq uggd!
Key 7 : Vtxltk vbiaxk bl oxkr vhhe!
Key 8 : Wuymul wcjbyl cm pyls wiif!
Key 9 : Xvznvm xdkczm dn qzmt xjjg!
Key 10 : Ywaown yeldan eo ranu ykkh!
Key 11 : Zxbpxo zfmebo fp sbov zlli!
Key 12 : Aycqyp agnfcp gq tcpw ammj!
Key 13 : Bzdrzq bhogdq hr udqx bnnk!
Key 14 : Caesar cipher is very cool!
Key 15 : Dbftbs djqifs jt wfsz dppm!
Key 16 : Ecguct ekrjgt ku xgta eqqn!
Key 17 : Fdhvdu flskhu lv yhub frro!
Key 18 : Geiwev gmtliv mw zivc gssp!
Key 19 : Hfjxfw hnumjw nx ajwd httq!
Key 20 : Igkygx iovnkx oy bkxe iuur!
Key 21 : Jhlzhy jpwoly pz clyf jvvs!
Key 22 : Kimaiz kqxpmz qa dmzg kwwt!
Key 23 : Ljnbja lryqna rb enah lxxu!
Key 24 : Mkockb mszrob sc fobi myyv!
Key 25 : Nlpdlc ntaspc td gpcj nzzw!
```

This works wonderfully. The given key was 12. But the cracked key was 14, this is because 26-12=14. The alphabet loops with the modulus function.

The full [code](https://github.com/Coder-Here/cracking-ciphers/blob/main/caesar%20cipher/caesar.py):

````py

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
```
