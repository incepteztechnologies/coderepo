import os
import pandas as pd
print("=== Employee Salary Processing ===")

# Read input file from local file system
input_file = "data/employees.csv"

df = pd.read_csv(input_file)

print("\nInput Employee Data:")
print(df)

# Calculate annual salary
df["annual_salary"] = df["salary"] * 12

# Calculate 10% bonus for salary >= 70000
df["bonus"] = df["salary"].apply(
    lambda salary: salary * 0.10 if salary >= 70000 else 0
)

print("\nProcessed Employee Data:")
print(df)

# Create output directory
os.makedirs("output", exist_ok=True)

# Write processed data to local file system
output_file = "output/employee_salary_report.csv"

df.to_csv(output_file, index=False)

print(f"\nReport created: {output_file}")

# Verify output file
assert os.path.exists(output_file)

print("Employee salary processing completed successfully.")