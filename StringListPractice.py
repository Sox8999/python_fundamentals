str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day')

str.replace('day', 'month')

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]


print y[0]
print y[len(y)-1]

z = [y[0], y[len(y)-1]]
print z

zz = [19,2,54,-2,7,12,98,32,10,-3,6]

zz.sort()
print zz

yy = zz[:len(zz)/2]
xx = zz[len(zz)/2:]

print yy
print xx

xx.insert(0, yy)

print xx
