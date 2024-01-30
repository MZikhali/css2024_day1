# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:10:15 2024

@author: zical
"""

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[11])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)


gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[-2])
print(gender[-5])


# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)
my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))
print(my_list[0:3]
# View a certain range of items:
print(my_list[0:3]

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
(person['phone']) = '555-555-5555'
print(person['phone'])


data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
print(df[df['age'] > 30])
print(df[1:4])


# Adding a new column
df['new_time'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_time'], inplace=True)
df.drop(columns=['new_column'], inplace=True)

age = [30 , 25 , 29 , 46 , 22]

print(age)

print(age[1])

print(max(age))

print(min(age))

print(len(age))

average = sum(age)/len(age)

print(average)



