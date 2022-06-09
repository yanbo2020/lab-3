import pickle

student = {"Jacob": 201932130146, "mutumba" : 201932130136}

outfile = open("students",'wb')

pickle.dump(student, outfile)
outfile.close()


infile = open("students", "rb")

new_student = pickle.load(infile)

infile.close()

print(new_student)

print(student == new_student)

print(type(new_student))