import doctest
from Line import Line
from Point import Point_for_HC

class H():

    def __init__(self,best_rules,weight_rules, rules=8 ):
        self.best_rules=best_rules
        self.weight_rules=weight_rules
        self.rules=rules

    #return sign on one point
    def sign(self,p):
        sum=0
        for i in range (self.rules):
            if(self.best_rules[i].is_low(p)):
                sum-=self.weight_rules[i]
            else:
                sum+=self.weight_rules[i]
        if(sum>=0):
            return 1
        else:
            return -1

    def is_right(self,p):
        if(self.sign(p)==p.gender):
            return True
        else:
            return False

