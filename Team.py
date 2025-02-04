numTest = int(input())
numofAgreed = 0
Agreed = ("1 1 0", "1 0 1", "0 1 1", "1 1 1")
 
for i in range(numTest):
  binery= str(input())
  if binery in Agreed:
    numofAgreed += 1
 
 
print(numofAgreed)