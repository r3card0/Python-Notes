# How to send a sql statement to a file

# create sql statement
def statement():
    statement = """
    SELECT * FROM table
    """
    return statement
# function stored in a variable
sql = statement()

# sent sql statement to sql file
def send_to_file():
    with open('file.sql','a') as f: # indicate the name of the new file
        f.write(sql)

def run():
    send_to_file()

if __name__ == "__main__":
    run()
