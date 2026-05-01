# temperature_converter.py
"""Temperature conversion functions"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

if __name__ == "__main__":
    # Test the functions
    print("=== Temperature Converter ===\n")
    
    # Test 1: Celsius to Fahrenheit
    celsius_temp = 25
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C = {fahrenheit_temp:.2f}°F")
    
    # Test 2: More conversions
    temps_celsius = [0, 10, 20, 30, 100]
    print("\nCelsius → Fahrenheit:")
    for temp in temps_celsius:
        result = celsius_to_fahrenheit(temp)
        print(f"  {temp}°C = {result:.2f}°F")
    
    # Test 3: Fahrenheit to Celsius
    print("\nFahrenheit → Celsius:")
    temps_fahrenheit = [32, 68, 86, 104, 212]
    for temp in temps_fahrenheit:
        result = fahrenheit_to_celsius(temp)
        print(f"  {temp}°F = {result:.2f}°C")