# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band_two = dict(vocals="Plant", guitar="Page")

print(band, band_two)
print(type(band))
print(len(band))

# Acces items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key value paris as tuples
print(band.items())

# Verify akey exists
print("guitar" in band)
print("triangle" in band)

# Change values

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# Delefe and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band_two.clear()
print(band_two)

del band_two

# Copy dictionaries

# band_two = band  # create a reference
# print("Bad copy!")
# print(band_two)
# print(band)

# band_two["drums"] = "Dave"
# print(band)

band_two = band.copy()
band_two["drums"] = "Dave"
print("Good Copy!")
print(band)
print(band_two)

# or use the dict() constructor function
band_tree = dict(band)
print("Good Copy!")
print(band_tree)

# Nested dictionaries
member_one = {"name": "Plant", "instrument": "vocalse"}
member_two = {"name": "Page", "instrument": "guitar"}
band = {"member_one": member_one, "member_two": member_two}

print(band)
print(band["member_one"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums_two = set((1, 2, 3, 4))

print(nums)
print(nums_two)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True ia a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 5}
print(nums)

# Checi id a value is in a set
print(2 in nums)


# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to anothr
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

# You can use update with lists, tuples and dictionaries too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
