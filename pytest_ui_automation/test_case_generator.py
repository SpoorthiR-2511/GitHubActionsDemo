from scenario_library import SCENARIOS

with open("generated_test_cases.txt", "w") as file:

    for requirement, scenarios in SCENARIOS.items():

        file.write(f"\nRequirement: {requirement}\n")
        file.write("-" * 50 + "\n")

        for i, scenario in enumerate(scenarios, start=1):

            file.write(
                f"TC_{i:03} : {scenario}\n"
            )

print("Test Cases Generated Successfully")