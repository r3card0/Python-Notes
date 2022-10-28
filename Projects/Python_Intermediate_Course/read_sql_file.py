# 1. empty list
# 2. set file path using with function
# 3. use for loop to append into empty list
# 4. convert list to string

def read_sql_file():
    sql = []
    with open('/file/path/script.sql','r',encoding='utf-8') as file:
        for line in file:
            sql.append(line)
        
        sql_statement = """""".join(sql)
        return sql_statement
