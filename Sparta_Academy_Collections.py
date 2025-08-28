# lists

# example_list = [1, True, "string"] # single data type ideal
#
# print(example_list[2])
"""
the number in the square bracket indicates which item on the list to return. 0 = first item etc.
To return an item from the END of the queue, use -. So, -1 would return the very last item in the list,
-2 would return the second last item etc.

"""
shopping_list = ["bread", "eggs", "cheese"]

# shopping_list[1] = "bananas" # replaces an item in the index with this item. 0=first item, so 1 = 2nd item

# shopping_list.append("mushrooms") # adds an item to the end of our index

# shopping_list.pop() # removes the last item on the list

# shopping_list.pop(0) # removes a specific item from the list, using the index value. 0 = first item etc

print(shopping_list.index("eggs"))
"""
search function. This allows you to find a specific item in your list by returning it's index value.
"""
print(shopping_list)