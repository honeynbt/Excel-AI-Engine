
# Generate synthetic structured data with 1000 rows and 10 columns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate 1000 rows of structured data
num_rows = 1000

# Create structured dataset
structured_data = {
    'employee_id': range(1, num_rows + 1),
    'name': [f'Employee_{i}' for i in range(1, num_rows + 1)],
    'department': np.random.choice(['Sales', 'Engineering', 'Marketing', 'HR', 'Finance'], num_rows),
    'age': np.random.randint(22, 65, num_rows),
    'salary': np.random.randint(30000, 150000, num_rows),
    'years_experience': np.random.randint(0, 40, num_rows),
    'performance_score': np.random.uniform(1.0, 5.0, num_rows).round(2),
    'projects_completed': np.random.randint(0, 50, num_rows),
    'hire_date': [datetime(2015, 1, 1) + timedelta(days=random.randint(0, 3650)) for _ in range(num_rows)],
    'is_manager': np.random.choice([True, False], num_rows, p=[0.15, 0.85])
}

df_structured = pd.DataFrame(structured_data)

print("Structured Data Sample:")
print(df_structured.head(10))
print(f"\nShape: {df_structured.shape}")
print(f"Data types:\n{df_structured.dtypes}")
print("\nStatistics:")
print(df_structured.describe())

# Save to CSV for later use
df_structured.to_csv('structured_data.csv', index=False)
print("\n✓ Structured data saved to structured_data.csv")
