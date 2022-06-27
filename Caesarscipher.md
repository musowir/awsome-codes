Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

    string s: cleartext
    int k: the alphabet rotation factor

Returns

    string: the encrypted string
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


code

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
