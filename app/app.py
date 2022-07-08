from app.math.math import plus


def main():
    try:
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        print("Sum of a + b = " + str(plus(a, b)))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
