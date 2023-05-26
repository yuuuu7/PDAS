import numpy as np

#12 File I/O on Numpy arrays

### Read the csv file using genfromtxt
filename = "singapore-residents-by-ethnic-group-and-sex-end-june-annual.csv"

data = np.genfromtxt(filename, dtype=['i2', 'U50', 'i8'], delimiter=',', names=True)
total_rows = len(data)

### Print out total rows of data in the file
print(f'There are altogether {total_rows} rows in the data file')

### Print out the number of years of data captured
data_years = data['year']
years = np.unique(data_years)
sorted_years = np.sort(years)
print(f'There are {len(years)} years of data captured from {sorted_years[0]} to {sorted_years[-1]}')
print()

## Extract only the rows with Total Residents" - using boolean indexing
keyword = 'Total Residents'
data_totalresidents = data[data['level_1'] == keyword]
#print(data_totalresidents)

### Print out the years which has the highest total number of residents
max_residents = data_totalresidents['value'].max()
argmax_residents = data_totalresidents['value'].argmax()
relevant_year = data_totalresidents[argmax_residents]['year']
print(f'Year with the highest total number of residents: {relevant_year}')
print(f'Population Count: { max_residents } ')

### Print out the years which has the lowest total number of residents
min_residents = data_totalresidents['value'].min()
argmin_residents = data_totalresidents['value'].argmin()
relevant_year = data_totalresidents[argmin_residents]['year']
print(f'\nYear with the lowest total number of residents: {relevant_year}')
print(f'Population Count: { min_residents } ')