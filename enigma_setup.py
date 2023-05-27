import random as r
"""
#TO MAKE ROTERS
master = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
master_lst = list(master)
print(master_lst)
roters = []

for i in range(5):
    r.shuffle(master_lst)
    roter_dict = {}
    for k in range(len(master_lst)/2):
        roter_dict[master[k]] = master_lst[k]
    roters.append(roter_dict)

for i in roters:
    print(i)

"""

#TO MAKE REFLECTOR

master = "ABCDEFGHIJKLM"
master_2 = "NOPQRSTUVWXYZ"

master_2_lst = list(master_2)
r.shuffle(master_2_lst)
reflector = []
reflector.append(list(master))
reflector.append(master_2_lst)


print(reflector)
