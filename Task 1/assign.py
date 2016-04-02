import math
import collections
matrix = {}
for i in range(1000): #change
    matrix[i] = {}


import operator

def pearson(x, y):
    xMean = 0
    yMean = 0

    countX = 0; countY = 0;
    for key in matrix:
        tempX = matrix[key].get(x)
        tempY = matrix[key].get(y)
        

        if tempX is not None and tempY is not None:
            xMean += tempX
            countX += 1
            yMean += tempY
            countY += 1
    if(countX == 0):
        xMean = 0
    else:
        xMean /= countX

    if(countY == 0):
        yMean = 0
    else:
        yMean /= countY

    topXY = 0; botX = 0; botY = 0;

    for key in matrix:
        tempX = matrix[key].get(x)
        tempY = matrix[key].get(y)

        if tempX is not None and tempY is not None:
            topXY += (tempX - xMean)*(tempY - yMean)
            botX += (tempX - xMean)**2
            botY += (tempY - yMean)**2

    botX = math.sqrt(botX)
    botY = math.sqrt(botY)

    temp = botX*botY
    if temp == 0:
        return 0
    else:
        return topXY/(botX*botY)


def itemitem(x,i): #user x, item i
    topsim = {}
    num = 0
    denom = 0
    #print('matrix keys')
    #print matrix[x].keys();
    for movie in matrix[x].keys():
        topsim[movie] = pearson(movie,i)
        #if topsim[movie] > 1 or topsim[movie] < -1:
        #	print(topsim[movie])
    sorted_top_items = sorted(topsim.items(), key = operator.itemgetter(1), reverse = True)
    #print('print sorted_top_items')
    #print(topsim)
    #print(sorted_top_items[1])
    count = 0

    for movie in sorted_top_items[:20]:
        #print("hello " + str(x) + " " + str(movie[0]))
        #if(count==20): break
        num = num + (movie[1] * matrix[x][movie[0]])
        if movie[1] < 0:
        	denom = denom - movie[1]
        else:
        	denom = denom + movie[1]    
        count = count + 1
    if denom == 0:
    	return 3
    return num/denom

def populate(fname):
    with open(fname) as f:
        for l in f:
            matrix[int(l.split()[0])][int(l.split()[1])] = float(l.split()[2])
            #l.split()
            #print("hello" + " l0 is " + str(l[0]) + " l1 is " + str(l[1]) + " l2 is " + str(l[2]))
            #print(l[1])
            #matrix[l[0]][l[1]] = l[2]




def recommend(user):
	temp = 0
	reccos = {}
	for i in range(1,1683): #change
		if matrix.get(user).get(i) is None:
			reccos[i] = itemitem(user, i)
    
	sorted_top_items_dsec = sorted(reccos.items(), key = operator.itemgetter(1), reverse = True)
	sorted_top_items_asec = sorted(reccos.items(), key = operator.itemgetter(1))
    #print("hello " + str(len(reccos)))
	for i in range(1,11):
		print(sorted_top_items_dsec[i])
		#print(sorted_top_items_asec[i])
#    print('ratings are being printed')
#    print(sorted_top_items)


populate('u1.base')
y=input('type user no. (b/w 1 to 942) you want recommendations for: ')
recommend(y)
