import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('clean_dataset.csv')

#graph1-- language popularity
languages = df['LanguageWorkedWith'].dropna().str.split(';').explode()
lang_count = languages.value_counts().head(8)

plt.figure(figsize=(10, 6))
lang_count.plot(kind='bar', color='steelblue')
plt.title('Top Programming Language')
plt.xlabel('Language')
plt.ylabel('Number Of Developers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('languages.png')
plt.close()
print("language.png file is saved in my directory!")

#graph2-- salary distribution
salary = pd.to_numeric(df['ConvertedComp'], errors='coerce').dropna()

plt.figure(figsize=(10, 6))
plt.hist(salary, bins=10, color='green', edgecolor='black')
plt.title('Salary Distribution (Cleaned Data)')
plt.xlabel('Salary (USD)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('salary.png')
plt.close()
print("salary.png saved")
