# QUESTION 1:
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        # Calculate the amount to discount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price


# QUESTION 2:
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
# Print the final price after applying the discount, or if no discount was applied, print the original price.

# Prompt user for input using Kenyan Shillings (Ksh)
try:
    original_price = float(input("Enter the original price of the item (Ksh): "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Use the function to calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output result based on whether discount was applied
    if final_price < original_price:
        print(f"The final price after {discount_percent}% discount is: Ksh {final_price:.2f}")
    else:
        print(f"No discount was applied. The price remains: Ksh {original_price:.2f}")

except ValueError:
    print("Error: Please enter valid numbers for price and discount. Example: 500 or 15.5")
