import subprocess
print("Step 1: Cleaning...")
subprocess.run(['python3', 'clean_outliers.py'])
print("\nStep 2: Analysis...")
subprocess.run(['python3', 'master_analysis.py'])