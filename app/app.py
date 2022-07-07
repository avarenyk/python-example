from app.math.math import plus
from app.Conditional_operator.max import max


def main():
    try:
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        print("Sum of a + b = " + str(plus(a, b)))
        print("Max of a and b = " + str(max(a, b)))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
    
