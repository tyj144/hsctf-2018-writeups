# OK
**Algo**, 250pts

We initially figured out that it was impossible to have more than two “O”s in a row because when a K changes into KO or an O changes into an OK, the O will always be attached to another K. Thus, the best we could do is “KOOK”.

We wrote a script that counted the number of “OO” pairs in a given string, which you can find here. This gave us the output:
1: 0
2: 1
3: 1
4: 3
5: 5
6: 11
7: 21
8: 43
9: 85
10: 171
11: 341
12: 683
13: 1365
14: 2731
15: 5461
16: 10923
17: 21845
18: 43691
19: 87381

This script was also incredibly slow, because it requires exponential time to expand each string and then it has to count all the pairs in the string. 

However, we noticed a pattern in the output, namely that the output roughly doubled each time. More specifically, the output was twice the previous plus one if we were on an odd reply, and twice the previous minus one if we were on an even reply. With this in mind, we could write a simple function that mimicked this output but was not exponential time. 

This script looks like:
```
num = 0
for i in range(1, 1000):
	num *= 2
	if (i % 2 == 1):
		num += 1
	else:
		num -= 1

print(num % (10 ** 9 + 7))
```

**Flag**: 114737202
