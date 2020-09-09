friends_ages = {"Rolf": 30, "Bob": 45, "Sara": 50}

for friend in friends_ages:
    print(f"{friend} is {friends_ages[friend]} years old")
    print(friend)

print(friends_ages)
# print(friends_ages.items()) # not quite a list....
friends = (list(friends_ages.items()))
for friend in friends:
    print(type(friend)) # so applying list to a dict.items returns a list of tuples

flist = (list(friends_ages.items()))
for f in flist:
    print(f"{f} is in the list of tuples; applying list to a dict.items returns a list of key-value tuples")

print(friends_ages.values())

for value in friends_ages.values():
    print(f"{value} is of type {type(value)}")
print(friends_ages.keys())
#

for friend, age in friends_ages.items():
    print(f"{friend} is {age} years old")

if "John" in friends_ages:
    print("John attended the school")
else:
    print("John did not attend")

ave_age = sum(friends_ages.values()) / len(friends_ages)
print(f"The average age of my friends is {ave_age}")
