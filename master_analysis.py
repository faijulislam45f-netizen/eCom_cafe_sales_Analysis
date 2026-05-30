#file2
import pandas as pd

#loading clean_dataset 
df = pd.read_csv("clean_dataset.csv")
print("="*45)
print("FINAL CLIENT ANALYTICS REPORT")
print("="*45)
print(f"Total Records: {len(df)}")

#step1 country wise
print("n1. TOP COUNTRIES:")
print(df['Country'].value_counts().head(5))

#step2 developer types
print("\n2. DEVELOPER TYPES:")
print(df['MainBranch'].value_counts())

#step3 language popularity
print("\n3. TOP LANGUAGE:")
languages = df['LanguageWorkedWith'].dropna().str.split(';').explode()
lang_count = languages.value_counts().head(5)
lang_df = pd.DataFrame({
    'Votes': lang_count, 
    'Market Share (%)':round(lang_count / len(df) * 100, 1)
})
print(lang_df)


#step4 salaries analysis
salary = pd.to_numeric(df['ConvertedComp'], errors='coerce').dropna()
print("\n4. SALARY ANALYSIS (Clean Data):")
print(f"Average Salary: ${round(salary.mean(), 2)}")
print(f"Median Salary:  ${salary.median()}")
print(f"Max Salary:     ${salary.max()}")
print("="*45)