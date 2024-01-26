def menu_for_users():
    print("\n" + "*" * 20 + " BPP Pizza Place Order Menu " + "*" * 20)
    print("╔" + "=" * 70 + "╗")
    print("""
                    Price For Each Pizza : £ 12.00

    **** Discount Offers *****

    -- 50% off on orders placed on tuesday 
    -- 25% off for orders placed using the app 
    -- Free delivery for ordering more than 5 pizzas 

                |Extra 2.5 charge for delivery|
    """)
    print("╚" + "=" * 70 + "╝")


def take_user_input():
    print("\n" + "*" * 20 + " BPP Pizza Place Order " + "*" * 20)
    print("=" * 70)

    while True:
        try:
            pizza_quantity = int(input('\nPlease enter the number of pizzas to order: '))
            if pizza_quantity > 0:
                break
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter a valid number!')

    delivery_requirement = input('\nDo you want the pizza to be delivered to your location (Y/N)? : ').upper()
    while delivery_requirement not in ['N', 'Y']:
        print("Please answer 'Y' or 'N'")
        delivery_requirement = input('\nDo you want the pizza to be delivered to your location (Y/N)? : ').upper()

    day_discount = input('\nAre you placing the order on Tuesday (Y/N)? : ').upper()
    while day_discount not in ['N', 'Y']:
        print("Please answer 'Y' or 'N'")
        day_discount = input('\nAre you placing the order on Tuesday (Y/N)? : ').upper()

    app_use = input('\nDid you use the app to place this order? (Y/N) : ').upper()
    while app_use not in ['N', 'Y']:
        print("Please answer 'Y' or 'N'")
        app_use = input('\nDid you use the app to place this order? (Y/N) : ').upper()

    print("=" * 70)
    print("\n" + "*" * 10 + " Thank You For Your Order!! Here Is Your  Total Bill!! " + "*" * 10)

    return pizza_quantity, delivery_requirement, day_discount, app_use


def app_use_pizza_price(in_pizza_number, delivery, is_tuesday):
    if is_tuesday == 'Y' and in_pizza_number >= 5:
        price = ((pizza_number * 12) * 0.50) * (1 - 0.25)
        return price
    elif is_tuesday == 'Y' and in_pizza_number < 5:
        if delivery == 'Y':
            price = ((pizza_number * 12 + 2.50) * 0.50) * (1 - 0.25)
            return price
        else:
            price = ((pizza_number * 12) * 0.50) * (1 - 0.25)
            return price
    elif is_tuesday == 'N' and in_pizza_number >= 5:
        price = (pizza_number * 12) * (1 - 0.25)
        return price
    elif is_tuesday == 'N' and in_pizza_number < 5:
        if delivery == 'Y':
            price = (pizza_number * 12 + 2.50) * (1 - 0.25)
            return price
        else:
            price = (pizza_number * 12) * (1 - 0.25)
            return price


def no_app_use_pizza_price(in_pizza_number, delivery, is_tuesday):
    if is_tuesday == 'Y' and in_pizza_number >= 5:
        price = ((pizza_number * 12) * 0.50)
        return price
    elif is_tuesday == 'Y' and in_pizza_number < 5:
        if delivery == 'Y':
            price = ((pizza_number * 12 + 2.50) * 0.50)
            return price
        else:
            price = ((pizza_number * 12) * 0.50)
            return price
    elif is_tuesday == 'N' and in_pizza_number >= 5:
        price = (pizza_number * 12)
        return price
    elif is_tuesday == 'N' and in_pizza_number < 5:
        if delivery == 'Y':
            price = (pizza_number * 12 + 2.50)
            return price
        else:
            price = (pizza_number * 12)
            return price


def calculate_total_price(in_use_app):
    if in_use_app == 'Y':
        total_price = app_use_pizza_price(pizza_number, is_delivery, tuesday)
    else:
        total_price = no_app_use_pizza_price(pizza_number, is_delivery, tuesday)

    output_final_price(pizza_number, round(total_price, 2), use_app, is_delivery, tuesday)


def output_final_price(in_pizza_number, in_total_price, in_app_use, in_delivery, is_tuesday):
    print("\n" + "=" * 70)
    print("********* BPP PIZZA PLACE BILL **************\n")

    print("ORDER".ljust(40) + "PRICE")

    if in_pizza_number > 5:
        # print(f"Pizza({in_pizza_number}) : {12 * in_pizza_number}")
        print(f"*** Quantity discount applied for ordering more than 5 pizzas ****")

    print("=" * 70)

    if is_tuesday == 'Y' and in_app_use == 'Y':
        print('\n*** Both APP and TUESDAY discounts applied ***')

    if in_app_use == 'Y':
        print("\n*** APP DISCOUNT APPLIED *****  ..... 25% OFF")

    if is_tuesday == 'Y':
        print("*** TUESDAY DISCOUNT APPLIED *** .... 50% OFF")

    if in_app_use == 'Y' or is_tuesday == 'Y':
        print(f"\nInitial Price Without Discount:".ljust(40) + f"£{(12 * in_pizza_number) : .2f}")
        print(f"\nTotal Price After Discount:".ljust(40) + f"£{in_total_price : .2f}")
    else:
        print(f"\nInitial Price:".ljust(40) + f"£{(12 * in_pizza_number) : .2f}")
        if in_pizza_number < 5:
            print(f"\nTotal Price After Delivery Charge:".ljust(40) + f"£{in_total_price : .2f}")
        else:
            print(f"\nTotal Price:".ljust(40) + f"£{in_total_price : .2f}")

    if in_delivery == 'Y' and in_pizza_number < 5:
        print()
        print('*** Extra fee of £2.50 is charged for delivery option ***')

    print("=" * 70)


# Print menu and call to take input
menu_for_users()

# User input values returned form take_user_input function
pizza_number, is_delivery, tuesday, use_app = take_user_input()

# Calculate total price
calculate_total_price(use_app)  # This function also calls for bill printing
