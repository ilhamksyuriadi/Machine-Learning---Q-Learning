# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:44:49 2018

@author: ilham k syuriadi
"""
import numpy as np
import random as rd

board = np.genfromtxt('board.txt')
CS = [] #variabel current state
IS = [9,0] #variabel initial state
GS = [0,9] #variabel goal state
Qtable = np.zeros((100,4))
Rtable = []
move = []
#Up Down Left Right
def generateRTable():#initiate the R table with possible move
    for i in range(9,-1,-1):
        for j in range(10):
            if i + 1 == 10 and j - 1 == -1:
                Rtable.append([1,0,0,1])
            elif i + 1 == 10 and j + 1 == 10:
                Rtable.append([1,0,1,0])
            elif i - 1 == -1 and j - 1 == -1:
                Rtable.append([0,1,0,1])
            elif i - 1 == -1 and j + 1 == 10:
                Rtable.append([0,1,1,0])
            elif i - 1 == -1:
                Rtable.append([0,1,1,1])
            elif i + 1 == 10:
                Rtable.append([1,0,1,1])
            elif j - 1 == -1:
                Rtable.append([1,1,0,1])
            elif j + 1 == 10:
                Rtable.append([1,1,1,0])
            else:
                Rtable.append([1,1,1,1])

def generateMove():#initiate table move with possible move for agent in a coordinat of board
    for i in range(len(Rtable)):
        temp = []
        if Rtable[i][0] == 1:
            temp.append(0)#0 = up
        if Rtable[i][1] == 1:
            temp.append(1)#1 = down
        if Rtable[i][2] == 1:
            temp.append(2)#2 = left
        if Rtable[i][3] == 1:
            temp.append(3)#3 = right
        move.append(temp)

def convert(s):#function for convert the board coordinate to list index
    if s[0] == 9:# so it can access the other list to move or other
        return s[1]
    elif s[0] == 8:
        return int("1" + str(s[1]))
    elif s[0] == 7:
        return int("2" + str(s[1]))
    elif s[0] == 6:
        return int("3" + str(s[1]))
    elif s[0] == 5:
        return int("4" + str(s[1]))
    elif s[0] == 4:
        return int("5" + str(s[1]))
    elif s[0] == 3:
        return int("6" + str(s[1]))
    elif s[0] == 2:
        return int("7" + str(s[1]))
    elif s[0] == 1:
        return int("8" + str(s[1]))
    elif s[0] == 0:
        return int("9" + str(s[1]))

def nextMove(move,CS):
    temp = []
    tabM = move[convert(CS)]
    for i in range(len(tabM)):
        if tabM[i] == 0:#up
            reward = Qtable[convert(CS)][0]
            temp.append([reward, 0])
        if tabM[i] == 1:#down
            reward = Qtable[convert(CS)][1]
            temp.append([reward, 1])
        if tabM[i] == 2:#left
            reward = Qtable[convert(CS)][2]
            temp.append([reward, 2])
        if tabM[i] == 3:#right
            reward = Qtable[convert(CS)][3]
            temp.append([reward, 3])
    result = sorted(temp,reverse=True)
    return result[0][1]
            
def getKoor(CS):
    return CS[0],CS[1]

gamma = 0.9
def imReward(R,Q):#immidiate reward
    return R + gamma * max(Q)

generateRTable()
generateMove()
eps = 1
episode = 1000
for i in range(episode):#train the agent with Qlearning
    CS = IS#curent state
    while CS != GS:
        i = CS[0]
        j = CS[1]
        BS = [i,j]
        NS = rd.choice(move[convert(CS)])
        if NS == 0:
            i -= 1
            CS = [i,j]
            Qtable[convert(BS)][0] = imReward(board[CS[0],CS[1]],Qtable[convert(CS)])
        elif NS == 1:
            i += 1
            CS = [i,j]
            Qtable[convert(BS)][1] = imReward(board[CS[0],CS[1]],Qtable[convert(CS)])
        elif NS == 2:
            j -= 1
            CS = [i,j]
            Qtable[convert(BS)][2] = imReward(board[CS[0],CS[1]],Qtable[convert(CS)])
        elif NS == 3:
            j += 1
            CS = [i,j]
            Qtable[convert(BS)][3] = imReward(board[CS[0],CS[1]],Qtable[convert(CS)])
    print("Epsiode : ",eps)
    eps += 1

print()
print("Agen telah dilatih")
step = []
step.append([IS[0],IS[1]])
CS = IS
while CS != GS:
    NS = nextMove(move,CS)
    if NS == 0:#up
        CS[0] -= 1
    elif NS == 1:#down
        CS[0] += 1
    elif NS == 2:#left
        CS[1] -= 1
    elif NS == 3:#right
        CS[1] += 1
    step.append([CS[0],CS[1]])
    
reward = [] 
print("Optimum Policy :")
for i in step:
    print(i)
    a,b = getKoor(i)
    reward.append(board[a,b])
print()
print("Reward Total: ", sum(reward))



































# =============================================================================
# while CS != GS:
#     idx = convert(CS)
#     x = CS[0]
#     y = CS[1]
#     nextS = getNext(CS,move)
#     if nextS == 0:
#         x = x - 1
#         CS[0] = x
#         print(CS[0],CS[1])
#     elif nextS == 1:
#         x = x + 1
#         CS[0] = x
#         print(CS[0],CS[1])
#     elif nextS == 2:
#         y = y - 1
#         CS[1] = y
#         print(CS[0],CS[1])
#     elif nextS == 3:
#         y = y + 1
#         CS[1] = y
#         print(CS[0],CS[1])
# 
# =============================================================================





















#while CS != GS:
# =============================================================================
# idx = convert(GS)
# x = CS[0]
# y = CS[1]
# tempM = move[idx]
# tempR = []
# for i in range(len(tempM)):
#     if tempM[i] == 0:
#         x = x-1
#         ns = x,y
#         reward = imReward(board[x][y],Qtable[convert(ns)])
#         tempR.append([reward,x,y,0])
#     elif tempM[i] == 1:
#         x = x+1
#         ns = x,y
#         reward = imReward(board[x][y],Qtable[convert(ns)])
#         tempR.append([reward,x,y,1])
#     elif tempM[i] == 2:
#         y = y-1
#         ns = x,y
#         reward = imReward(board[x][y],Qtable[convert(ns)])
#         tempR.append([reward,x,y,2])
#     else:
#         y = y+1
#         ns = x,y
#         reward = imReward(board[x][y],Qtable[convert(ns)])
#         
# =============================================================================

    















































# =============================================================================
# while CS != GS:
#     idx = convert(CS)
#     x,y = CS[0],CS[1]
#     tempReward = []
#     tempMove = move[idx]
#     for i in range(len(tempMove)):
#         if tempMove[i] == 0:
#             x = x-1
#             ns = CS[0]-1, CS[1]
#             reward = imReward(board[x][y],Qtable[convert(ns)])
#             tempReward.append([reward,x,y,0])
#         elif tempMove[i] == 1:
#             x = x+1
#             ns = CS[0]+1, CS[1]
#             reward = imReward(board[x][y],Qtable[convert(ns)])
#             tempReward.append([reward,x,y,1])
#         elif tempMove[i] == 2:
#             y = y-1
#             ns = CS[0], CS[1]-1
#             reward = imReward(board[x][y],Qtable[convert(ns)])
#             tempReward.append([reward,x,y,2])
#         elif tempMove[i] == 3:
#             y = y+1
#             ns = CS[0], CS[1]+1
#             reward = imReward(board[x][y],Qtable[convert(ns)])
#             tempReward.append([reward,x,y,3])
#     result = sorted(tempReward,reverse=True)
#     print(result)
#     if result[0][3] == 0:
#         Qtable[convert(CS)][0] = float(result[0][0])
#         #print(CS)
#         CS[0],CS[1] = result[0][1],result[0][2]
#         print(CS)
#     elif result[0][3] == 1:
#         Qtable[convert(CS)][0] = float(result[0][0])
#         #print(CS)
#         CS[0],CS[1] = result[0][1],result[0][2]
#         print(CS)
#     elif result[0][3] == 2:
#         Qtable[convert(CS)][0] = float(result[0][0])
#         #print(CS)
#         CS[0],CS[1] = result[0][1],result[0][2]
#         print(CS)
#     elif result[0][3] == 3:
#         Qtable[convert(CS)][0] = float(result[0][0])
#         #print(CS)
#         CS[0],CS[1] = result[0][1],result[0][2]
#         print(CS)
# =============================================================================
        
        
        
        
        
        
        
        
#print(Qtable)
# =============================================================================
#     if result[0][3] == 0:
#         Qtable[convert(CS),0] = float(result[0][0])
#         CS[0] = result[0][1]
#         CS[1] = result[0][2]
#         print(CS)
#     elif result[0][3] == 1:
#         Qtable[convert(CS),1] = float(result[0][0])
#         CS[0] = result[0][1]
#         CS[1] = result[0][2]
#         print(CS)
#     elif result[0][3] == 2:
#         Qtable[convert(CS),2] = float(result[0][0])
#         CS[0] = result[0][1]
#         CS[1] = result[0][2]
#         print(CS)
#     else:
#         Qtable[convert(CS),3] = float(result[0][0])
#         CS[0] = result[0][1]
#         CS[1] = result[0][2]
#         print(CS)
# =============================================================================

    
            






























