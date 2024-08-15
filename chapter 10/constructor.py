class employee:
    language = "py"
    salary = 120000

    # Init method will always be called when a new object is created 
    def __init__(self,language,salary): # dunder method which is automatically called (starts with __ )
        print("A new object has been created")
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language}. THe salary is {self.salary}")
    
    

shivansh = employee("javascript",250000)
shivansh.getInfo()