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
    return (pos[0] >= 0 and pos[1] >= 0 and pos[0] <= 1000 and pos[1] <= 1000)


def a_star(queue:list, cameFrom:dict, visited:dict, goal, b):
        global iteration
        (h_dis, c_dis ,current_pos) = heappop(queue)
        
        iteration += 1

        new_c_dis = c_dis+1
        new_moves = []
        for h_move in horse_moves:
            new_move = addTup(h_move,current_pos)
            if(valid(new_move, b)):
                if(new_move not in visited or visited[new_move] > new_c_dis):
                    cameFrom[new_move] = current_pos
                    visited[new_move] = new_c_dis
                    new_h_dis = new_c_dis + h(new_move, goal)
                    heappush(queue, (new_h_dis,new_c_dis,new_move))
                    new_moves.append(new_move)
        return new_moves


#takes in start horse position, the end horst position,
#the bishops position,
#and outputs the minimum number of moves
def bishopProblem(h1,h2,b):
    global iteration
    moves = []
    for h_move in horse_moves:
        moves.append([h_move])
    
    f_visited = dict()    
    f_visited[h1]=0
    f_cameFrom = dict()
    f_queue = list()
    heappush(f_queue,(h(h1,h2),0,h1))

    b_visited = dict()    
    b_visited[h2]=0
    b_cameFrom = dict()
    b_queue = list()
    heappush(b_queue,(h(h2,h1),0,h2))

    while True:
        new_moves_forward = a_star(f_queue, f_cameFrom, f_visited, h2,b)
        new_moves_backward = a_star(b_queue, b_cameFrom, b_visited, h1,b)

        for new_move in new_moves_forward:
            if(new_move in b_visited):
                print(new_move)

                f_path = path(new_move, f_cameFrom)
                b_path = path(new_move, b_cameFrom)
                b_path.reverse()
                f_path.extend(b_path)
                return f_path

        for new_move in new_moves_backward:
            if(new_move in f_visited):
                print(new_move)

                f_path = path(new_move, f_cameFrom)
                b_path = path(new_move, b_cameFrom)
                b_path.reverse()
                f_path.extend(b_path)
                return f_path

        



moves = bishopProblem((0,0),(1000,555),(0,0))
print(len(moves))
print(moves)
print(iteration)
