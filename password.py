# generate a password with length "passlen" with no duplicate characters in the password
import random

s = "abcdefghijklmnopqrstuvwxyz"
n = "01234567890"
slen = 4
nlen = 4
p =  "".join(random.sample(s, slen))
p2 =  "".join(random.sample(n, nlen))
p = p.title()
pw = (p + p2)
print pw
