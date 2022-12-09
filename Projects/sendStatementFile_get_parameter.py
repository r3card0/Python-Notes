# How to send a sql statement to sql file getting parameters

def send_to_file(sql_statement,file_name):
    with open(file_name,'a') as f:
        f.write(sql_statement)

        
# Can be used variables and a path directory
send_to_file(sql_statement,'path/of/the/file/file.sql')
