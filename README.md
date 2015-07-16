# randompassword

A good password is hard to guess but easy to remember.  https://xkcd.com/936/ explains one way to do this.

## Usage

This script picks four random words for you.  It then shows you the number of similar combinations it could have come up with.  (On my machine, the `words.txt` file contains 57,077 words.  I haven't heard of a lot of them, but they're at least memorable.)

<pre>
$ ./randompassword.py
Scalops sugent fizgig Ovampo
57077 ^ 3 = 185944533315533
57077 ^ 4 = 10613156128050677041
</pre>

You'll need to have Python installed, which will be the case on any Mac or Linux machine.  Haven't even considered how to deal with Windows; pull requests welcome.
