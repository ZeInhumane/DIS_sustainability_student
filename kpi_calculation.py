import pandas as pd
from utility.functions import calculate_carbon

# read and load the necessary excel file 
df_building = pd.read_excel("store/output/clean_data.xlsx")
df_basic = pd.read_excel("store/input/basic_data.xlsx")

# set "tab" as index for easier checking with the "codes" 
df_basic.set_index("tab", inplace=True)
data_basic = df_basic.to_dict(orient="index")

# read the "power" sheet from the Excel file and load it into df_intensity dataframe
df_intensity = pd.read_excel("store/input/basic_data.xlsx", sheet_name='power')

# set the "year" column as the index for df_intensity to make it easier to access data by year.
# TODO: write your code here

# convert the df_intensity DataFrame to a dictionary with the "year" values as keys.
data_intensity = # TODO: write your code here

# To update the df_building by adding "EUI", "WEI" and "carbon_index" column
# iterate through each row of df_building to calculate the value of each kpi
# insert the calculated value at the specified index row by row  
for index, row in df_building.iterrows():

    # get the building code for the current row
    # TODO: write your code here

    # get the corresponding data of the code in the data_basic
    data_building = # TODO: write your code here

    # check if the data exists
    # use the respective data to calculate EUI, WEI and carbon emissions
    if data_building:
        # Calculate EUI
        df_building.at[index, 'EUI'] = row['energy'] / data_building['gfa']

        # assume that the number of staff per m^2 is 9.2 
        # assume that the number of visitors is 10% of the staff 
        # Calculate WEI
        estimated_staff = data_building['gfa'] / 9.2
        estimated_visitors = 0.10 * estimated_staff
        df_building.at[index, 'WEI_Area'] = row['water'] / data_building['gfa']
        df_building.at[index, 'WEI_People'] = row['water'] * 1000 / (estimated_staff + 0.25 * estimated_visitors) / row['working_day']

        # calculate carbon energy and water by using the 'calculate_carbon' function import from utility
        # TODO: write your code here for carbon energy
        # TODO: write your code here for carbon water
        df_building.at[index, 'carbon_index'] = (df_building.at[index, 'carbon_water'] + df_building.at[index, 'carbon_energy']) / data_building['gfa'] / (estimated_staff 
                                                                                                                                                           + 0.25 * estimated_visitors) * 10000
        
output_file_path = 'store/output/clean_data.xlsx'
# Save the dataframe to an Excel file with specified path 
# TODO: write your code here
