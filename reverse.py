# def henry(old):
#     new = []
#     t = len(old)
#     for i in range(0,t):
#         e = len(old) - 1
#         new.append(old[e])
#         old.remove(old[e])
#     return new 

# listnum = [1,2,3,4,5,6,7,8]
# print(henry(listnum))

# split mid, reverse
# def henry(old):
#     new = []
#     t = len(old)
#     for i in range(0,t):
#         e = len(old) - 1
#         new.append(old[e])
#         old.remove(old[e])
#     return new 

# listnum = [1,2,3,4,5,6,7,8]
# m = len(listnum)//2
# listnum1 = listnum[:m]
# listnum2 = listnum[m:]
# print(henry(listnum1) + henry(listnum2))

# oddnumber, meadian stay mid
def henry(old):
    new = []
    t = len(old)
    if t % 2 == 0:
        for i in range(0,t):
            e = len(old) - 1
            new.append(old[e])
            old.remove(old[e])
        print(new) 
    else:
        for i in range(0,t):
            e = len(old) - 1
            new.append(old[e])
            old.remove(old[e])
        print(listnum1 + [new[m]] + listnum2)

listnum = [1,2,3,4,5,6,7,8,9]
m = len(listnum)//2
listnum1 = new[:m]
listnum2 = new[m:]
henry(listnum)

# coba kalo ganjil, tengahnya ga gerak

# old = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# new = []
# t = int(len(old)//2)
# old1 = old[:t]
# old2 = old[t:]

# old = old1
# new1 = []
# a = len(old)
# for i in range(0,a):
#     e = len(old) - 1
#     new1.append(old[e])
#     old.remove(old[e])
# # print(new1)

# old = old2
# new2 = []
# a = len(old)
# for i in range(0,a):
#     e = len(old) - 1
#     new2.append(old[e])
#     old.remove(old[e])
# # print(new2)
# print(new1 + new2)



# old = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# new = []
# t = int(len(old)//2)

# if len(old)%2 == 0:
#     old1 = old[:t]
#     new1 = []
#     a = len(old1)
#     for i in range(0,a):
#         e = len(old1) - 1
#         new1.append(old1[e])
#         old.remove(old1[e])
#     # print(new1)
#     old2 = old[t:]
#     new2 = []
#     a = len(old)
#     for i in range(0,a):
#         e = len(old) - 1
#         new2.append(old[e])
#         old.remove(old[e])
#     # print(new2)
#     print(new1 + new2)
# else:
#     old1 = old[:t]
#     old = old1
#     new1 = []
#     a = len(old)
#     for i in range(0,a):
#         e = len(old) - 1
#         new1.append(old[e])
#         old.remove(old[e])
#     old2 = old[t+1:]
#     old = old2
#     new2 = []
#     a = len(old)
#     for i in range(0,a):
#         e = len(old) - 1
#         new2.append(old[e])
#         old.remove(old[e])
#     # print(new2)
#     print(new1 + new2)