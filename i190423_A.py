#!/usr/bin/env python
# coding: utf-8

# # List and Dictionaries 

# # Part A 

# In[1]:


TimeArray=[]


print ("Enter the number of Car Bookings ")
number=int(input())
for i in range (number):
    appendArray=[]
    print ("\n      Booking  ",i)
    print("Enter the Start day ")
    ip=int(input())
    appendArray.append(ip)
    print("Enter the End day ")
    ip=int(input())
    appendArray.append(ip)
    TimeArray.append(appendArray)
print (TimeArray)

# TimeArray=[[1,10], [5, 10],[11,20]]
TimeArray.sort(key=lambda x: x[0])
def CheckOverlap (array1,array2):
    if ((array1[0]< array2[1] and array1[1]>array2[0] ) or (array2[0]< array1[1] and array2[1]>array1[0])):
        return True
    else:
        return False

CarCount=1;
for i in range (len(TimeArray)-1):
    if (CheckOverlap(TimeArray[i],TimeArray[i+1])):
        CarCount=CarCount+1
        
            
print("Number of Cars needed are ",CarCount)


# #### 

# # Part 2

# In[2]:


lis = [2,2,4,2,4,5,6, 1,1]

def most_frequent_elements_in_lis(elem_list, left, right, frequency):
    dictionary ={}
    AnsArray=[]
    for i in range (left ,right+1):
        if elem_list[i] not in dictionary:
            dictionary [elem_list[i]]=0
        dictionary[elem_list[i]]=dictionary[elem_list[i]]+1
        if dictionary [elem_list[i]]==frequency:         
            AnsArray.append(elem_list[i])
    print (AnsArray)
    return AnsArray
most_frequent_elements_in_lis(lis,0,5,2)    
    


# # Part 3 

# In[3]:


