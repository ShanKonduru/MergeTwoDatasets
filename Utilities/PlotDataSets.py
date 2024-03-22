import pandas as pd
import matplotlib.pyplot as plt

class PlotDataSets:
    def __init__(self, output_data= 'datasets/updated_defect_details.csv'):
        # Read the updated defect details dataset
        self.impact_df = pd.read_csv(output_data)

    def loadData(self):
        # Define the data for the bubble chart
        defect_ids = self.impact_df['Defect ID']
        impacted_customers = self.impact_df['Number of Customers Impacted']
        versions = self.impact_df['Version #']

        # Define colors for different versions
        colors = {'V1': 'blue', 'V2': 'green'}  # You can add more colors for additional versions

        # Map versions to colors
        version_colors = [colors[version] for version in versions]

        # Plot the bubble chart
        plt.figure(figsize=(12, 8))
        plt.scatter(defect_ids, impacted_customers, s=impacted_customers*50, c=version_colors, alpha=0.5, edgecolors="black", linewidth=2)

        # Add labels and title
        plt.title('Defect Impact Bubble Chart')
        plt.xlabel('Defect ID')
        plt.ylabel('Number of Customers Impacted')

        # Add legend for versions
        legend_labels = [plt.Line2D([0], [0], marker='o', color=color, label=version, markersize=10) for version, color in colors.items()]
        plt.legend(handles=legend_labels, title='Version', loc='upper right')

        # Show the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()