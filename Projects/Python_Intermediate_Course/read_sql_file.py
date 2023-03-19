# 1. empty list
# 2. set file path using with function
# 3. use for loop to append into empty list
# 4. convert list to string

class Read:
    def __init__(self,pathfile) -> None:
        self.pathfile = pathfile

    def read_sql_file(self):
        self.sql = []
        with open(self.pathfile,'r',encoding='utf-8') as file:
            for line in file:
                self.sql.append(line)

            sql_statement = """""".join(self.sql)
            return sql_statement

# Instance
test = Read('/path/file.sql')

print(test.read_sql_file())


