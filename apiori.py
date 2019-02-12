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
                #print(x)
                while i < x.__len__():
                    if x[i] != "":
                        #item.add(x[i])
                        dataItem.add(x[i])
                    i += 1
            dataItem=sorted(dataItem)
        #print(dataItem)
        #print(transact)
        given=input("given confidence ")
        print(given)
        expect=input("expected confidence ")
        print(expect)
        stri=given+","+expect
        print(stri)
        temp=stri.split(",")
        temp=sorted(temp)
        print(temp)
        stri=""
        for i in range(temp.__len__()):
            stri+=str(temp[i])
            if i<temp.__len__()-1:
                stri+=","
        print(stri)
        self.aprioriFucn(dataItem, transact,given,expect,stri)
        
        
        
    def aprioriFucn(self,dataItem,transact,given,expect,stri):
        
        giv=0
        get=0
        minimumSupport=self.checkSubset(dataItem,transact)
        print(minimumSupport)
        givenValue,getValue=self.checkConfidence(minimumSupport,given,expect,stri)
        if givenValue!=0:
            giv=givenValue
        if getValue!=0:
            get=getValue
        candidateTable=dataItem
        i=0
        while i<2:
            candidateTable=self.makeCandidateTable(candidateTable)
            
            minimumSupport=(self.checkSubset(candidateTable,transact))
            print(minimumSupport)
            givenValue,getValue=self.checkConfidence(minimumSupport,given,expect,stri)
            if givenValue!=0:
               giv=givenValue
            if getValue!=0:
               get=getValue
            '''can2=self.makeCandidateTable(candidateTable)
            print(self.checkSubsetAndMakeCandidateTable(can2,transact))'''
            i+=1
        print(giv)
        print((get/giv)*100)

    def checkConfidence(self,minimumSupport,given,expect,stri):
        #print(minimumSupport)
        givenValue, getValue=0,0
        for x in minimumSupport:
            
            if x==given:
                givenValue=minimumSupport[x]
                print(givenValue)
            elif x==stri:
                getValue=minimumSupport[x]
                print(getValue)
        return givenValue, getValue
                
    def makeCandidateTable(self,dataSet):
        print("lol")
        print(dataSet)
        finalList=list()
        i=0
        while i <dataSet.__len__():
            j=i+1
            temp = dataSet[i].split(",")
            while j < dataSet.__len__():
                lis = dataSet[j].split(",")
                f = 0
                x=0
                while x<lis.__len__()-1:
                    if temp[x] != lis[x]:
                       f = 1
                    x+=1
                if f==0:
                    #print(dataSet[i])
                    new = dataSet[i] + "," + lis[lis.__len__()-1]


                    finalList.append(new)
                j+=1
            i+=1
        tempSet=set(finalList)
        returnList=sorted(tempSet)
        print(returnList)
        return returnList

    def checkSubset(self, finalList,transact):
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

    #def getConfidence(self):
        #print("given confidence ")
        
        #self.aprioriFucn(dataItem, transact)

apiori().readFile()