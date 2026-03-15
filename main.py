import pandas as pd


def calculate_benefits(row):
    salary = row['Salary']
    years = row['Years']
    
    # Pension Logic (Minimum 10 years service)
    monthly_pension = (salary * years) / 70 if years >= 10 else 0
    
    # Gratuity Logic (Minimum 5 years service)
    total_gratuity = (15 * salary * years) / 26 if years >= 5 else 0
    
    return pd.Series([round(monthly_pension, 2), round(total_gratuity, 2)])

try:
    df = pd.read_csv('employees.csv')
    print("Successfully loaded employee data...")

    df[['Calculated_Pension', 'Calculated_Gratuity']] = df.apply(calculate_benefits, axis=1)


    print("\n--- Pension Calculation Results ---")
    print(df)

    df.to_csv('processed_pensions.csv', index=False)
    print("\nResults saved to 'processed_pensions.csv'!")

except FileNotFoundError:
    print("Error: 'employees.csv' not found. Please create the file first.")