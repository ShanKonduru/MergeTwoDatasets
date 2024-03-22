import pandas as pd

# Read the datasets
defect_df = pd.read_csv('datasets/defect_details.csv')
customer_df = pd.read_csv('datasets/customer_details.csv')

# Merge the datasets on 'Product ID' and 'Product Version Used'
merged_df = pd.merge(defect_df, customer_df, left_on=['Product ID', 'Version #'], 
                     right_on=['Product ID', 'Product Version Used'], how='inner')

# Calculate the number of customers impacted by each defect
impact_df = merged_df.groupby(['Defect ID', 'Version #']).agg({
    'Cust ID': 'count'
}).reset_index()

# Rename the 'Cust ID' column to 'Number of Customers Impacted'
impact_df.rename(columns={'Cust ID': 'Number of Customers Impacted'}, inplace=True)

# Save the updated defect details to a new CSV file
impact_df.to_csv('datasets/updated_defect_details.csv', index=False)

print(impact_df)
