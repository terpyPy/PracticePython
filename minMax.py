# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math
# cur game move: curDepth, that nodes ordinal pos, max player goes first,
# value of node: scores list 
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]
    # the next case is maxTurn reached

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))
scores = [3, 5, 2, 9, 12, 5, 23, 25]
treeDepth = math.log(len(scores), 2)
print('the optimal value is :', end='')
print(minimax(0, 0, True, scores, treeDepth))