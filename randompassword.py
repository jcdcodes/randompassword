#!/usr/bin/env python
import random

words = [w.strip() for w in open('/usr/share/dict/words').readlines() if len(w)>4 and len(w)<9]

print random.choice(words),
print random.choice(words),
print random.choice(words),
print random.choice(words)
print len(words), "^ 3 =", len(words)**3
print len(words), "^ 4 =", len(words)**4