StudentData=[{'roll_no': 'p18-1001', 'marks': {
'english': (1.4, 2.5, 15, 9.6, 33),
'calculus': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 88.4
},
{'roll_no': 'p18-1002', 'marks': {
'english': (2.4, 1.5, 12, 1.6, 21),
'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
{'roll_no': 'p18-1003', 'marks': {
'calculus': (2.4, 1.5, 12, None, 21),
'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4}]

def get_student_marks(StudentData):
    StudentsMarks={}
    for data in StudentData:
        StudentRecord={}
        for courses,marks in data['marks'].items():
            filtered=filter (None,marks)
            StudentRecord[courses]=sum(list(filtered))
        StudentsMarks[data['roll_no']]=StudentRecord
    print (StudentsMarks)


get_student_marks(StudentData)
gradeCondition={'A': 80, 'B': 70, 'C': 60, 'D': 50}
def get_Grade(ObtainedMarks ,gradingScheme ):
    for grade,marks in gradingScheme.items():
        if ObtainedMarks>marks:
            return grade
    return 'F'

print('Obtained Grade for 65 marks is ',get_Grade(65,gradeCondition)) 


# # 2) Numpy Matrix

# # Part A (i)

# In[4]:


import numpy as np
array=np.random.randint(1,10,size=(7,7))
print(array)
def second_Max_RowSum(mat):
    maximum=0
    SecondMax=0
    for i in range (len(mat)):
        value=sum(array[i])
        if (value>maximum):
            SecondMax=maximum
            maximum=value
    return SecondMax
print("Second Maximum sum is ",second_Max_RowSum(array))


# # Part (ii) 

# In[5]:


print (array)
def CheckTriangularMatrix(matrix):
    return (np.allclose(matrix,np.triu(matrix)) or np.allclose(matrix,np.tril(matrix))) and np.allclose(matrix, np.diag(np.diag(matrix))) 
CheckTriangularMatrix(array)
    
    
    
    
    
    
    
    
    
    
    
    


# # Part (iii)

# In[6]:


print(array)
def Minimum_Sum_Array(matrix):
    minimum=100
    index=-1
    for i in range(len(matrix)):
        value=np.sum(matrix[i])
        if value<minimum:
            minimum=value
            index=i
    return matrix[index]

print ('Minimum Sum Row is ',Minimum_Sum_Array(array))


# # Part (iv)

# In[7]:


def SwapRows(matrix):
    for i in range(0,len(matrix)-2,4):
        save=np.copy(matrix[i+2])
        matrix[i+2],matrix[i]=matrix[i],save
          

    print(matrix)
    return matrix

print (array)

print ('Swapped matrix')

SwapRows(array)


# # Part (v)

# In[8]:


def CalculateMean(array):
    return np.mean(array,axis=1)
CalculateMean(array)


# # Part (vi)

# In[9]:


print('Old Array ',array)
def SortColumns(matrix):
    matrix.sort(axis=0)
    return matrix

print('New Array ',SortColumns(array))


# # Q2 Part B

# In[10]:


def CreateString(matrix,string1):    
    row=0
    for character in string1:
        check=matrix[row].count(character)
        if check:
            matrix[row].remove(character)
        else:
            return "NO"
        row=(row+1)%len(matrix)
    return "YES"    
array=[['w','g','a'],['s','a','y'],['d','s','f']] 
print(CreateString(array,"wasay"))
array=[['w','g','a'],['h','h','y'],['d','s','f']] 
print(CreateString(array,"wasay"))        
        


# # Part C 

# In[11]:


def MaximumSum(matrix):
    Maximum=-1
    for i in range(len(matrix)-2):
        for j in range(len(matrix[i])-2):
            ad=matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
            if ad>Maximum:
                Maximum=ad
    return Maximum


matrix=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(MaximumSum(matrix))


# # Part D

# # Part i 

# In[12]:


import numpy as np
def ReplaceOdd(array):
    array[1::2]=-1
    return array
array=np.array([0,1,2,3,4,5,6,7,8,9])
copyArray=np.copy(array)
print(ReplaceOdd(copyArray))


# # Part ii

# In[13]:


import numpy as np 
def GetInRange(array,small,big):
    return np.where(np.logical_and(array> small, array< big))

array=np.random.randint(1,17,20)
print(GetInRange(array,5,10))


# # 3) String Manipulations 

# # Part A

# In[14]:


def CheckAnagram(string1,string2):
    if len(string1)==len(string2):
        if string1== string2[::-1]:
            return True
        else:
            return False
    else:
        return False
    
print(CheckAnagram('acc','cba'))
print(CheckAnagram('abc','cba'))


# # Part B

# In[15]:



def CheckRotation(string1,string2):
    if len(string1)==len(string2):
        if (string1[-1]+string1[:-1])== string2:
            return True
        else:
            return False
    else:
        return False
print(CheckRotation('xyz','zxy'))
print(CheckRotation('xyz','zxy'))


# # Part C

# In[16]:


def CheckSuperString(string1):
    CountArray={i:string1.count(i) for i in set(string1)}
    for i in set(string1):
        if CountArray[i] != (90-ord(i)+1):
            return False
    return True
print(CheckSuperString('ZZYY'))   


# # Part D 

# In[17]:


def FindPalindromes(string1):
    substrings=[string1[i:j+1] for i in range (len (string1))for j in range(i,len(string1)) ]
    palindromes=[]
    for x in list(set(substrings)):
        if x == x[::-1]:
            palindromes.append(x)
    print(palindromes)
    return palindromes
FindPalindromes('abba')
FindPalindromes('saad')


# Question 4 

## import random

class Card:
    action =""
    def __init__(self,Type="",value=0):
        self.Type=Type
        self.value=value
    def getCardInfo(self):
        return self.Type,self.value
    def CardPlayable(self,LastPlayedCard):
        if self.Type==LastPlayedCard.Type:
            if LastPlayedCard.value==4:
                return False
            return True
        elif self.value== LastPlayedCard.value:
            return True
    def getType(self):
        return self.Type
    def getValue(self):
        return self.value

class Deck:
    Cards=[]
    def __init__(self):
        self.CompleteDeck()
    def CompleteDeck(self):
        for j in range (4):
            for i in range(13):
                if j==0: 
                    self.Cards.append(Card('Spades',i+1))
                if j==1:
                    self.Cards.append(Card('Hearts',i+1))
                if j==2:
                    self.Cards.append(Card('Diamonds',i+1))
                if j==3:
                    self.Cards.append(Card('Clubs',i+1))
                
        
    def ShuffleCards(self):
        random.shuffle(self.Cards)
    
    def PrintDeck(self):
        for card in self.Cards:
            print(card.getCardInfo())
    
    def GiveOneCard(self):
        if len(self.Cards)==0:
            self.CompleteDeck()
        self.ShuffleCards()
        return self.Cards.pop()
    
    def CutDeck(self):
        return self.Cards.pop(random.randrange(0,len(self.Cards)))


class Player:
   
    def __init__(self, name , age ):
        self.PlayerCard={}
        self.PlayerCard['Diamonds']=[]
        self.PlayerCard['Spades']=[]
        self.PlayerCard['Hearts']=[]
        self.PlayerCard['Clubs']=[]
        self.name=name
        self.age=age
    def getPlayerInfo(self):
        return self.name,self.age
    def TakeCardFromDeck(self,Deck):
        newcard=Deck.GiveOneCard()
        Type,value=newcard.getCardInfo()
        self.PlayerCard[Type].append(value)
        return Deck
    def ShowCards(self):
        print ("\n{} Cards \n".format(self.name))
        for Type,value in self.PlayerCard.items():
            print ("{} : ".format(Type))
            if len(value)==0:
                print("None ",end=" ")
            for val in value:
                if val==11:
                    print('J',end="  ")
                elif val ==12:
                    print ('Q',end="  ")
                elif val ==13:
                    print ('K',end="  ")
                else:
                    print (val,end="  ")
            print('')   
    def RemoveCard(self,card):
        self.PlayerCard[card.Type].remove(card.value)

class Game:
    Players=[]
    lastCardPlayed=Card()
    CardstoHit=0
    CallCard=0
    KingSpades=0
    KingHearts=0
    def __init__(self,totalPlayers):
        self.deck=Deck()
        self.TotalPlayers=totalPlayers
    def addPlayers(self,player):
        self.Players.append(player)
    def DisplayPlayers(self):
        for player in self.Players:
            print(player.getPlayerInfo())
            
    def GiveCards(self):
        for player in self.Players:
            for i in range (5):
                self.deck=player.TakeCardFromDeck(self.deck)
    def CutDeck(self):
        self.lastCardPlayed=self.deck.CutDeck()
        return self.lastCardPlayed
    def getPlayers(self):
        return self.Players
    def PlayGame(self):
        Player_Index=0
        print("Starting Card  : ",self.CutDeck().getCardInfo())
        while (1):
            self.Players[Player_Index].ShowCards()
            print ('Do you want to play Card ? 1 for Yes , any other number for NO ')
            choice= int(input())
            if choice==1:      
                print("Enter the Card Type to Play  :  ")
                Type=str(input())
                print("Enter the Value of Card to Play (11 for 'J' , 12 for 'Q' and 13 for 'K' )")
                value =int (input())
                CardToBePlayed=Card(Type,value)
                if self.CallCard==1 and value!= 11:
                    Player_Index=(Player_Index+1)% len(self.Players)  
                    print( "\n ****** LAST CARD PLAYED is  ",self.lastCardPlayed.getCardInfo())
                else: 
                    self.CallCard==0
                    
                if CardToBePlayed.CardPlayable(self.lastCardPlayed)==True:
                    self.Players[Player_Index].RemoveCard(CardToBePlayed)
                    self.lastCardPlayed=CardToBePlayed          
                    if value==2 :
                        self.CardstoHit=self.CardstoHit+2
                    if value==3 :
                        self.CardstoHit=self.CardstoHit+3 
                    if Type=="Hearts" and value==13:
                        self.KingHearts=1
                        self.CardstoHit=5
                        Player_Index=(Player_Index+1)% len(self.Players)
                        continue
                        
                        
                    if Type=="Spades" and value==13:
                        self.KingSpades=1
                        self.CardstoHit=5
                        if Player_Index>1:
                            Player_Index=(Player_Index-1)% len(self.Players)
                        else:
                            Player_Index=len(self.Players)-1
                        continue
                        
                    if value==11:
                        print('Do you want to call a Card? 1 for Yes and any other key for No ')
                        choice2=int(input())
                        if choice2==1:
                            value==0
                            while value!=2 or value!=3 or value !=4:
                                print("Enter the Card Type to Call  :  ")
                                Type=str(input())
                                print("Enter the Non Action Card  Value to Call (11 for 'J' , 12 for 'Q' and 13 for 'K' )")
                                value =int (input())
                                CardToBePlayed=Card(Type,value)
                            self.lastCardPlayed=CardToBePlayed
                        else:
                            self.CallCard=1
                        
                else:
                    if (self.CardstoHit==0):
                        self.Players[Player_Index].TakeCardFromDeck(self.deck)
                        self.Players[Player_Index].TakeCardFromDeck(self.deck)
                    else:
                        while self.CardstoHit!=0:
                            self.Players[Player_Index].TakeCardFromDeck(self.deck)
                            self.CardstoHit=self.CardstoHit-1 
                            self.KingSpades=0
                            self.KingHearts=0
            else:
                if (self.CardstoHit==0):
                    if (self.lastCardPlayed.getValue()!=4):
                        print('Taking One Card From Deck ')
                        self.Players[Player_Index].TakeCardFromDeck(self.deck)                
                else:
                    while self.CardstoHit!=0:
                        self.Players[Player_Index].TakeCardFromDeck(self.deck)
                        self.CardstoHit=self.CardstoHit-1
                        self.KingSpades=0
                        self.KingHearts=0
            
            Player_Index=(Player_Index+1)% len(self.Players)  
            
            print( "\n ****** LAST CARD PLAYED is  ",self.lastCardPlayed.getCardInfo())
            
            
            
            
            
            
    
NumberOfPlayers=3
game = Game(NumberOfPlayers)

print ("1 to  play with 3 players(info already added only for easy testing and checking ) ,2 to play for N Players")
choice=int(input())
if choice==2:
    print("Enter Number of Players : ")
    NumberOfPlayers=int(input())
    for i in range (NumberOfPlayers):
        name =""
        age = 1
        print ("Player no ",i+1)
        print ("Enter the Name : " ,end="  ")
        name=str(input())
        print("Enter the Age : ",end="  ")
        age=int (input ())
        game.addPlayers(Player(name,age))
else:
    game.addPlayers(Player("Wasay",18))
    game.addPlayers(Player("Ali",20))
    game.addPlayers(Player("Zain",15))
game.GiveCards()
game.DisplayPlayers()
game.PlayGame()







        

## 

# In[ ]:





# In[ ]:





# In[ ]:




