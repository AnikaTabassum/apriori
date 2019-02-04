import re
class apiori:
    def __init__(self):
        "do "

    def readFile(self):
        item=set()
        dataset=list()
        with open ("data.txt") as file:
            for line in file:
                #x=line.split(",")
                x = re.split(",|\n",line)
                #dataset.append(x)
                i=1
                while i<x.__len__():
                    if x[i]!="":
                        item.add(x[i])
                        dataset.append(x[i])
                    i+=1
        print(dataset)
        supportForOne=self.makeCandidateSet(item,dataset)
        
        itemSetL1=self.minimumSupport(supportForOne,item)
        currentLset=self.joinSet(itemSetL1,2)
        #makeTable
    def makeCandidateSet(self,item,dataset):
        support={}
        for value in item:
        #for value in item:
            i=0
            cnt=0
            while i<dataset.__len__():
                    #print(dataset[i])
                    #print(value)
                if value==dataset[i]:
                    cnt+=1
                support[value]=cnt
                i+=1
                #print(value)
                #print(cnt)
        print(support)
        return support
    def minimumSupport(self,minimum,item):
        i=0
        itemSet={}
        for value in item:
            if minimum.get(value)>=2:
                itemSet[value]=minimum.get(value)
        return itemSet
            #print(minimum.get(value))

    def joinSet(self,itemSet,length):
        #return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
        finalSet=set()
        finalList=list()
        for i in itemSet:
            newSet=set()
            newSet.add(i)
            print("i")
            print(i)
            for j in itemSet:
                if newSet.__len__()==length-1:
                    newSet.add(j)
                    print(j)
                    #print(newSet)
                    #finalSet.add(newSet)
                    finalList.append(newSet)
                    print(finalList)
                    newSet.remove(j)
        print(finalList)





apiori().readFile()
#apiori().makeTable()
