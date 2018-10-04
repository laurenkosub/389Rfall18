Writeup 5 - Binaries I
======

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 5 Writeup

My first approach to the problem was to translate the C functions given to us
from C to assembly seeing that the functions themselves where short and only
really emcompassed a loop with one line of code in the loop.

I used labels to simulate the loops. I did this by first comparing i and strl/len
and then jumping to the done label if i was not less than strl/len. at the end
of the loop, I incremented i and simply jumped back up to the comparison line.

For memset, you are indexing a string so you want to access every byte.
I had to move val (1 char) into the i-th byte of str. To do this,
I needed to isolate 1 byte of val (by referencing sil instead of all of rsi).
I then moved sil into the i-th byte of rdi (str) which is emcompassed in the
following line:
    mov byte [rdi+rax], sil     ;rax = counter (i), rdi = str, rsi = val
That line translates to "move sil into the address [rdi+rax] points to".

I was able to apply the same thinking to strncpy, where the only difference was
that you needed to move src[i] into dst[i] (so moving a byte of a string into
a byte of a string instead of just a value into a byte of a string). To do this,
I used a register (rbx, or more specifically bl because I only needed to store
1 bit). I moved 1 byte of [rsi+rax] (src[i]) into bl, then I moved bl into 
byte [rdi+rax] to get the following two lines:
    mov     bl, byte [rsi + rax] 
    mov     byte [rdi+rax], bl

One issue I ran into when I initially did this was the 'invalid size for operand'
issue. Instead of moving a bit of [rsi+counter] into bl (1 bit of the register),
I moved it into rbx (8 bits of the register), which didn't match the size. After
thinking about it for a bit, I determined it to be a size issue (since the error
stated: 'invalid size') in my dst[i] = src[i] portion of the code, so I tried to
isolate the one bit instead of using a full 8 bits of the register and that worked.

