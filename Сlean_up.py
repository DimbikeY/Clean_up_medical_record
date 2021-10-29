medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)
print()
print()
num_records = updated_medical_data.count("$")
print("There are {records} medical records in the data.".format(records = num_records))
#updated_medical_data.strip()
print()
print()
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)
print()
print()
medical_records = []
for element in medical_data_split:
  medical_records.append(element.split(","))
print(medical_records)

medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)


for i in medical_records_clean:
  i[0] = i[0].upper()
  print(i[0])

names = []
ages = []
bmis = []
insurance_costs = []
for num in medical_records_clean:
  names.append(num[0])
  ages.append(num[1])
  bmis.append(num[2])
  insurance_costs.append(num[-1])
print(names)
print(ages)
print(bmis)
print(insurance_costs)


total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
print(total_bmi)

average_bmi = round(total_bmi / len(bmis))
average_bmi = round(average_bmi)
print("Average BMI: {average_bmi}".format(average_bmi = average_bmi))