# use python2
# reference => https://youtu.be/227Pr6Yhj4Q
import base64
import itertools

# base64 were written in gif frames
img = ['zg5', 'zND', 'MAo=', 'MTI', 'U2N']

perm = list(itertools.permutations(img))

for i in (itertools.permutations(['zg5', 'zND', 'MAo=', 'MTI', 'U2N'])):
    flag = ''.join(i)
    try:
        print(base64.decodestring(flag))
    except:
            pass
