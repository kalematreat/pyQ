# 3/4 --> 1,3,4
#1. Write a program to merge two dictionaries.
def merge_dictionaries(dict1, dict2):
    # merged_dict = dict1.copy()
    merged_dict={}
    merged_dict.update(dict1)   
    merged_dict.update(dict2)   
    return merged_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}
merged = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged)

#3. Write a Python function to check if a key exists in a dictionary.
def key_exists(my_dict, key):
    if key in my_dict:
        return True
    else:
        return False
my_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'mango': 5}
key_to_check = 'banana'
print(f"Does the key '{key_to_check}' exist? {key_exists(my_dict, key_to_check)}")
key_to_check = 'grape'
print(f"Does the key '{key_to_check}' exist? {key_exists(my_dict, key_to_check)}")

#4. Implement a program to invert the keys and values of a dictionary.
def invert_dictionary(my_dict):
    inverted_dict = {v: k for k, v in my_dict.items()}
    return inverted_dict
my_dict = {'apple': 10, 'banana': 2, 'orange': 5, 'mango': 7}
inverted = invert_dictionary(my_dict)
print("Inverted Dictionary:", inverted)

