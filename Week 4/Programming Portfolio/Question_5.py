def centigrade_to_fahrenheit(temperature):
    temperature = float(temperature)
    fahrenheit = (temperature * 1.8) + 32
    result = f"{temperature: .2f} Centigrade is equivalent to {fahrenheit: .2f} Fahrenheit"
    return result


def fahrenheit_to_centigrade(temperature):
    temperature = float(temperature)
    centigrade = (temperature - 32) / 1.8
    result = f"{temperature: .2f} Fahrenheit is equivalent to {centigrade: .2f} Centigrade"
    return result


print(centigrade_to_fahrenheit(35))
print(fahrenheit_to_centigrade(96))
