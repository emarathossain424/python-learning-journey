'''
Find the final amount to pay

Step 1 — The inputs you get
When someone is buying something, you’ll have:

total_amount – the starting price before discounts.
Example: 800

membership_level – the customer’s membership tier.
Options: "none", "silver", "gold", "platinum"

coupon_code – a special discount code.
Options: "DISC10", "DISC20", "BOGO", or "" (meaning no coupon).

is_first_purchase – whether this is their first time buying.
True or False.

Step 2 — Membership discount rules
The first discount is based on membership:

silver → 5% off

gold → 10% off

platinum → 15% off

none → no discount

Step 3 — Coupon discount rules
After the membership discount, check if they used a coupon:

"DISC10" → 10% off the new amount

"DISC20" → 20% off the new amount, but only if the new amount is more than 500

"BOGO" → if the new amount is above 200, subtract 100 flat

Step 4 — First purchase bonus
If is_first_purchase is True and the total after all discounts is still above 300, subtract another 50.

Step 5 — Prevent negative amounts
If the total somehow becomes less than 0, make it 0.

Step 6 — Final output
Your program should print:

The final amount to pay

Which discounts were applied and in what order
'''

initial_amount = 800
membership_level = "gold"
coupon_code = "DISC20"
is_first_purchase = True

def calculate_final_amount(total_amount, membership_level, coupon_code, is_first_purchase):
    
    # Membership discount
    if membership_level == "silver":
        total_amount -= total_amount * 5/100
        print(f"After applying 5% silver membership discount final amount is: {total_amount}")
    elif membership_level == "gold":
        total_amount -= total_amount * 10/100
        print(f"After applying 10% gold membership discount final amount is: {total_amount}")
    elif membership_level == "platinum":
        total_amount -= total_amount * 15/100
        print(f"After applying 15% platinum membership discount final amount is: {total_amount}")

    # Coupon discount
    if coupon_code == "DISC10":
        total_amount -= total_amount * 10/100
        print(f"After applying 10% DISC10 coupon discount final amount is: {total_amount}")
    elif coupon_code == "DISC20":
        if total_amount > 500:
            total_amount -= total_amount * 20/100
            print(f"After applying 20% DISC20 coupon discount final amount is: {total_amount}")
    elif coupon_code == "BOGO":
        if total_amount > 200:
            total_amount -= 100
            print(f"After applying BOGO coupon discount final amount is: {total_amount}")

    # First purchase bonus
    if is_first_purchase and total_amount > 300:
        total_amount -= 50
        print(f"After applying first purchase bonus final amount is: {total_amount}")

    # Prevent negative amounts
    if total_amount < 0:
        total_amount = 0

    return total_amount

final_amount = calculate_final_amount(initial_amount, membership_level, coupon_code, is_first_purchase)
print(f"The final amount to pay is: {final_amount}")
