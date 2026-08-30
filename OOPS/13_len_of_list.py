# Override the __len___() method on vector of problem 5 to display the dimension of the vector
class vector:
    def __init__(self,l):
        self.l=l
    def __len__(self):
        return len(self.l)

v1=vector([1,2,3])
print(v1.l)
print(len(v1))