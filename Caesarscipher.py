Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Sample Input
11
middle-Outz
2

Sample Output

okffng-Qwvb

Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b


#code
def caesarCipher(s, k):
    r=[]
    for i in s:
        if((i.isalpha()) and (i.isupper())):
            r.append(chr((int(ord(i)-65+k))%26 +65))
        elif((i.isalpha()) and (i.islower())):
            r.append(chr((int(ord(i)-97+k))%26 +97))
        else:
            r.append(i)
    s = "".join(r)        

    return s      
