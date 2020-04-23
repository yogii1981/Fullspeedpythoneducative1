from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# convert the date:
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

# create a loop to  over moma rows
ages = []
for row in moma:
    birth = row[3]
    date = row[6]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
print(row[:])

print(birth_date)
print(death_date)
print(date)
