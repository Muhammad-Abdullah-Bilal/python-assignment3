# ---
# ### **Basic Operations** 

# 1. Create a dictionary `student` with keys: `name`, `age`, and `grade`. Assign them appropriate values.

student = { 
    "name": "Muhammad Abdullah",
    "age": 19,
    "grade": "A",
    } 
 
# 2. Access the value of the key `grade` in the `student` dictionary.

print(student["grade"])

# 3. Add a new key `city` to the `student` dictionary and set its value to `"New York"`. 

student["city"] = "New York"
print(student)

# 4. Update the value of the `age` key in the `student` dictionary to `20`. 

student["age"] = 20
print(student)

# 5. Remove the key `city` from the `student` dictionary.  

del student["city"]
print(student)

# ---

# ### **Iterating through Dictionaries**  
# 6. Iterate through the dictionary `student` and print all keys. 

for each_key in student.keys():
    print(each_key)
# 7. Iterate through the dictionary `student` and print all values.

for each_value in student.values():
    print(each_value) 
# 8. Iterate through the dictionary `student` and print all key-value pairs in the format `key: value`.

for key, value in student.items():
    print(key, " : ", value)  
# 9. Check if the key `grade` exists in the `student` dictionary and print `True` or `False`.

print("grade" in student)
# 10. Count the total number of keys in the `student` dictionary.
  
total_keys = len(student)
print(total_keys)

# 2nd Approach
count = 0
for each_key in student.keys():
    count += 1
print(count)

# ---

# ### **Advanced Dictionary Usage** 
 
# 11. Merge the following two dictionaries and print the result:
  
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}   

dict1.update(dict2)
print(dict1)
# 12. Create a dictionary from a list of tuples: `[('name', 'Alice'), ('age', 25), ('city', 'Paris')]`.

list_of_touples = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
dictionary = dict(list_of_touples)
print(dictionary)

# 13. Sort the keys of the dictionary `{'z': 1, 'a': 2, 'c': 3}` in ascending order and print the sorted dictionary. 

my_dict = {'z': 1, 'a': 2, 'c': 3}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)

sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)

# 14. Reverse the dictionary `{'a': 1, 'b': 2, 'c': 3}` so that keys become values and values become keys. 

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in my_dictionary.items()}
print(reversed_dict)

# 15. Write a Python function to check if two dictionaries are identical (contain the same key-value pairs). 

def check_dict(dict1, dict2):
    if dict1 == dict2:
        return "Both dictionaries have the same key-value pairs."
    else:
        return "The dictionaries do not have the same key-value pairs."

dict1 = {
    "name": "Abdullah",
    "height": 5.4,
}
dict2 = {
    "name": "Shahzaib",
    "height": 5.2,
}

result = check_dict(dict1, dict2)
print(result)

# ---

# ### **Nested Dictionaries** 

# 16. Create a nested dictionary to represent the following data:  
#     ```plaintext
#     Person:  
#       Name: John  
#       Age: 30  
#       Address:  
#         Street: 123 Elm St  
#         City: Boston  
#     ```  

Person = {
    "Name": "John",
    "Age": 30,
    "Adress": {
        "Street": "123 Elm St",
        "City": "Boston",
    }
}
print(Person)

# 17. Access the value of the `City` key in the nested dictionary from the previous question.

print(Person["Adress"]["City"]) 

# 18. Add a new key `Phone` to the nested dictionary with the value `"123-456-7890"`.

Person["Adress"]["Phone"] = "123-456-7890"
print(Person)

# 19. Delete the `Address` key from the nested dictionary. 

del Person["Adress"] 
print(Person)

# 20. Iterate through all the keys in the outermost level of the nested dictionary and print them.

Person = {
    "Name": "John",
    "Age": 30,
    "Adress": {
        "Street": "123 Elm St",
        "City": "Boston",
    }
}
for key in Person.keys():
     print(key) 

# ---

# ### **Applications of Dictionaries**  


# 21. Use a dictionary to count the occurrences of each word in the string `"hello world hello python world"`. 

text = "hello world hello python world"
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1 

print(word_count)

# 22. Write a Python program to find the key with the maximum value in the dictionary `{'a': 10, 'b': 15, 'c': 7}`. 

dict = {'a': 10, 'b': 15, 'c': 7}
max_key = max(dict, key=dict.get)
print("Key with the maximum value:", max_key)

# 23. Create a dictionary to map numbers 1 to 5 to their squares (e.g., `{1: 1, 2: 4, 3: 9, ...}`). 

square_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(square_dict)
# Other method
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2
print(squares_dict)

# 24. Write a Python program to remove duplicate values from the dictionary `{'a': 10, 'b': 15, 'c': 10, 'd': 15}`.

my_dictionary = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
uniq_dict = {}
seen_values = set()
for key, value in my_dictionary.items():
    if value not in seen_values:
        uniq_dict[key] = value
        seen_values.add(value)

print(uniq_dict)

# 25. Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return `"Key not found"`.  

def get_value_from_dict(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return "key does not exist"

my_dict = {"a": 10, "b": 20, "c": 30}
print(get_value_from_dict(my_dict, "b"))  
print(get_value_from_dict(my_dict, "d")) 

# ---

# ### **Challenging Problems**  
# 26. Given two dictionaries `dict1 = {'a': 5, 'b': 10}` and `dict2 = {'a': 3, 'b': 7}`, write a Python program to add the values of matching keys and print the result. 

dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}
result = {}
for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + dict2[key] 

print(result)

# 27. Write a Python program to create a dictionary where the keys are the first `n` positive integers, and the values are their cubes. Take `n` as user input.

n = int(input("Enter a number:"))
dictionary = {}
for i in range(1, n+1):
    value = i ** 3
    dictionary[i] = value
print (dictionary)

# 28. Flatten the following nested dictionary into a single-level dictionary:  
#     {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
del dict

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)

# 29. Write a Python program to split a dictionary into two based on whether the values are odd or even.

def split_dict_by_odd_even(d):
    even_dictionary = {}
    odd_dictionary = {}

    for key, value in d.items():
        if value % 2 == 0:
            even_dictionary[key] = value
        else:
            odd_dictionary[key] = value
    return even_dictionary, odd_dictionary

input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
even_dictionary, odd_dictionary = split_dict_by_odd_even(input_dict)
print("Even dictionary:", even_dictionary)
print("Odd dictionary:", odd_dictionary)

# 30. Create a dictionary comprehension to filter out all keys in `{'a': 1, 'b': 2, 'c': 3, 'd': 4}` where the value is less than 3. 

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {key: value for key, value in original_dict.items() if value >= 3}
print(filtered_dict)

# ---