
# Creating sets
myset = {"apple", "banana", "cherry"}
set2 = {"banana", "dates", "mango"}

# Displaying set
print("Initial set:", myset)

# Length of set
print("Length:", len(myset))

# Add element
myset.add("orange")
print("After add():", myset)

# Add multiple elements
myset.update(["grapes", "kiwi"])
print("After update():", myset)

# Remove element (throws error if not found)
myset.remove("banana")
print("After remove('banana'):", myset)

# Discard element (no error if not found)
myset.discard("papaya")
print("After discard('papaya'):", myset)

# Pop element (removes random element)
removed = myset.pop()
print("After pop():", myset)
print("Popped element:", removed)

# Clear set
temp_set = myset.copy()
temp_set.clear()
print("After clear():", temp_set)

# Copy set
copy_set = myset.copy()
print("Copied set:", copy_set)


# Union
union_set = myset.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = myset.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = myset.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
sym_diff_set = myset.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)


set3 = myset.copy()
set3.intersection_update(set2)
print("\nintersection_update():", set3)

set4 = myset.copy()
set4.difference_update(set2)
print("difference_update():", set4)

set5 = myset.copy()
set5.symmetric_difference_update(set2)
print("symmetric_difference_update():", set5)


setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

print("\nSetA:", setA)
print("SetB:", setB)

print("issubset():", setA.issubset(setB))
print("issuperset():", setB.issuperset(setA))
print("isdisjoint():", setA.isdisjoint(set2))


print("\nIs 'apple' in myset?", "apple" in myset)
print("Is 'banana' not in myset?", "banana" not in myset)
