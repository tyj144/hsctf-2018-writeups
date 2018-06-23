plain  = "onetwothreefourfivesixseveneightnineten"
cipher = "qzcxwqxbpcctqoptsfcgsngcfczcskbxzszcxcz"
key = {}
pattern = {}

for i in range(0, len(plain)):
	key[cipher[i]] = plain[i]
	pattern[ord(plain[i]) - ord("a") + 1] = ord(cipher[i]) - ord("a") + 1

flag_cipher = "mrkcdpmsuimzstqrlg"

flag = ""

for letter in flag_cipher:
	if letter in key:
		flag += key[letter]
	else:
		flag += "*"

print("From the key, we know part of the flag is: " + flag)
print("-----------------------------------")
print("We know that these letters get encrypted into:")

for p in sorted(pattern.iterkeys()):
	print("%d: %d" % (p, pattern[p]))