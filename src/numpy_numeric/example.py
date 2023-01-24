import numpy as np


class numeric:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation if (operation in ["add","sub","divide","multiply","*","+","-","/","subtract"]) else print("Not a valid operation")


    def method(self):
        if self.operation == "+" or self.operation == "add":
            result = np.add(self.a,self.b)
            print(f"addition of %s + %s = %s"%(self.a,self.b,result))

        elif self.operation == "-" or self.operation =="sub" or self.operation =="subtract":
            result = np.subtract(self.a, self.b)
            print(f"subtraction of %s - %s = %s"%(self.a,self.b,result))

        elif self.operation == "*" or self.operation =="multiply":
            result = np.multiply(self.a, self.b)
            print(f"multiplication of %s * %s = %s"%(self.a,self.b,result))

        elif self.operation == "/" or self.operation =="divide":
            result = np.divide(self.a, self.b)
            print(f"division of %s / %s = %s"%(self.a,self.b,result))

        else:
            print("Not a vaild operation")

        return result

def run():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=float, help="number 1")
    parser.add_argument("b", type=float, help="number 2")
    parser.add_argument("operation", type=str, help="operation")

    args = parser.parse_args()
    num = numeric(args.a, args.b, args.operation)
    result = num.method()

    return result


if __name__ == "__main__":
    run()
    
