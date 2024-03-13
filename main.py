from fs.appending_column import add_column_to_sql_files 


# Define VARCHAR as a constant to represent the SQL VARCHAR data type
VARCHAR = "VARCHAR"

add_column_to_sql_files("./fs/", "FlagURL", f"{VARCHAR}(1024)")