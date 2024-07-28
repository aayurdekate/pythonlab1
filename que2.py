# Que(2) Let A=[‘abc’, ‘xyz’, ‘aba’, '1221’] be a given string, and write a Python
# program that prints the string or strings and their index from the given list,
# ensuring that the first and last characters of the strings to be printed are
# identical.
def print_matching_strings(A):
    for index, item in enumerate(A):
        if isinstance(item, str) and len(item) > 0 and item[0] == item[-1]:
            print(f"Index: {index}, String: {item}")

A = ['abc', 'xyz', 'aba', '1221']
print_matching_strings(A)

