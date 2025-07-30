import pandas as pd

# Load dataset
df = pd.read_csv('data/netflix_titles.csv')

# Convert 'date_added' to datetime, ignoring errors
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Drop rows with missing 'date_added'
df = df.dropna(subset=['date_added'])

# Group by month and count shows added
monthly_counts = df.groupby(pd.Grouper(key='date_added', freq='M')).size().reset_index(name='shows_added')

# Create mock MRR by multiplying shows_added by 1000
monthly_counts['mrr'] = monthly_counts['shows_added'] * 1000

# Use shows_added * 10 as proxy for active users
monthly_counts['active_users'] = monthly_counts['shows_added'] * 10

# Rename columns
monthly_counts = monthly_counts.rename(columns={'date_added': 'date'})

# Save processed data to CSV
monthly_counts.to_csv('data/processed_netflix.csv', index=False)

print("Processed Netflix data saved to data/processed_netflix.csv")
