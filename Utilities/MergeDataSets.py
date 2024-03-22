import pandas as pd

class MergeDataSets:
    def __init__(self, data_set1, data_set2, output_file):
        # Read the datasets
        self.defect_df = pd.read_csv(data_set1)
        self.customer_df = pd.read_csv(data_set2)
        
        # Merge the datasets on 'Product ID' and 'Product Version Used'
        self.merged_df = pd.merge(self.defect_df, self.customer_df, 
                                  left_on=['Product ID', 'Version #'], 
                                  right_on=['Product ID', 'Product Version Used'], 
                                  how='inner')

        # Calculate the number of customers impacted by each defect
        self.impact_df = self.merged_df.groupby(['Defect ID', 'Version #']).agg({
            'Cust ID': 'count'
        }).reset_index()

        # Rename the 'Cust ID' column to 'Number of Customers Impacted'
        self.impact_df.rename(columns={'Cust ID': 'Number of Customers Impacted'}, inplace=True)

        # Save the updated defect details to a new CSV file
        self.impact_df.to_csv(output_file, index=False)

    def displayImpact(self):
        print(self.impact_df)
