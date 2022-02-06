# example of closure

def make_multiplier(x):
    
    def multiplier(m):
        return x * m
    
    return multiplier

times10 = make_multiplier(10)
times04 = make_multiplier(4)

print(times10(3))
print(times04(5))
print(times10(times04(2)))