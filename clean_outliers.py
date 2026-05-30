import pandas as pd
import numpy as np

print("Data is currently loading...")
df = pd.read_csv('survey_results_public.csv')

#step1 unnecessary column drop
df = df.drop(columns=['Sexuality', 'Ethnicity', 
                      'CodeRevHRS', 'BlockchainOrg', 
                      'BlockchainIs'], errors='ignore')

#step2 nulls handling
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['DevType'] = df['DevType'].fillna('Unknown')

#step3 salary outliers analysis
salary_data = pd.to_numeric(df['ConvertedComp'], errors='coerce').dropna()

print(f"Total Salaries: {len(salary_data)}")
print(f"Max Salary: ${salary_data.max()}")
print(f"Average Salary: ${round(salary_data.mean(), 2)}")

Q1 = salary_data.quantile(0.25)
Q3 = salary_data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = max(0,Q1 - 1.5 * IQR)
upper_bound = Q3 + 1.5 * IQR

print(f"\nStatistical Boundaries:")
print(f" Lower Limit: ${round(lower_bound, 2)}")
print(f" Upper Limit: ${round(upper_bound, 2)}")

outliers = salary_data[(salary_data < lower_bound) | (salary_data > upper_bound)]
clean_salaries = salary_data[(salary_data > lower_bound) & (salary_data < upper_bound)]
print(f"\nTotal outliers found: {len(outliers)}")
if not outliers.empty:
    print("Outlier values (unusual, not necessarily fake):")
    outliers_rows = df[df['ConvertedComp'].isin(outliers)].copy()
    outliers_rows['DevType'] = outliers_rows['DevType'].str[:30]
    print(outliers_rows[['Country', 'DevType', 'ConvertedComp']].to_string())

print("\n" + "="*45)
print("SALARY ANALYSIS REPORT")
print("="*45)
print(f"With Outliers Avg:   ${round(salary_data.mean(), 2)}")
print(f"Without Outliers Avg:${round(clean_salaries.mean(), 2)}")
print(f"Median:              ${clean_salaries.median()}")
print(f"Max Salary:          ${clean_salaries.max()}")
print("="*45)
df = df[(pd.to_numeric(df['ConvertedComp'], errors='coerce') <= upper_bound) | 
        (df['ConvertedComp'].isna())]
print("Note: Outliers Unusual, Not Necessarily Fake!")

#step4 save this file with clean_dataset.csv file
df.to_csv('clean_dataset.csv', index=False)
print("\nclean_dataset.csv file saved")
print(f"Final shape: {df.shape}")