def prg2com(inlist, coms):
    outlist = []
    sumout = []
    for x in range(coms):
        outlist.append([])
        sumout.append(0)

    #print(outlist)
    #print(sumout)
        
    inlist.sort(reverse=True)
    
    print('inlist: ',inlist)

    for bread in inlist:
        lowbasket = sumout.index(min(sumout))
        
        #print('lowbasket: ',lowbasket)
        outlist[lowbasket].append(bread)
        
        #print(sumout)
        
        sumout[lowbasket] += bread
        
        #print(sumout)

    return outlist

print(prg2com([3,15,6,22,13,2], 3))

