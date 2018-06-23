# Teacher Struggles
**Algo**, 100pts

```
enc = "zkdxmxkhvgofoqvyeccuxokfimbtyhrbkpougnvzbhseotymydwbadenbzxrzfanxetkvyiczvoybearnqszydnwhrjamlpcqfxi"
num = 0
for letter in enc:
  if letter == "h":
    num = num + 1
  elif letter == "s":
    num = (num + 1) * 2
  elif letter == "c":
    num = (num + 1) * 3
  elif letter == "t":
    num = (num + 1) * 4
  elif letter == "f":
  	num = (num + 1) * 5

print(num)
```
Concise version:
enc = "zkdxmxkhvgofoqvyeccuxokfimbtyhrbkpougnvzbhseotymydwbadenbzxrzfanxetkvyiczvoybearnqszydnwhrjamlpcqfxi"
num = 0
multiples = { "h": 1, "s": 2, "c": 3, "t": 4, "f": 5 }

for letter in enc:
  if letter in multiples:
  	num = (num + 1) * multiples[letter]

print(num)

**Flag**: 29774315