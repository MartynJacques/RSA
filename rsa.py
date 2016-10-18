import math

def generate_key(p, q):
    n = p * q
    totient_n = (p - 1) * (q - 1)
    e = find_e(totient_n)
    d = find_d(e, totient_n)
    return e, d, n

def find_d(e, totient_n):
    # 1 = (e*d)mod(totient_n)
    for d in range(totient_n, 1, -1):
        if ((e * d) % totient_n) == 1:
            return d

def find_e(totient_n):
    for e in range(2, totient_n):
        # if gcd = 1, then relative prime so return x
        if gcd(e, totient_n) == 1:
            return e

def gcd(a, b):
    t = 0;
    while(b != 0):
        t = a;
        a = b;
        b = t%b;
    return a;

def encrypt(m, e, n):
    # c = m^d mod n
    return math.pow(m, e) % n

def decrypt(c, d, n):
    # m = c^d mod n
    return math.pow(c, d) % n

e, d, n = generate_key(7, 17)
print "e = {0}. d = {1}, n = {2}".format(e, d, n)

original_m = 19
print "Original message: {0}".format(original_m)

c = encrypt(original_m, e, n)
print "Encrypted message: {0}".format(c)

recieved_m = decrypt(c, d, n)
print "Decrypted message: {0}".format(recieved_m)
