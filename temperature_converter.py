def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)

def convert_temperature(temperature: float, unit: str):
    unit = unit.upper()  # Accept 'c' or 'f' (case-insensitive)
    if unit == 'C':
        return f"{temperature}°C is {celsius_to_fahrenheit(temperature)}°F"
    elif unit == 'F':
        return f"{temperature}°F is {fahrenheit_to_celsius(temperature)}°C"
    else:
        return "Please input the correct unit: 'C' for Celsius or 'F' for Fahrenheit"

# --- CLI Entry Point ---
def main():
    print("🌡️ Temperature Converter")
    
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ")
        result = convert_temperature(temp, unit)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number for temperature.")

if __name__ == "__main__":
    main()
