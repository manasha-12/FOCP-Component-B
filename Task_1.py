print("""BPP Pizza Prize Calculator
===========================""")


def take_user_input():
    while True:
        try:
            pizza_quantity = int(input('How many pizzas ordered? '))
            if pizza_quantity > 0:
                break
            else:
                print('Please enter a positive number')
        except ValueError or TypeError:
            print('Please enter a valid number!')

    while True:
        try:
            delivery_requirement = input('Is delivery required? (Y/N) ').upper()
            if delivery_requirement in ['N', 'Y']:
                break
            else:
                print("Please answer 'Y' or 'N'")
        except ValueError:
            print("Please answer 'Y' or 'N'")

    while True:
        try:
            day_discount = input('Is it Tuesday? (Y/N) ').upper()
            if day_discount in ['N', 'Y']:
                break
            else:
                print("Please answer 'Y' or 'N'")
        except ValueError:
            print("Please answer 'Y' or 'N'")

    while True:
        try:
            app_use = input('Did the customer use the app? (Y/N) ').upper()
            if app_use in ['N', 'Y']:
                break
            else:
                print("Please answer 'Y' or 'N'")
        except ValueError:
            print("Please answer 'Y' or 'N'")

    return pizza_quantity, delivery_requirement, day_discount, app_use


# conditions for calculation
pizza_number, is_delivery, tuesday, use_app = take_user_input()


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
        price = (pizza_number * 12) * (1 - 0.25)
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

    output_final_price(pizza_number, round(total_price, 2))


def output_final_price(in_pizza_number, total_calculated_price):
    print(f"""
Price per Pizza : £12.00    Pizza Quantity : {in_pizza_number}
Total Price : £{total_calculated_price : .2f}""")


# function call
calculate_total_price(use_app)
