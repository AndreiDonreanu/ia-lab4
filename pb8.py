from re import search

from SearchProblem import SearchProblem
import random

from pb1 import lista



def get_random_action(n,stare):

    dumy=SearchProblem(n,0,0)

    vecini=dumy.get_successors(stare)

    randomint=random.randint(0,len(vecini)-1)

    return vecini[randomint][0]












stareinitiala=SearchProblem(5,1,1)

starefinala=SearchProblem(5,3,4)

print("%s"%stareinitiala+" to " + "%s"%starefinala)

path1=["UP","DOWN","DOWN","RIGHT","RIGHT"]

print(starefinala.do_path(path1,stareinitiala.get_initial_state()))



actiune=get_random_action(5,stareinitiala.get_initial_state())

print(actiune)

