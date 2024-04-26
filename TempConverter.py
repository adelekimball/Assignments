##This defines my input and output variables. 
def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)

    print("Temperature in Celsius:", celsius)

##this is the converter. It uses the python syntax for the subtraction and division.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

#Prompts user to enter in variables from "main" when script is run directly
if __name__ == "__main__":
    main()