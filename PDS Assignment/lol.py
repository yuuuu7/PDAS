import numpy as np
import matplotlib.pyplot as plt

#Initialize the contents of the different files into variables first
resale_1990_1999 ='./resale-flat-price-CSVs/resale-flat-prices-based-on-approval-date-1990-1999.csv'


resale_2000_2012 = './resale-flat-price-CSVs/resale-flat-prices-based-on-approval-date-2000-feb-2012.csv'
 
resale_mar2012_dec2014 = './resale-flat-price-CSVs/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv'

resale_jan2015_dec2016 = './resale-flat-price-CSVs/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv'

resale_2017_onwards = './resale-flat-price-CSVs/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv'

#data set 1
data1 = np.genfromtxt(resale_1990_1999, encoding=None, dtype=None, delimiter=',', names=True, usecols=("month", "town", "flat_type", "lease_commence_date", "resale_price"))

rows = len(data1)

print(f"There are all together {rows} rows in the file {resale_1990_1999}")

data1_yflat_months = data1['month']
years_1 = np.unique(data1_yflat_months)
sorted_years_1 = np.sort(years_1)
print(f'\nThere were data captured from {sorted_years_1[0]} to {sorted_years_1[-1]}')

keyword1 = '1 ROOM'
keyword2 = '2 ROOM'
keyword3 = '3 ROOM'
keyword4 = '4 ROOM'
keyword5 = '5 ROOM'
keyword6 = 'EXECUTIVE'
keyword7 = 'MULTI GENERATION'      

data1_1flat = data1[data1['flat_type'] == keyword1]
data1_2flat = data1[data1['flat_type'] == keyword2]
data1_3flat = data1[data1['flat_type'] == keyword3]
data1_4flat = data1[data1['flat_type'] == keyword4]
data1_5flat = data1[data1['flat_type'] == keyword5]
data1_Exec = data1[data1['flat_type'] == keyword6]
data1_7flat = data1[data1['flat_type'] == keyword7] 
print(f'\nThere are a total number of {len(data1_1flat)} {keyword1} resale flats')
print(f'There are a total number of {len(data1_2flat)} {keyword2} resale flats')
print(f'There are a total number of {len(data1_3flat)} {keyword3} resale flats')
print(f'There are a total number of {len(data1_4flat)} {keyword4} resale flats')
print(f'There are a total number of {len(data1_5flat)} {keyword5} resale flats')
print(f'There are a total number of {len(data1_Exec)} {keyword6} resale flats')
print(f'There are a total number of {len(data1_7flat)} {keyword7} resale flats') 
#data set 2
data2 = np.genfromtxt(resale_2000_2012, encoding=None, dtype=None, delimiter=',', names=True, usecols=("month", "town", "flat_type", "lease_commence_date", "resale_price"))

rows = len(data2)

print(f"\nThere are all together {rows} rows in the file {resale_2000_2012}")

data2_yflat_months = data2['month']
years_2 = np.unique(data2_yflat_months)
sorted_years_2 = np.sort(years_2)
print(f'\nThere were data captured from {sorted_years_2[0]} to {sorted_years_2[-1]}')

keyword1 = '1 ROOM'
keyword2 = '2 ROOM'
keyword3 = '3 ROOM'
keyword4 = '4 ROOM'
keyword5 = '5 ROOM'
keyword6 = 'EXECUTIVE'
keyword7 = 'MULTI-GENERATION'

data2_1flat = data2[data2['flat_type'] == keyword1]
data2_2flat = data2[data2['flat_type'] == keyword2]
data2_3flat = data2[data2['flat_type'] == keyword3]
data2_4flat = data2[data2['flat_type'] == keyword4]
data2_5flat = data2[data2['flat_type'] == keyword5]
data2_Exec = data2[data2['flat_type'] == keyword6]
data2_7flat = data2[data2['flat_type'] == keyword7] 

