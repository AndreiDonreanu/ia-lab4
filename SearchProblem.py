from idlelib.debugobj_r import remote_object_tree_item


class SearchProblem:

    def __str__(self):
        return "("+"%s"%self.x_goal+",""%s)"%self.y_goal

    def __repr__(self):
        return "("+"%s"%self.x_goal+",""%s)"%self.y_goal

    def __init__(self,n,x_goal,y_goal):
        self.n = n
        self.x_goal = x_goal
        self.y_goal = y_goal

    def get_initial_state(self):
        return (self.x_goal,self.y_goal)

    def is_goal(self, state):
        return state[0]==self.x_goal and state[1]==self.y_goal


    def get_successors(self, state):
        posibleactions=[]
        if state[0]-1>=0:
            posibleactions.append(("UP",(state[0]-1,state[1])))

        if state[0]+1<=self.n:
            posibleactions.append(("DOWN",(state[0]+1,state[1])))

        if state[1]-1>=0:
            posibleactions.append(("LEFT",(state[0],state[1]-1)))

        if state[1]+1<=self.n:
            posibleactions.append(("RIGHT",(state[0],state[1]+1)))

        return posibleactions

    def do_path(self,path,state):

        x=state[0]
        y=state[1]

        for i in path:
          if i=="UP" and x>=0:
              x-=1
          if i=="DOWN" and x<=self.n:
              x+=1
          if i=="LEFT" and y>=0:
              y-=1
          if i=="RIGHT" and y<=self.n:
              y+=1

        print((x,y))
        return self.is_goal((x,y))