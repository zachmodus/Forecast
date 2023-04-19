import pandas as pd

# Replace `your_file_path.csv` with the actual path to your CSV file
file_path = 'C:\\Users\\zacha\\PycharmProjects\\Forecast\\Needswork.csv'

# Load the data from the CSV file
df = pd.read_csv(file_path)

# Replace `start_date` and `end_date` with the dates you want to cut from your data
start_date = '2021-09-02'
end_date = '2022-05-31'

# Convert the DATE column to a datetime data type
df['DATE'] = pd.to_datetime(df['DATE'])

# Filter the data to include only rows between `start_date` and `end_date`
df = df[(df['DATE'] >= start_date) & (df['DATE'] < end_date)]

# Save the filtered data to a new CSV file
updated_file_name = file_path[:-4] + '_updated.csv'  # Create a new file name
df.to_csv(updated_file_name, index=False)  # Save the data to the new file

# Print a confirmation message
print(f"Filtered data saved to {updated_file_name}")
