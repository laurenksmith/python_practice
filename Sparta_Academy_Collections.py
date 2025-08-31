
"""
# lists

# example_list = [1, True, "string"] # single data type ideal
#
# print(example_list[2])

the number in the square bracket indicates which item on the list to return. 0 = first item etc.
To return an item from the END of the queue, use -. So, -1 would return the very last item in the list,
-2 would return the second last item etc.


# shopping_list = ["bread", "eggs", "cheese"]

# shopping_list[1] = "bananas" # replaces an item in the index with this item. 0=first item, so 1 = 2nd item

# shopping_list.append("mushrooms") # adds an item to the end of our index

# shopping_list.pop() # removes the last item on the list

# shopping_list.pop(0) # removes a specific item from the list, using the index value. 0 = first item etc

# print(shopping_list.index("eggs"))

search function. This allows you to find a specific item in your list by returning it's index value.

# print(shopping_list)

# Dictionary

# key value pairs
contact_list = {  # curly brackets used for dictionaries
    "jane": "07385493"  # press enter to make space for dict. common to make more readable
}


Dictionaries allow you to manage complex data sets, compared to lists.
# print(contact_list["jane"]) # need to use specified key in square brackets, rather than index number/value

# Dictionaries don't have option to append list. Have to use the following syntax to add a key
# value to a dictionary

Similar process for amending data in dictionaries
contact_list["bob"] = "new number"

key method is useful as it returns all keys in dictionary, helpful in large dictionary
print(contact_list.keys())

 values method returns all keys in dictionary
print(contact_list.values)

contact_list["bob"] = "7987534"

print(contact_list)

# pop method will remove a particular entry and requires a key

print(contact_list.pop("jane"))
"""

theList = []
theList.append(1234)
theList.append(4567)
theList.append(99)
theList.append(5)

print(len(theList))