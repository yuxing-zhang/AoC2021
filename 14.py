from collections import Counter

# Linked list to contain the data and count the occurrence of each letter
class LL():
    def __init__(self, seq='', table={}):
        self.h = None
        self.table = table
        for i in seq[::-1]:
            self.h = [i, self.h]
    def insert(self):
        p = self.h
        while p[1]:
            p[1] = [self.table[p[0]+p[1][0]], p[1]]
            p = p[1][1]
    def count(self):
        c = Counter()
        p = self.h
        while p:
            c[p[0]] += 1
            p = p[1]
        return c

# Input data processing
with open('input.txt') as f:
    seq = f.readline()[:-1]
    table = {l[:2]: l[-2] for l in f.readlines()[1:]}

# Part 1
l = LL(seq, table)

for i in range(10): l.insert()
count = sorted(l.count().values())
print(count[-1] - count[0])

# Part 2
# A naive scaling of the previous algorithm is guaranteed to overflow
# the memory. Instead, we only iterate to 20 steps and count the
# occurrence of each letter in the strings produced by iterating every
# length-2 substring another 20 steps.

# Following part 1, l has already been iterated 10 steps
# for i in range(10): l.insert()
l = LL(seq, table)

# Caching the occurrence of each letter in string generated by every
# possible length-2 substring
c19 = {}
for k in table:
    l_ = LL(k, table)
    for i in range(19): l_.insert()
    c19[k] = l_.count()

# The occurrence of each letter after 40 steps can be obtained by adding
# the occurence tables generated by every letter after 20 steps and
# subtracting the occurence of every letter at the 20th step except the
# ends and subtracting the inserted letters at the 21st step.
p = l.h
count = Counter(p[0])
while p[1]:
    t = table[p[0] + p[1][0]]
    count += c19[p[0] + t] + c19[t + p[1][0]]
    count[t] -= 1
    count[p[0]] -= 1
    p = p[1]

count = sorted(count.values())
print(count[-1] - count[0])
