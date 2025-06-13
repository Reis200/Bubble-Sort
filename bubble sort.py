# bubble sort
import sys

class Program:
    def __init__(self):
        self.list_input = input("Enter a list of of items to be sorted seperated by commas e.g 1,2,3 or a,b,c,d:")
        self.list = self.list_input.split(",")
        print(self.list)
        self.list_type = input("Do you want to sort a list of text, numbers, or decimals: ")
        self.list_type = self.list_type.strip()
        self.list_type = self.list_type.lower()
        match self.list_type:
            case "t":
                self.list_type = "string"
            case "text":
                self.list_type = "string"
            case "texts":
                self.list_type = "string"
            case "n":
                self.list_type = "number"
            case "number":
                self.list_type = "number"
            case "numbers":
                self.list_type = "number"
            case "d":
                self.list_type = "decimal"
            case "decimal":
                self.list_type = "decimal"
            case "decimals":
                self.list_type = "decimal"
            case _:
                print("We could not identify the type of list please re-run and try again...")
                sys.exit()

        print(self.list_type + " sort type has been selected")

    def bubble_sort(self):
        if self.list_type == "number":
            self.list = [int(item.strip()) for item in self.list]
        elif self.list_type == "decimal":
            self.list = [float(item.strip()) for item in self.list]

        print(self.list)
        
        swapped = True
        while swapped == True:
            swapped = False
            for itemIndex in range(0,len(self.list)-1):
                if self.list[itemIndex] > self.list[itemIndex + 1]:
                    temp = self.list[itemIndex]
                    self.list[itemIndex] = self.list[itemIndex + 1]
                    self.list[itemIndex + 1] = temp
                    swapped = True

        print("List sorted:")
        print(self.list)
        
                
program1 = Program()
program1.bubble_sort()
