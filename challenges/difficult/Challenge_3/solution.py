from itertools import permutations

with open('wordlist.txt', 'r') as f:
    words = set([word.strip() for word in f.readlines()])


with open('scrambled.txt', 'r') as f2:
    scrambled = set([word.strip() for word in f2.readlines()])

for word in scrambled:
    perm = set([''.join(per) for per in permutations(word)])
    match = (words & perm).pop()
    print('{0} -> {1}'.format(word, match))
