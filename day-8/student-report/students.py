class Student(object):

    def __init__(self, name, regid, age=0):
        self.name = name
        self.regid = regid
        self.age = age
        self.marks = {"physics": 0, "chemistry": 0, "maths": 0, "biology": 0}
        self.average = 0
        self.rank = 0

    # customize the object representation and print output

    def __repr__(self):
        return str(self.regid)

     
    def __str__(self):
        return ','.join([str(self.name), str(self.age), str(self.regid), ','.join(map(str,self.marks.values())), \
                         str(self.average), str(self.rank)])


    def calculate_average(self):
        self.average = sum(list(map(float, self.marks.values())))/len(self.marks.values())
        return self.average

    def set_rank(self, rank):
        self.rank = rank
        return self.rank

    def get_rank(self):
        return self.rank

    def set_marks(self, **marks_list):  # s.set_marks(phy=90, chem=80)
        self.marks = marks_list

    def get_marks(self):
        return self.marks
    
    def debug(self):
        print(self.name)
    
# -------------------------------------------------------------------------------------- #

if __name__ == "__main__":

    s = Student('Anil', 1221)
    s.set_marks(phy=90, chem=80, math=98, bio=77)
    s.calculate_average()
    print(s)