print(f'\nThere are a total number of {len(data2_1flat)} {keyword1} resale flats')
print(f'There are a total number of {len(data2_2flat)} {keyword2} resale flats')
print(f'There are a total number of {len(data2_3flat)} {keyword3} resale flats')
print(f'There are a total number of {len(data2_4flat)} {keyword4} resale flats')
print(f'There are a total number of {len(data2_5flat)} {keyword5} resale flats')
print(f'There are a total number of {len(data2_Exec)} {keyword6} resale flats')
print(f'There are a total number of {len(data2_7flat)} {keyword7} resale flats') 
#data set 3
data3 = np.genfromtxt(resale_mar2012_dec2014, encoding=None, dtype=None, delimiter=',', names=True, usecols=("month", "town", "flat_type", "lease_commence_date", "resale_price"))

rows = len(data3)

print(f"\nThere are all together {rows} rows in the file {resale_mar2012_dec2014}")

data3_yflat_months = data3['month']
years_3 = np.unique(data3_yflat_months)
sorted_years_3 = np.sort(years_3)
print(f'\nThere were data captured from {sorted_years_3[0]} to {sorted_years_3[-1]}')

keyword1 = '1 ROOM'
keyword2 = '2 ROOM'
keyword3 = '3 ROOM'
keyword4 = '4 ROOM'
keyword5 = '5 ROOM'
keyword6 = 'EXECUTIVE'
keyword7 = 'MULTI-GENERATION'

data3_1flat = data3[data3['flat_type'] == keyword1]
data3_2flat = data3[data3['flat_type'] == keyword2]
data3_3flat = data3[data3['flat_type'] == keyword3]
data3_4flat = data3[data3['flat_type'] == keyword4]
data3_5flat = data3[data3['flat_type'] == keyword5]
data3_Exec = data3[data3['flat_type'] == keyword6]
data3_7flat = data3[data3['flat_type'] == keyword7] 

print(f'\nThere are a total number of {len(data3_1flat)} {keyword1} resale flats')
print(f'There are a total number of {len(data3_2flat)} {keyword2} resale flats')
print(f'There are a total number of {len(data3_3flat)} {keyword3} resale flats')
print(f'There are a total number of {len(data3_4flat)} {keyword4} resale flats')
print(f'There are a total number of {len(data3_5flat)} {keyword5} resale flats')
print(f'There are a total number of {len(data3_Exec)} {keyword6} resale flats')
print(f'There are a total number of {len(data3_7flat)} {keyword7} resale flats') 
#data set 4
data4 = np.genfromtxt(resale_jan2015_dec2016, encoding=None, dtype=None, delimiter=',', names=True, usecols=("month", "town", "flat_type", "lease_commence_date", "resale_price"))

rows = len(data4)

print(f"\nThere are all together {rows} rows in the file {resale_jan2015_dec2016}")

data4_yflat_months = data4['month']
years_4 = np.unique(data4_yflat_months)
sorted_years_4 = np.sort(years_4)
print(f'\nThere were data captured from {sorted_years_4[0]} to {sorted_years_4[-1]}')

keyword1 = '1 ROOM'
keyword2 = '2 ROOM'
keyword3 = '3 ROOM'
keyword4 = '4 ROOM'
keyword5 = '5 ROOM'
keyword6 = 'EXECUTIVE'
keyword7 = 'MULTI-GENERATION'

data4_1flat = data4[data4['flat_type'] == keyword1]
data4_2flat = data4[data4['flat_type'] == keyword2]
data4_3flat = data4[data4['flat_type'] == keyword3]
data4_4flat = data4[data4['flat_type'] == keyword4]
data4_5flat = data4[data4['flat_type'] == keyword5]
data4_Exec = data4[data4['flat_type'] == keyword6]
data4_7flat = data4[data4['flat_type'] == keyword7] 

