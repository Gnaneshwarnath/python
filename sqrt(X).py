num = float(input("Enter a number: "))

# Handle negative input if necessary
if num < 0:
    print("Please enter a non-negative number.")
else:
    # Initial guess for the square root
    sqrt_guess = 1.0

    # Iterate to improve the guess
    for _ in range(10):  # You can adjust the number of iterations for better accuracy
        sqrt_guess = 0.5 * (sqrt_guess + num / sqrt_guess)

    # Convert the square root to an integer (round down)
    rounded_sqrt = int(sqrt_guess)

    print("The rounded square root of {0} is: {1}".format(num, rounded_sqrt))
