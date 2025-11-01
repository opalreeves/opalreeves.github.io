def add_surname(names):
    return [ name + " Kardashian" for name in names if name.lower().startswith("k")]

names_input = input("Enter first names separated by spaces: ").split()
result = add_surname(names_input)
print(result)