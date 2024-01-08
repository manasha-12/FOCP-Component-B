def conversion():
    user_input = str(input("Enter temperature: ")).lower()
    if "c" in user_input:
        temperature_list = [user_input]
        separated_list = [i for i in temperature_list[0]]
        separated_list[-1:] = []
        joined_list = "".join(separated_list)
        temperature = float(joined_list)
        fahrenheit = (temperature * 1.8) + 32
        result = f"{temperature: .2f}C is equivalent to {fahrenheit}F"
        return result
    else:
        result = "Enter temperature in Celsius!"
        return result


print(conversion())