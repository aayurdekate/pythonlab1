# Given lists
colour_names = ["Black", "Red", "Maroon", "Yellow"]
colour_codes = ["000000", "FF0000", "800000", "FFFF00"]

# Convert to list of dictionaries
list_of_dicts = [{"colorName": name, "colorCode": code} for name, code in zip(colour_names, colour_codes)]

# Print the resulting list of dictionaries
print(list_of_dicts)
