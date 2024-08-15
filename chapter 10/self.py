class employee:
    language = "py"
    salary = 120000
    # Self is required to point out about which attributes function is talking about
    # Rather than giving all the parameter we use self
    # Self indicated at whatever attributes the related object contain it is going to consider those attributes only
    def getInfo(self):
        print(f"The language is {self.language}. THe salary is {self.salary}")
    
    def greet(self):
        print("Good morning")


    # By marking it as staticmethod the method would not be required with any attributes and object specifier.
    @staticmethod
    def greeting():
        print("Hey How are you!!")
    


shivansh = employee()

shivansh.getInfo()
shivansh.greet()
shivansh.greeting()