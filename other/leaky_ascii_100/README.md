# Leaky Ascii
**Other**, 100pts
This one was actually pretty cool. When you first connect, you see a bunch of asterisks and can’t see the password Keith is sending over. Not only that, when he asks you to send the password back over to confirm that you got it, it doesn’t even let you type it in.

However, if you try to write the output to a file, the actual password gets written to your file and you can see it. We can do this by typing “nc shell.hsctf.com 10101 > leaky_ascii.txt”. He tells you that the password is: “p106iWIcJpF5dLBew2ZaaBVGqZuLw77G” and you have to send it back to him.

And not only does the password get written to the file, but the fact that the output is getting written into a file stops the program and gives you an opportunity to enter the flag back in. So you can type “p106iWIcJpF5dLBew2ZaaBVGqZuLw77G” back in, and the program will receive it, and send the flag back, which you can find in the txt file.

**Flag**: flag_{3ScaPE_C0De5_4_l1F3}