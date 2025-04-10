collection={1,4,5,4,1,7,"hello","world"}

print(collection)
print(type(collection))
print(len(collection))

empltyset=set()
print(type(empltyset))


empltyset.add(2)
empltyset.add(4)
empltyset.add(2)


print(empltyset)

empltyset.remove(2)

print(empltyset)

empltyset.clear()
print(empltyset)

#unioon
set1={1,4,6,7,8}
set2={4,7,9,8}

print(set1.union(set2))


#intersection

print(set1.intersection(set2))