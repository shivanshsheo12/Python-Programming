class employee:
    # This is a class attribute
    language = "py"
    salary = 120000

shivansh = employee()
shivansh.name = "Shivansh" # This is a object attribute
print(shivansh.name,shivansh.language,shivansh.salary)

rohan = employee()
rohan.name = "Rohan"
print(rohan.name,rohan.language,rohan.salary)
