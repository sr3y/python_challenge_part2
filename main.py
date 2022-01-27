import csv
import json
import os
import pickle
import json.decoder


# A: processes all inputs and returns in a list
def check_input(name_in, birthday_in, age_in, email_in, password_in):
    """processes all inputs and returns in a list"""
    names = name_in.split()
    for item in names:
        if not item.isalpha():
            print("\ninvalid name")
            return
    date = birthday_in.split()
    num_date = []
    for item in date:
        if not item.isnumeric():
            print("\ninvalid birthday")
            return
        else:
            num_date.append(int(item))

    year = num_date[2]

    if year < 1917 or year > 2015:
        print(year)
        print("\ninvalid birthday")
        return

    if not age_in.isnumeric():
        print("\ninvalid age")
        return

    char = email_in.find("@")
    if char == -1:
        print("\ninvalid email")
        return

    return name_in.title(), num_date, int(age_in), email_in, password_in

# C: returns data from csv file
def return_users_csv():
    """returns data from csv file"""

    stored_data = []
    with open('csv_file.csv', 'r') as file:
        reader = csv.reader(file)
        print(next(reader))
        for row in reader:
            stored_data.append(row)
        file.close()
        return stored_data

# P: returns data from pickle file
def return_users_pickle():
    """returns data from pickle file"""

    stored_data = []
    with open('pickle_file.pickle', 'rb') as file:
        try:
            while True:
                stored_data.append(pickle.load(file))
        except EOFError:
            pass
            file.close()
    return stored_data

# J: returns data from json file
def return_users_json():
    """returns data from json file"""
    data_j = []
    if os.stat("storage.json").st_size != 0:
        with open("storage.json", "r") as file_j:
            try:
                print("opening")
                data_j = json.load(file_j)
                print("no errors yet...")
                print(data_j)
            except json.decoder.JSONDecodeError:
                print("error accepted")
                pass
        file_j.close()
    return data_j

print(return_users_json())

# A: collect input from user
name = input("name: ")
birthday = input("birthday (mm dd yyyy): ")
age = input("age: ")
email = input("email: ")
password = input("password: ")

# C: creates a titles for csv file data
header = ["name", "birthday", "age", "email", "password"]
# A: stores the processed data as list
more_data = check_input(name, birthday, age, email, password)

# A: creating files:
data = []
if os.stat("csv_file.csv").st_size == 0:
    with open('csv_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
        f.close()

# A: if data meets requirements, the data is stored
if more_data is not None:
    print("more data returns a value ")
    with open("storage.json", "w") as file:
        print("dumping content from json into b")
        b = return_users_json()
        print("appending values from more data to b")
        print(b)
        b.append(more_data)
        print(b)
        print("dumping b")
        json.dump(more_data, file)
        file.close()

    with open('csv_file.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(more_data)
        f.close()
    with open('pickle_file.pickle', 'ab+') as f:
        pickle.dump(more_data, f)

#print(return_users_pickle())
print(return_users_json())


