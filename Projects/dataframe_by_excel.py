import pandas as pd

class Dexel:
    def __init__(self,pathfile) -> None:
        self.pathfile = pathfile

    def dataframeByExcel(self):
        df_read = pd.read_excel(self.pathfile)
        df = df_read.copy(deep=True)
        return df
