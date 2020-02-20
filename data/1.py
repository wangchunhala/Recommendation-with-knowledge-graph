u1=[]
a1=[]
r1=[]
import numpy as np
i=0
with open('user_artist.dat2', 'r') as infile:

    for line in infile:
        i+=1
        if(i>=75000):
          u = line.split('\t')[:]
          u1.append(u)
user=[]
for u in u1:
    user.append(int(u[0]))
lis=[]
for i in user:
    if i not in lis:
        lis.append(i)
ml=[]
for i in u1:
    if i[1] not in ml:
        ml.append(i[1])

with open('user_artist.dat4', 'w') as outfile:
    for us in lis:
        unew=[]
        ux=[]
        mlux=[]
        for un in u1:
            if(int(un[0])==int(us)):
                unew.append(un)
                ux.append(un[1])
        outfile.write(str(us)+'\t'+'(')
        for un in unew:
            outfile.write('\t'+str(un[1]))
        outfile.write('\t'+')')
        for i in ml:
            if i not in ux:
                mlux.append(i)
        for noe in mlux:
            outfile.write('\t' + str(noe))
        outfile.write('\n')




