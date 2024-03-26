

d1={1:15, 2:25}
d2 = {3:30, 4:40}
d3 = {5:45, 6:65}


d1.update(d2)
d1.update(d3)

print(d1)

students = {
    1: "Kārlis",
    2: "Dace",
    3: "Edgars",
    4: "Anastasija",
    5: "Evija"
}

students[4]

students[6] = "Uldis"
students.update({students.__len__() + 1: "Jānis"})

'Anna' in students.values()






