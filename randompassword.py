#!/usr/bin/env python
import random

try:
    words = [w.strip() for w in open('/usr/share/dict/words').readlines() if len(w)>4 and len(w)<9]
except:
    words = [w.strip() for w in open('/usr/share/dict/american-english').readlines() if len(w)>4 and len(w)<9]

# We use SystemRandom here because the default random claims not to be random enough.
r = random.SystemRandom()

print r.choice(words),
print r.choice(words),
print r.choice(words),
print r.choice(words)
print len(words), "^ 3 =", len(words)**3
print len(words), "^ 4 =", len(words)**4
