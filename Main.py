from Utilities.MergeDataSets import MergeDataSets
from Utilities.PlotDataSets import PlotDataSets

set_1 = 'datasets/defect_details.csv'
set_2 = 'datasets/customer_details.csv' 
output = 'datasets/updated_defect_details.csv'

# Create an instance of the MergeDataSets class
merge_data = MergeDataSets(data_set1=set_1, data_set2=set_2, output_file=output)

# Display the updated defect details
merge_data.displayImpact()

# Create an instance of the PlotDataSets class
plot_merged_data = PlotDataSets()

# Load the data and plot the bubble chart
plot_merged_data.loadData()
