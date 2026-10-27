# int float  bool 
# list tuple dict set

# average
def mean(xs):
    return sum(xs) /len(xs)
def std(xs):
    m = mean(xs)
    return (sum((x-m)**2 for x in xs) / len(xs))**0.5

data = [3.0,1.0,2.0]
m,s = mean(data),std(data)
z = [(x-m)/s for x in data]
print(z)
print(data)

