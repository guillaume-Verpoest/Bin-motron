import random
people = ["pierre", "paul", "guillaume", "eliott"]
crew = {}
cpt = 0
number_in_group = 2

random.shuffle(people)
while(len(people) >= number_in_group):
    cpt+=1
    newarray = []
    for i in range(number_in_group):
        newarray.append(people[0])
        people.remove(people[0])
    crew["group" + str(cpt)] = newarray
if len(people) > 0 :
    crew["group" + str(cpt+1)] = people

print(crew)

from sandbox import test

print(test)

