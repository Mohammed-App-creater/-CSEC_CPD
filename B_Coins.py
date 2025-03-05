conditions = {"A": 0, "B": 0, "C": 0}
for i in range(3):
    cond = input()
    if cond[1] == ">":
        conditions[cond[0]] += 1
    else:    
        conditions[cond[2]] += 1
if conditions["A"] == conditions["B"] or conditions["A"] == conditions["C"] or conditions["B"] == conditions["C"]:
    print("Impossible")
else:   
    l = ["A", "B", "C"]
    for i in conditions:
        l[conditions[i]] = i
    print("".join(l))