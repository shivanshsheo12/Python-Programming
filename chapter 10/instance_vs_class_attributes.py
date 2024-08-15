class employee:
    # This is a class attribute
    name = "Ramesh"
    language = "py"
    salary = 120000

shivansh = employee()
shivansh.name = "Shivansh" # This is a object attribute
print(shivansh.name,shivansh.language,shivansh.salary)

# Between class attribute and instance attribute, instance attribute are preffered over class one