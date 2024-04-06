def isFalse(x: int, y: int, z: int):
    list = [x, y, z]
    i = 0
    for integer in list:
        if integer > 0:
            i+=1
    if i == 2:
        return True
    else:
        return False
        
isFalse(2,0,-1)

'''
data = [[1,2], [5,8], [9,2]]

(1-2)*(5-8)*(9-2) = (-1)*(-3)*(7) = 21

'''

pairs = [[1,2], [5,8], [9,2]]
newlist = []
for pair in pairs:
  newlist.append(pair[0] - pair[1])

for integer in newlist:
    integer
pairs = [[1,2], [5,8], [9,2]]
result = [(a[0]-a[1]) for a in pairs]