print(f'\nThere are a total number of {len(data4_1flat)} {keyword1} resale flats')
print(f'There are a total number of {len(data4_2flat)} {keyword2} resale flats')
print(f'There are a total number of {len(data4_3flat)} {keyword3} resale flats')
print(f'There are a total number of {len(data4_4flat)} {keyword4} resale flats')
print(f'There are a total number of {len(data4_5flat)} {keyword5} resale flats')
print(f'There are a total number of {len(data4_Exec)} {keyword6} resale flats')
print(f'There are a total number of {len(data4_7flat)} {keyword7} resale flats') 
#data set 5
data5 = np.genfromtxt(resale_2017_onwards, encoding=None, dtype=None, delimiter=',', names=True, usecols=("month", "town", "flat_type", "lease_commence_date", "resale_price"))

rows = len(data5)

print(f"\nThere are all together {rows} rows in the file {resale_2017_onwards}")

data5_yflat_months = data5['month']
years_5 = np.unique(data5_yflat_months)
sorted_years_5 = np.sort(years_5)
print(f'\nThere were data captured from {sorted_years_5[0]} to {sorted_years_5[-1]}')

keyword1 = '1 ROOM'
keyword2 = '2 ROOM'
keyword3 = '3 ROOM'
keyword4 = '4 ROOM'
keyword5 = '5 ROOM'
keyword6 = 'EXECUTIVE'
keyword7 = 'MULTI-GENERATION'

data5_1flat = data5[data5['flat_type'] == keyword1]
data5_2flat = data5[data5['flat_type'] == keyword2]
data5_3flat = data5[data5['flat_type'] == keyword3]
data5_4flat = data5[data5['flat_type'] == keyword4]
data5_5flat = data5[data5['flat_type'] == keyword5]
data5_Exec = data5[data5['flat_type'] == keyword6]
data5_7flat = data5[data5['flat_type'] == keyword7] 


print(f'\nThere are a total number of {len(data5_1flat)} {keyword1} resale flats')
print(f'There are a total number of {len(data5_2flat)} {keyword2} resale flats')
print(f'There are a total number of {len(data5_3flat)} {keyword3} resale flats')
print(f'There are a total number of {len(data5_4flat)} {keyword4} resale flats')
print(f'There are a total number of {len(data5_5flat)} {keyword5} resale flats')
print(f'There are a total number of {len(data5_Exec)} {keyword6} resale flats')
print(f'There are a total number of {len(data5_7flat)} {keyword7} resale flats') 

total_1_room_flat_resale_flats = len(data1_1flat) + len(data2_1flat) + len(data3_1flat) + len(data4_1flat) + len(data5_1flat)
total_2_room_flat_resale_flats = len(data1_2flat) + len(data2_2flat) + len(data3_2flat) + len(data4_2flat) + len(data5_2flat)
total_3_room_flat_resale_flats = len(data1_3flat) + len(data2_3flat) + len(data3_3flat) + len(data4_3flat) + len(data5_3flat)
total_4_room_flat_resale_flats = len(data1_4flat) + len(data2_4flat) + len(data3_4flat) + len(data4_4flat) + len(data5_4flat)
total_5_room_flat_resale_flats = len(data1_5flat) + len(data2_5flat) + len(data3_5flat) + len(data4_5flat) + len(data5_5flat)
total_exec_flat_resale_flats = len(data1_Exec) + len(data2_Exec) + len(data3_Exec) + len(data4_Exec) + len(data5_Exec)


flat_types = ['1-Room', '2-Room','3-Room','4-Room','5-Room','Executive']
resale_counts = [total_1_room_flat_resale_flats,total_2_room_flat_resale_flats,total_3_room_flat_resale_flats,total_4_room_flat_resale_flats,total_5_room_flat_resale_flats,total_exec_flat_resale_flats]

plt.pie(resale_counts, labels=flat_types, autopct='%1.1f%%')
plt.title('Most Popular Resale Flat Types')
plt.show()








