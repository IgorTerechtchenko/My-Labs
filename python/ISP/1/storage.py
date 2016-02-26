import re
class Storage:
    def __init__(self):
        self.un_collection = set()
   
    def add(self, item):
        if item in self.un_collection:
            print "Item '{}' already exists".format(item)
        else: 
            self.un_collection.add(item)
            print "Item '{}' added".format(item)
    
    def remove(self, item):
        if item in self.un_collection:
            self.un_collection.remove(item)
            print "Item '{}' removed".format(item)
        else:
            print "Item '{}' does not exist".format(item)
           
    def find(self, item):
        if item in self.un_collection:
            print "Item {} found",format(item)
        else:
            print "Item {} not found".format(item)        
    
    def list(self):
        print ", ".join(self.un_collection)

    def save(self, file_name):
        try:
            with open(file_name, "w") as file:
                file.write(", ".join(self.un_collection))
        except IOError:
            print "File '{}' doesn't exist:".format(file_name)
        
    def load(self, file_name):
        try:
            with open(file_name, "r") as file:
                text = file.read()
                self.un_collection = set(text.split(","))
        except IOError:
            print "File '{}' doesn't exist:".format(file_name)

    def grep(self, exp): 
        try:
            expression = re.compile(exp)
            found = False
        except re.error:
            print "Invalid regexp"
            return
        for x in self.un_collection:
            result = expression.match(x)
            if result != None:
                print x
                found = True
        if found != True:
            print "No matches found."
