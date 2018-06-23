# Review
**Binary**, 100pts

Run `nc shell.hsctf.com 10000` in the terminal to connect to the program.

We know from the C file that the program will submit the review and display the flag if valid is true, meaning it is not 0. However, valid is defined at 0 near the beginning of the file.

To trigger the `if (valid)` case, we have to overwrite valid somehow. We can do this with a simple buffer overflow. We will simply feed in a title longer than the 32 bytes allocated to `buffer`, which will begin overwriting memory outside of `buffer` and eventually overwrite `valid` to be non-zero.

We can give the program the movie title, “BOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIIIBOIIIIII” to overwrite the memory outside of the buffer and rate the movie a 1 in order to bypass the “Invalid rating” case.

**Flag**: flag{r0tt3n_p0t4t035_rul3z!!!}