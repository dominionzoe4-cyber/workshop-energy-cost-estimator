# CTE213 PROJECT
# WORKSHOP ENERGY COST ESTIMATOR
# Name: Onyekwere Zoe Kosiobabire
# Department: Mechatronics Engineering
# Institution: YABATECH
# Class: ND2

def calc_kwh(power, hours):
    return (power / 1000) * hours


def calc_cost(kwh, tariff):
    return kwh * tariff


def energy_saving_status(power):
    if power > 1500:
        return "HIGH POWER - PLC timer recommended"
    elif power > 800:
        return "MEDIUM POWER - Timer recommended"
    else:
        return "LOW POWER - Normal operation"


# Illustrative machine ratings. Check each machine's nameplate
# and replace these estimates with its actual rated power.
machines = {
    1: ("Lathe Machine", 3000),
    2: ("Milling Machine", 4000),
    3: ("Drilling Machine", 1500),
    4: ("Grinding Machine", 2000),
    5: ("Welding Machine", 5000),
    6: ("Air Compressor", 3000),
    7: ("Electric Motor", 1500),
    8: ("Hydraulic Press", 7500),
    9: ("Bench Grinder", 750),
    10: ("CNC Machine", 6000),
    11: ("Power Saw", 2000),
    12: ("Conveyor Belt", 1000)
}


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=" * 55)
    print("          WORKSHOP ENERGY COST ESTIMATOR")
    print("=" * 55)
    print("Developed by: Onyekwere Zoe Kosiobabire")
    print("Department: Mechatronics Engineering")
    print("Institution: YABATECH | Class: ND2")
    print("=" * 55)

    print("\nAVAILABLE WORKSHOP MACHINES")
    for number, (name, power) in machines.items():
        print(f"{number:2}. {name} - {power} W")

    while True:
        try:
            quantity = int(input("\nHow many different machines do you want to calculate? "))
            if 1 <= quantity <= len(machines):
                break
            print(f"Enter a number from 1 to {len(machines)}.")
        except ValueError:
            print("Please enter a whole number.")

    selected_machines = []
    selected_numbers = set()

    for index in range(quantity):
        while True:
            try:
                choice = int(input(f"\nSelect machine {index + 1} by number: "))
                if choice not in machines:
                    print("Invalid selection. Choose a number from the list.")
                elif choice in selected_numbers:
                    print("You have already selected that machine. Choose another.")
                else:
                    break
            except ValueError:
                print("Please enter a whole number.")

        name, power = machines[choice]

        while True:
            hours = get_positive_float(
                f"Enter daily operating hours for {name} (maximum 24): "
            )
            if hours <= 24:
                break
            print("Operating hours cannot exceed 24 per day.")

        energy = calc_kwh(power, hours)
        selected_machines.append({
            "name": name,
            "power": power,
            "hours": hours,
            "kwh": energy
        })
        selected_numbers.add(choice)
        print(f"{name} added successfully.")

    tariff = get_positive_float("\nEnter electricity tariff per kWh (Naira): ")

    total_kwh = sum(machine["kwh"] for machine in selected_machines)
    total_daily_cost = calc_cost(total_kwh, tariff)
    monthly_kwh = total_kwh * 30
    monthly_cost = monthly_kwh * tariff

    print("\n" + "=" * 55)
    print("                 WORKSHOP ENERGY REPORT")
    print("=" * 55)

    for machine in selected_machines:
        daily_cost = calc_cost(machine["kwh"], tariff)
        print(f"\nMachine: {machine['name']}")
        print(f"Power rating: {machine['power']:.0f} W")
        print(f"Operating time: {machine['hours']:.2f} hours/day")
        print(f"Daily energy: {machine['kwh']:.2f} kWh")
        print(f"Daily cost: N{daily_cost:,.2f}")
        print(f"Monthly cost (30 days): N{daily_cost * 30:,.2f}")

    highest = max(selected_machines, key=lambda item: item["kwh"])
    high_power_count = sum(
        1 for machine in selected_machines if machine["power"] > 1000
    )

    print("\n--- TOTAL ENERGY CONSUMPTION ---")
    print(f"Total daily energy: {total_kwh:.2f} kWh")
    print(f"Total daily cost: N{total_daily_cost:,.2f}")
    print(f"Total monthly energy (30 days): {monthly_kwh:.2f} kWh")
    print(f"Total monthly cost: N{monthly_cost:,.2f}")

    print("\n--- ENERGY ANALYSIS ---")
    print(f"Highest energy-consuming machine: {highest['name']}")
    print(f"Energy consumed: {highest['kwh']:.2f} kWh")
    print(f"Machines above 1000 W: {high_power_count}")

    if total_kwh > 20:
        print("Workshop status: HIGH ENERGY CONSUMPTION")
    elif total_kwh > 10:
        print("Workshop status: MEDIUM ENERGY CONSUMPTION")
    else:
        print("Workshop status: LOW ENERGY CONSUMPTION")

    print("\n--- PLC ENERGY-SAVING ANALYSIS ---")
    for machine in selected_machines:
        print(
            f"{machine['name']}: "
            f"{energy_saving_status(machine['power'])}"
        )

    print("\nRECOMMENDATION")
    print("Consider PLC timers and suitable operating schedules to")
    print("reduce unnecessary machine running time.")
    print("This program provides recommendations; it does not control")
    print("a physical PLC or switch machines off automatically.")

    print("\nNote: Machine power ratings are illustrative estimates.")
    print("Check the actual machine nameplates for accurate results.")
    print("=" * 55)
    print("       THANK YOU FOR USING THIS PROGRAM")
    print("=" * 55)


if __name__ == "__main__":
    main()
