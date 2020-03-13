# sets are like lists but without repeated elements

s = set([1,2,3])
t = set([3,4,5])

print("Set s:",s)
print("Set t:",t)
print("union", s.union(t))
print("Intersection:", s.intersection(t))
print("s difference t:",s.difference(t))
print("t difference s:",t.difference(s))

print("1 in s:", 1 in s)
print("1 not in t:", 1 not in t)