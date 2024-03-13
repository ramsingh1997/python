import os

def add_column_to_sql_files(directory, column_name, data_type):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".sql"):
            file_path = os.path.join(directory, filename)
            # Read the SQL file
            with open(file_path, "r") as file:
                sql_content = file.readlines()

            # Find the line containing "CREATE TABLE"
            for i, line in enumerate(sql_content):
                if "CREATE TABLE" in line:
                    # Add the new column and its data type after the last column definition
                    last_column_index = i
                    while ";" not in sql_content[last_column_index]:
                        last_column_index += 1
                    sql_content.insert(last_column_index, f"    {column_name} {data_type},\n")
                    break

            # Write the updated SQL content back to the file
            with open(file_path, "w") as file:
                file.writelines(sql_content)

# Provide the directory containing SQL files, new column name, and data type
# directory_path = "./fs/"
# new_column_name = "country"
# new_column_data_type = "VARCHAR(50)"

# add_column_to_sql_files(directory_path, new_column_name, new_column_data_type)