#Write a Python program to find duplicate values from a list and display those.
def find_duplicates(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

