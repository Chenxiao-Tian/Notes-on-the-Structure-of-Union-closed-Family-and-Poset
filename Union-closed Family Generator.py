# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:51:21 2020

@author: 田晨霄
"""
Family={
  (1, 11, 13), (1, 6, 24, 11, 13, 14), (20, 5, 23),(1, 2, 5, 7, 11, 12, 13, 20, 23), 
 (2, 5, 7, 8, 9, 12, 16, 20, 22, 23, 27, 28), (1, 20, 5, 23, 11, 13), (9, 28, 22), 
 (1, 2, 5, 6, 7, 11, 12, 13, 14, 20, 23, 24), (2, 12, 7), 
 (1, 5, 6, 8, 9, 11, 13, 14, 16, 20, 22, 23, 24, 27, 28), 
 (1, 2, 7, 9, 11, 12, 13, 22, 28), (1, 2, 6, 7, 8, 9, 11, 12, 13, 14, 16, 22, 24, 27, 28), 
 (20, 5, 22, 23, 9, 28), (2, 6, 7, 24, 12, 14), (16, 1, 8, 27, 11, 13), (2, 20, 5, 23, 7, 12),
 (1, 2, 6, 7, 11, 12, 13, 14, 24), (6, 22, 24, 9, 28, 14), 
 (2, 5, 6, 7, 8, 9, 12, 14, 16, 20, 22, 23, 24, 27, 28), (1, 22, 9, 11, 28, 13), 
 (16, 22, 8, 9, 27, 28), (1, 2, 5, 6, 7, 9, 11, 12, 13, 14, 20, 22, 23, 24, 28), 
 (6, 8, 9, 14, 16, 22, 24, 27, 28), (1, 8, 9, 11, 13, 16, 22, 27, 28), 
 (1, 2, 5, 7, 8, 9, 11, 12, 13, 16, 20, 22, 23, 27, 28), (16, 2, 7, 8, 27, 12), 
 (1, 2, 7, 8, 11, 12, 13, 16, 27), (16, 6, 8, 24, 27, 14), (1, 6, 9, 11, 13, 14, 22, 24, 28),
 (16, 1, 8, 11, 27, 13), (2, 6, 7, 9, 12, 14, 22, 24, 28), 
 (1, 5, 8, 9, 11, 13, 16, 20, 22, 23, 27, 28), (2, 20, 5, 7, 23, 12),
 (2, 5, 6, 7, 9, 12, 14, 20, 22, 23, 24, 28), (2, 22, 7, 9, 28, 12), 
 (5, 8, 9, 16, 20, 22, 23, 27, 28), (2, 22, 7, 9, 12, 28), 
 (1, 5, 6, 8, 11, 13, 14, 16, 20, 23, 24, 27), (2, 6, 7, 8, 12, 14, 16, 24, 27), 
 (22, 6, 24, 9, 28, 14), (1, 5, 6, 11, 13, 14, 20, 23, 24), (2, 5, 7, 8, 12, 16, 20, 23, 27),
 (1, 2, 6, 7, 9, 11, 12, 13, 14, 22, 24, 28), (1, 5, 8, 11, 13, 16, 20, 23, 27), 
 (2, 5, 6, 7, 8, 12, 14, 16, 20, 23, 24, 27), (1, 6, 8, 11, 13, 14, 16, 24, 27), 
 (1, 5, 9, 11, 13, 20, 22, 23, 28), (1, 5, 6, 9, 11, 13, 14, 20, 22, 23, 24, 28), 
 (1, 2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 20, 22, 23, 24, 27, 28), 
 (5, 6, 9, 14, 20, 22, 23, 24, 28), (5, 6, 8, 9, 14, 16, 20, 22, 23, 24, 27, 28), 
 (1, 2, 5, 6, 7, 8, 11, 12, 13, 14, 16, 20, 23, 24, 27), (16, 20, 5, 23, 8, 27), 
 (1, 2, 5, 7, 9, 11, 12, 13, 20, 22, 23, 28), (2, 7, 8, 9, 12, 16, 22, 27, 28),
 (20, 5, 6, 23, 24, 14), (2, 5, 6, 7, 12, 14, 20, 23, 24), (2, 5, 7, 9, 12, 20, 22, 23, 28),
 (1, 6, 8, 9, 11, 13, 14, 16, 22, 24, 27, 28), (1, 2, 7, 8, 9, 11, 12, 13, 16, 22, 27, 28),
 (5, 6, 8, 14, 16, 20, 23, 24, 27), (1, 2, 7, 11, 12, 13), (24, 6, 14), 
 (16, 6, 24, 8, 27, 14), (1, 2, 6, 7, 8, 11, 12, 13, 14, 16, 24, 27), 
 (1, 2, 5, 7, 8, 11, 12, 13, 16, 20, 23, 27), (2, 6, 7, 8, 9, 12, 14, 16, 22, 24, 27, 28), 
 (8, 16, 27)}
print("""Step 1: Verify the family is a union-closed family.""".center(96,"="))
judge=True
v=[]
for A in Family:
    v.append(set(A))
new=[]
for x in v:
    if x not in new:
        new.append(x)
for i in range(len(new)):
    new[i]=tuple(new[i])
Family=set(new)
print(len(Family)+1)
for A in Family:
    for B in Family:
        if A!=" ∅ " and B!=" ∅ ":
            if ((set(A)|set(B)) not in ([set(subset) for subset in Family])):
                judge=False
print("\n"+"Is it a union-closed family? Result:"+str(judge)+"\n")
print("""Step 2: Get all the elements.""".center(96,"="))
allelements=set()
for subset in Family:
    if subset!=" ∅ ":
        allelements=allelements|set(subset)
print("\n"+"Get all the 18 elements in this Family:"+str(allelements)+"\n")
print("\n"+"""Step 3: Count the frequency of elements.""".center(96,"=")+"\n")
frequency__diction={}
for x in allelements:
    frequency__diction[x]=0
for subset in Family:
    if subset != " ∅ ":
        for element in set(subset):
            frequency__diction[element]+=1
print("The frequency of all the 18 elements: ",frequency__diction)
print("\n"+"""Step 4: It's a counterexample.""".center(96,"=")+"\n")
maximum__frequency=max(frequency__diction.values())/(len(Family)+1)
print("the maximum frequency:",maximum__frequency)
print("The maximum frequency"+str(maximum__frequency)+"is less than 0.5!It's a counterexample.")