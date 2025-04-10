import math_utils

main = lambda: (
    (lambda: (
        print("result:", {
            "+": math_utils.add,
            "-": math_utils.subtract,
            "*": math_utils.multiply,
            "/": math_utils.divide,
            "**": math_utils.power,
            "%": math_utils.mod
        }.get(
            (op := input("enter operator (+, -, *, /, **, %): ")),
            lambda x, y: "invalid operator."
        )(x := float(input("enter the first number: ")), y := float(input("enter the second number: "))))
    ))()
    if True else None
)

try:
    if __name__ == "__main__":
        main()
except ValueError:
    print("invalid input.")
