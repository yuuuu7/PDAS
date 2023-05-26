import numpy as np


#5. Manupilating Array Shapes

#Task 1
a = np.arange(15,30)

new_shape = [3,5]
lol = np.reshape(a, new_shape)


print(lol)

#Task 2

#a
a = np.array([ ['Mary', 'John','Bob'],
['Zoe', 'Chris','Ann'],
['Leon', 'Kathy','Sam']])

flattened_array = a.flatten()

print(flattened_array)

#b
b = np.array([ [1,2,3,4,5,6], [7,8,9,10,11,12]])

new_shape = [3,4]

new_array = np.reshape(b, new_shape)

print(new_array)

#Task 3
a = np.array([ [1,2,3,4,5,6], [7,8,9,10,11,12]])

lol = a.transpose()

print(lol)

#6 Manupilating Array Content

#Task 2

#a
x = np.arange(100)

sub_arrays = np.array_split(x, 20)

print(sub_arrays)

#b
x = np.arange(100)

interval = [10,25,45,75,95]

lol = np.split(x, interval)

print(lol)

#7. Copying Arrays

x = np.array([1, 2, 3])
y = x
z = np.copy(x)

print(y)
print(z) 

#8. Sorting Arrays

#a
arr_1 = np.random.randint(100,200,10)

sorted_arr = np.sort(arr_1)

print(sorted_arr)

#b
arr_2 = np.random.randint(1,20,(3,5))

sorted_array_2 = np.sort(arr_2, axis=0)

print(sorted_array_2)

#c
arr_3 = np.random.randint(100,200,(2,5))

arr_3_copy = arr_3.copy()

print(np.sort(arr_3_copy, axis=1)) 

#9. Subsettings and Indexing
a = np.array((np.arange(0,10),
np.arange(10,20),
np.arange(20,30),
np.arange(30,40)))

b = np.random.randint(100,200,(3,3))

#a
even_numbers = a[a%2==0]

print(even_numbers)

#b
greater_than_150 = b[b > 150]

print(greater_than_150)

#Task 3

b = np.arange(9.).reshape(3, 3)
b5 = np.where( b > 5 )

print(b5)
for row, col in zip(b5[0], b5[1]):
    print(f"Value: {b[row, col]} in row {row} and column {col}")


#11. Statistical Methods

a = np.array((np.arange(0,10),
np.arange(10,20),
np.arange(20,30),
np.arange(30,40)))

#a
print("Sum of all Numbers is: ", np.sum(a))

#b
print("The mean is: ", np.mean(a))

#c
row_sums = np.sum(a, axis=1)

for i, row_sum in enumerate(row_sums, start=1):
    print(f"Row {i} sum: {row_sum}")


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