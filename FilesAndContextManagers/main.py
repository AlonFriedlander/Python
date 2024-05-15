# class FileStream:
#     def __init__(self,path, mode):
#         self.path = path
#         self.mode = mode
#
#     def __enter__(self):
#         self.filestream = open(self.path, self.mode)
#         return self.filestream
#
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         self.filestream.close()




# from contextlib import contextmanager

# @contextmanager
# def filestream(path,mode):
#     f = open(path, mode)
#     yield f
#     f.close()
#
# with filestream("file.txt","w") as file:
#     file.write("hello world!")
#
# print(file.closed)


# import string
# import os

# def generate_files():
#     # Generate file names from A.txt to Z.txt
#     file_names = [f"{letter}.txt" for letter in string.ascii_uppercase]
#
#     # Write the name of the letter to each file
#     for file_name, letter in zip(file_names, string.ascii_uppercase):
#         with open(file_name, 'w') as file:
#             file.write(letter)
#
# def delete_files():
#     # Generate file names from A.txt to Z.txt
#     file_names = [f"{letter}.txt" for letter in string.ascii_uppercase]
#
#     # Delete each file
#     for file_name in file_names:
#         os.remove(file_name)
#
# if __name__ == "__main__":
#     generate_files()
#     delete_files()

# def read_first_n_lines(file_name, n):
#     try:
#         with open(file_name, 'r') as file:
#             lines = [next(file) for _ in range(n)]
#             return lines
#     except FileNotFoundError:
#         print(f"Error: File '{file_name}' not found.")
#         return []
#
#
# if __name__ == "__main__":
#     file_name = input("Enter the file name: ")
#     n = int(input("Enter the number of lines to read: "))
#
#     lines = read_first_n_lines(file_name, n)
#     if lines:
#         print(f"The first {n} lines of '{file_name}' are:")
#         for line in lines:
#             print(line, end='')


import pandas as pd

# Read the data from the Excel file
df = pd.read_csv("corona.csv")

# Calculate min and max age for vaccinated and unvaccinated patients
min_age_vaccinated = df[df['Is_vaccinated'] == 'Y']['Age'].min()
max_age_vaccinated = df[df['Is_vaccinated'] == 'Y']['Age'].max()
min_age_unvaccinated = df[df['Is_vaccinated'] == 'N']['Age'].min()
max_age_unvaccinated = df[df['Is_vaccinated'] == 'N']['Age'].max()

print("Min Age (Vaccinated):", min_age_vaccinated)
print("Max Age (Vaccinated):", max_age_vaccinated)
print("Min Age (Unvaccinated):", min_age_unvaccinated)
print("Max Age (Unvaccinated):", max_age_unvaccinated)

# Calculate average length of hospitalization
avg_hospitalization_length = df['Length_of_hospitalization'].mean()
print("Average Length of Hospitalization:", avg_hospitalization_length)


# Filter data based on user input and write to a new file
def filter_data():
    gender = input("Enter gender (M/F): ")
    age_min = int(input("Enter minimum age: "))
    age_max = int(input("Enter maximum age: "))
    vaccinated = input("Vaccinated? (Y/N): ")

    filtered_df = df[
        (df['gender'] == gender) &
        (df['Age'] >= age_min) &
        (df['Age'] <= age_max) &
        (df['Is_vaccinated'] == vaccinated)
        ]

    filtered_df.to_csv("filtered_data.csv", index=False)
    print("Filtered data written to filtered_data.xlsx")


# Call the filter_data function to filter the data and write to a new file
filter_data()
