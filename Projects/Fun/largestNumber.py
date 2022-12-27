# 

def largestNumber(n):
    listNumbers = []
    for i in range(0,10 ** n):
        listNumbers.append(i)
    
    return max(listNumbers)

def run():
  print(largestNumber(1)) # enter any integer
  
if __name__ == "__main__":
  run()
  
  
