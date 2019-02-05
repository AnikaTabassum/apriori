import re
class apiori:
    def __init__(self):
        "do "

    def readFile(self):
        dataset = list()
        transact=list()

        with open("data.txt") as file:
            for line in file:
                # x=line.split(",")
                x = re.split(",|\n", line)
                # dataset.append(x)
                transact.append(x)
                i = 1

                while i < x.__len__():
                    if x[i] != "":
                        #item.add(x[i])
                        dataset.append(x[i])
                    i += 1

        #print(transact)
        item=set(dataset)
        item=sorted(item)
        print(item)
        supportForOne = self.makeCandidateSet(item, dataset)

        itemSetL1 = self.minimumSupport(supportForOne, item)
        currentLset = self.joinSet(itemSetL1, 2)
        listMake=list(list(currentLset))
        #print(listMake)
        itemSetL2=self.checkSubsetAndMakeCandidateTable(transact,currentLset)
        currentL2set=self.joinSet(itemSetL2,3)


    def makeCandidateSet(self, item, dataset):
        support = {}
        stringList=list()
        string=""
        for value in item:
            # for value in item:
            i = 0
            cnt = 0
            stringList.append(value)
            string+=value
            while i < dataset.__len__():
                # print(dataset[i])
                # print(value)

                if value == dataset[i]:
                    cnt += 1
                support[value] = cnt
                i += 1


        return support

    def minimumSupport(self, minimum, item):
        i = 0
        itemSet = {}
        for value in item:
            if minimum.get(value) >= 2:
                itemSet[value] = minimum.get(value)
        return itemSet
        # print(minimum.get(value))

    def joinSet(self, itemSet, length):
        # return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
        strg=""
        print(itemSet)
        finalList=list()
        for i in itemSet:
            newSet = set()
            newSet.add(i)

            for j in itemSet:
                if newSet.__len__() == length - 1:
                    newSet.add(j)
                    #print(newSet.__len__())
                    if newSet.__len__()==length:

                        temp=set(newSet)
                        strg+=str(newSet)
                        finalList.append(temp)
                        #print(strg)
                    newSet.remove(j)
        #print(finalList)
        return finalList

    def checkSubsetAndMakeCandidateTable(self, transact, finalList):
        flag=0
        candidateTable={}
        print(transact)
        temp=list()
        for value in finalList:
            temp.append(list(value))

        i=0
        while i < temp.__len__():
            j=0
            cnt=0
            while j< transact.__len__():
                if (all(x in transact[j] for x in temp[i])):
                    cnt+=1
                    #print("fdsf")
                j+=1

            if cnt>=2:

                '''strp= re.split('[|]', stra)
                print(strp)'''
                tem=""
                lop="', '"
                u=0
                while u<temp[i].__len__():
                    tem+=str(temp[i][u])
                    u+=1
                    if u<temp[i].__len__():
                        tem+=lop
                    #u+=1
                candidateTable[tem]=cnt
            i += 1


        print(candidateTable)
        return candidateTable

apiori().readFile()