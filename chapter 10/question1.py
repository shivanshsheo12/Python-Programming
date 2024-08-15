class Programmer:

    def __init__(self,name,domain):
        self.name = name
        self.domain = domain
    
    def getinfo(self):
        print(f"Programmer Name : {self.name}")
        print(f"Domain : {self.domain}")


shivansh = Programmer("Shivansh","Frontend")
gaurav = Programmer("Gaurav","Backend")
vijay = Programmer("Vijay","Full Stack")


shivansh.getinfo()
gaurav.getinfo()
vijay.getinfo()