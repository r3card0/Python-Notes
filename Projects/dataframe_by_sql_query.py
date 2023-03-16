import pandas as pd
from connect import Connect

# create dataframe from sql query
class Dataframe:
    def __init__(self,query) -> None:
        self.query = query
    
    def dataframeByQuery(self):
        df_read = pd.read_sql_query(self.query,connection)
        df = df_read.copy(deep=True)
        return df
