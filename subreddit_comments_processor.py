import pandas as pd

# Load the Excel file containing the "id" and "permalink" columns
df = pd.read_excel(r'file_path.xlsx')

# Ensure there are no missing values in the permalink column
df = df.dropna(subset=['permalink'])

# Extract the subreddit from each permalink and create a new column for it
def extract_subreddit(permalink):
    try:
        return permalink.split('/r/')[1].split('/')[0]
    except IndexError:
        return None

df['subreddit'] = df['permalink'].apply(extract_subreddit)

# Drop rows where subreddit extraction failed
df = df.dropna(subset=['subreddit'])

# Group by subreddit
grouped = df.groupby('subreddit')

# Create a dictionary to hold the data for the new format
data = {'Subreddit': [], 'Posts': []}

for subreddit, group in grouped:
    data['Subreddit'].append(subreddit)
    data['Posts'].append(', '.join(group['permalink'].tolist()))

# Create a DataFrame from the dictionary
new_df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
new_df.to_excel('Saved_comments.xlsx', index=False)

print("Subreddits and their posts saved to 'Saved_comments.xlsx'")