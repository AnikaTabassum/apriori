import re
class apiori:
    def __init__(self):
        "do "


    def readFile(self):
        dataItem = set()
        transact=list()

        with open("data.txt") as file:
            for line in file:
                # x=line.split(",")
                
                x = re.split(" |\n", line)
                # dataset.append(x)
                transact.append(x[1])
                
                i = 1
                
                x= re.split(" |\n|,",line)
                print(x)
                while i < x.__len__():
                    if x[i] != "":
                        #item.add(x[i])
                        dataItem.add(x[i])
                    i += 1
            dataItem=sorted(dataItem)
        #print(dataItem)
        #print(transact)
        self.aprioriFucn(dataItem, transact)
        
        
        
    def aprioriFucn(self,dataItem,transact):
        print(self.checkSubsetAndMakeCandidateTable(dataItem,transact))
        candidateTable=dataItem
        i=0
        while i<3:
            candidateTable=self.makeCandidateTable(candidateTable)
            
            print(self.checkSubsetAndMakeCandidateTable(candidateTable,transact))
            '''can2=self.makeCandidateTable(candidateTable)
            print(self.checkSubsetAndMakeCandidateTable(can2,transact))'''
            i+=1

    def makeCandidateTable(self,dataSet):
        
        finalList=list()
        i=0
        while i <dataSet.__len__():
            j=i+1
            temp = dataSet[i].split(",")
            while j < dataSet.__len__():
                lis = dataSet[j].split(",")
                f = 0
                x=1
                while x<lis.__len__():
                    if temp[x] != lis[x]:
                       f = 1
                    x+=1
                if f==0:
                    #print(dataSet[i])
                    new = dataSet[i] + "," + lis[0]
                    
                    finalList.append(new)
                j+=1
            i+=1
        
        returnList=sorted(finalList)
        print(returnList)
        return returnList

    def checkSubsetAndMakeCandidateTable(self, finalList,transact):
        flag=0
        candidateTable={}
        #print(transact)
        temp=list()
        for value in finalList:
            temp.append(str(value))
        i=0
        while i < temp.__len__():
            #print(temp[i])
            j=0
            cnt=0
            while j< transact.__len__():
                #print(transact[j])
                if (all(x in transact[j] for x in temp[i])):
                    cnt+=1
                    #print("fdsf")
                j+=1
            
            if cnt>=2:
                candidateTable[temp[i]]=cnt
            #print("cnt"+str(cnt))
            i += 1
        return candidateTable

apiori().readFile()
