def main():
    print("===ECo-smart Irrigation system ===")
    print("Company: QuantumLeaf\n")

    weather = input("enter the weather condition (Raining/Sunny/cloud): ").strip().capitalize()
    try:
        moisture = float(input("enter the soil moisture level (0-100): "))
    except ValueError:
        print("Invalid input. Try again.\n")
        return
    
    if moisture < 0 or moisture > 100:
        print("moisture level must be between 0 and 100.")
        return
     
    if weather == "Raining":
        status = "standby"

    elif weather == "Sunny" and moisture < 30:
        status = "Active"

    elif weather == "Cloudy"and moisture <10:
        status = "ACtive"

    else:
        status = "standby"

    print(f"\nQuantumLeaf Irrigation status:  {status}")

if __name__ == "__main__":
    main()