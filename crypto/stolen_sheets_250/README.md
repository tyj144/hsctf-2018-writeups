# Stolen Sheets
**Crypto**, 250pts

I wrote a script to observe a pattern between the given plaintext words to encrypted words. We know from the sheet that "onetwothreefourfivesixseveneightnineten" will map to "qzcxwqxbpcctqoptsfcgsngcfczcskbxzszcxcz".

The script outputs the number of the plaintext letter to the number of the encrypted plaintext letter (e.g. “A” = 1):
```
5: 3
6: 20
7: 11
8: 2
9: 19
14: 26
15: 17
18: 16
19: 7
20: 24
21: 15
22: 6
23: 23
24: 14
```
From this, we can observe that the output of each consecutive number is 9 less than the previous mod 26. We can use the fact that 5 (the letter “e”) encrypts to 3 (the letter “c”) to form an equation that calculates the sequence of encrypted values.

We will define e to be the encrypted value and p to be the plain text value.
We know that the difference between each number is -9, thus the formula takes on the form:
e = (-9p + m) % 26
where m is some value smaller than 26 that adds onto the number to make it match the sequence.

We can plug in 5 and 3 to get:
```
3 = (-9 * 5 + m) % 26 
3 = -45 % 26 + m
3 = 7 + m
m = -4
```
Thus, we can calculate the sequence of encrypted values to be:
e = (-9p - 4) % 26
We can write a script to calculate the sequence of encrypted values and map them back to letters with this:
```
# key stores a map from the encrypted letter to the plain text letter
key = {}
for i in range(ord("a"), ord("z")):
	num = i - ord("a") + 1
	# the observed pattern
	encrypted = (-9 * num - 4) % 26
	# do this because mod 26 changes 26 to 0, when 26 should remain 26
	if (encrypted == 0):
		encrypted = 26

	# adds the encrypted letter and its corresponding normal letter to key
	key[chr(ord("a") + encrypted - 1)] = chr(ord("a") + num - 1)

flag_cipher = "mrkcdpmsuimzstqrlg"

flag = ""

for letter in flag_cipher:
	if letter in key:
		flag += key[letter]
	else:
		flag += "*"

print(flag)
```

**Flag**: algebraicmanifolds

I realized afterwards, but this was an Affine cipher, which you could decode easily at https://www.dcode.fr/affine-cipher by brute forcing. It’s actually the fifth option: “A=17,B=12	ALGEBRAICMANIFOLDS”