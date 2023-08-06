def get_user_input():
    while True:
        weight_input = input("Enter your weight in kilograms: ")
        height_input = input("Enter your height in meters: ")

        if weight_input and height_input:
            try:
                weight = float(weight_input)
                height = float(height_input)
                return weight, height
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and height.")
        else:
            print("Please enter valid values for weight and height.")

def calculate_BMI(weight, height):
    BMI = weight / ((height / 100) ** 2)
    return BMI

def classify_BMI(BMI):
        if BMI < 18.5:
            return "You are Under Weight"
        elif 18.5 <= BMI < 24.9:
            return "Normal Weight"
        elif 25 <= BMI < 29.9:
            return "Over Weight"
        else:
            return "You have Obesity"

def main():
        W, H = get_user_input()
        print(f"weight: {W:.2f} kg")
        print(f"height: {H:.2f} cm")
        BMI = calculate_BMI(W, H)
        print(f"Your BMI is :{BMI:.2f}")
        Categories = classify_BMI(BMI)
        print(f"Category: {Categories}")

main()

