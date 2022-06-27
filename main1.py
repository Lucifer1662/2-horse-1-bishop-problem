from PriorityQueue import PriorityQueue
from heapq import heappop,heappush

def addTup(x1,x2):
    return (x1[0]+x2[0], x1[1]+x2[1])

def difTup(x1,x2):
    return (x1[0]-x2[0], x1[1]-x2[1])

def absTup(x1):
    return (abs(x1[0]), abs(x1[1]))

horse_moves = [
        (2,1),
        (-2,-1),
        (-2,1),
        (2,-1),

        (1,2),
        (-1,2),
        (-1,-2),
        (1,-2)
    ]

def path(last, cameFrom):
    ps = [last]
    while(last in cameFrom):
        next = cameFrom[last]
        last = next
        ps.append(next)
    ps.reverse()
    return ps


iteration = 0

def h(pos,des):
    dif = absTup(difTup(des,pos))
    return (max(dif)//2)

def valid(pos, b):
    return (pos[0] >= 0 and pos[1] >= 0 and pos[0] <= 10000 and pos[1] <= 10000)

#takes in start horse position, the end horst position,
#the bishops position,
#and outputs the minimum number of moves
def bishopProblem(h1,h2,b):
    global iteration
    moves = []
    for h_move in horse_moves:
        moves.append([h_move])
    
    visited = dict()

    queue = list()
    heappush(queue,(h(h1,h2),0,h1))
    visited[h1]=0
    cameFrom = dict()
    while(True):

        (h_dis, c_dis ,current_pos) = heappop(queue)
        
        iteration += 1

        if(current_pos == h2):
            return path(current_pos, cameFrom)

        new_c_dis = c_dis+1
        for h_move in horse_moves:
            new_move = addTup(h_move,current_pos)
            if(valid(new_move, b)):
                if(new_move not in visited or visited[new_move] > new_c_dis):
                    cameFrom[new_move] = current_pos
                    visited[new_move] = new_c_dis
                    new_h_dis = new_c_dis + h(new_move, h2)
                    heappush(queue, (new_h_dis,new_c_dis,new_move))


moves = bishopProblem((0,0),(1000,555),(0,0))
print(len(moves))
print(moves)
print(iteration)
