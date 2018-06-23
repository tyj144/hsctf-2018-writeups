# Andrew Wiles
**Other**, 250 pts

From https://codegolf.stackexchange.com/questions/32696/disprove-fermats-last-theorem, we figured that overflowing the integer taken in was a good idea. Playing around with cubed values around the max int, we found that 2048 * 2048 * 2048 = 0.

We tried 2048 for all three values, thinking that it would evaluate to 0 + 0 = 0, however, it did not. On the other hand 2048 * 2048 = 4194304 did indeed work for all three values, which gave us the flag.

An easy way to do this is by typing: 
`python -c "print('4194304 ' * 3)" | nc shell.hsctf.com 9999`

**Flag**: flag{contained_in_margins}
