

def addTup(x1,x2):
    return (x1[0]+x2[0], x1[1]+x2[1])


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

iteration = 0

#takes in start horse position, the end horst position,
#the bishops position,
#and outputs the minimum number of moves
def bishopProblem(h1,h2,b):
    global iteration
    moves = [[h1]]
    
    visited = set()
    while(True):
        h_moves = moves.pop(0)
        # print(h_moves)
        iteration+=1
        current_h_move = h_moves[-1]
        if(current_h_move == h2):
            return h_moves

        for h_move in horse_moves:
            new_h_moves = list(h_moves)
            new_move = addTup(h_move,current_h_move)
            if(new_move not in visited):
                new_h_moves.append(new_move)
                moves.append(new_h_moves)
                visited.add(new_move)
        # print()


moves = bishopProblem((0,0),(1000,555),(0,0))
print(len(moves))
print(moves)
print(iteration)

