import sys

def calculate(smartwatch, laptop, smartphone):
    total = smartwatch + laptop + smartphone
    return total

if __name__ == "__main__":
    smartwatch = float(sys.argv[1])
    laptop = float(sys.argv[2])
    smartphone = float(sys.argv[3])

    total = calculate(smartwatch, laptop, smartphone)
    print("Total:", total)



