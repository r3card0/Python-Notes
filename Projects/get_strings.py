class String:
    def __init__(self) -> None:
        pass

    
    def reg(self):
        self.region = str(input('Set the region: '))
        return self.region
    
    def q(self):
        self.quarter = str(input('Set the quarter -> YY1QQ: '))
        return self.quarter
    
    def jn(self):
        self.jira_number = int(input('Set jira number: '))
        return self.jira_number
    

def run():
    pass
    ## region = String()
    # quarter = String()
    # jira_number = String()
    # print(region.reg())
    # print(quarter.q())
    # print(jira_number.jn())


if __name__ == "__main__":
    run()
