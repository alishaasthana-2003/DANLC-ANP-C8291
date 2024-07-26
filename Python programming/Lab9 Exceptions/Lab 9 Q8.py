#Exception Handling in List Operations
#- Write a function `safe_list_access` that takes a list and an index as arguments and returns the element at that index. Use exception handling to manage:
#- Index out of range.
#- Any other error (provide a generic error message).
#- Test the function with various lists and indices, including valid, negative, and out-of-range indices.

def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."
    except Exception as e:
        return f"An error occurred: {e}"


print(safe_list_access([1, 2, 3, 4], 2))
print(safe_list_access([1, 2, 3, 4], -1))
print(safe_list_access([1, 2, 3, 4], 10))
print(safe_list_access([1, 2, 3, 4], 'a'))
print(safe_list_access([], 0))  
