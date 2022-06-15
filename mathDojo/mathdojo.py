class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for y in nums:
            self.result -= y
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# # run each of the methods a few more times and check the result!

y = md.add(100,200).add(300,100,100).subtract(50, 200).result
print(y)

z = md.subtract(50).add(25, 5).result
print(z)