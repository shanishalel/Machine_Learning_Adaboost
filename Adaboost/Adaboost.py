# got some help from github user we found https://github.com/eliahusatat/Machine-Learning
import doctest
import itertools
import random
import math

import numpy as np

from Adaboost.Line import Line
from Adaboost.Point import Point_for_HC
from Adaboost.H import H

"""
p3=Point_for_HC("5  1   -6")
p4=Point_for_HC("4  -1  4")
p5=Point_for_HC("2  1   -8")
points=[]
points.append(p3)
points.append(p4)
points.append(p5)
line=Line((Point_for_HC("0   -1   -4"),Point_for_HC("2   1   0")))
print(line.is_right(p3))
points1=[]
points1.append(p4)
points1.append(p3)
"""

    # rank the error of the line (if we ronge about the label we add the weight to the rate)
def line_error(line, points):
    rate=0
    for p in points:
        if(line.is_right(p)==False):  #made an error
            rate+=p.weight
            if(p.weight==0):
                print("the w is :{}".format(p.weight))
    if(rate==0):
        return 0.000000001
    else:
        return rate



#this function return the best rule (line) on the points
def best_line(points):
    best = Line((points[0], points[1]))
    best_rate =line_error(best, points)
    for p in itertools.combinations(points, 2):
        temp = Line(p)
        temp_rate = line_error(temp, points)
        if (temp_rate < best_rate):
            best = temp
            best_rate = temp_rate
    return best



def adaboost(points,rules=8):
    sum=0
    best_rules=[]
    weight_rules=[]  #weight=alpha_t
    for i in range (0,rules) :
        best_r=best_line(points)  #find the best rule
        best_rules.append(best_r)
        et=line_error(best_r,points)  #getting the error on the points
        num=(1-et)/et
        alpha_t=0.5*(np.log(num))  #np=numpy
        weight_rules.append(alpha_t)
        for p in points:
            if(best_r.is_right(p)==False):
                p.weight=p.weight*(np.math.e ** (alpha_t))
            else:
                p.weight=p.weight*(np.math.e ** (-alpha_t))
            sum+=p.weight
        for p in points: #normalized the point weight
            p.weight=p.weight/sum

    ans= H( best_rules,weight_rules,8)

    for p in points:
        p.weight=1/len(points)

    return ans


def run_train(points, rules=8,times=10):
    learn_ans=[]
    test_ans=[]
    for i in range(1, rules + 1):
        multi_sum = 0
        multi_sum2 = 0
        for j in range(times):
            learn = []
            test = []
            #filling the 2 list above with the points we get in random way
            for p in points:
                rand = random.randint(0, 1)
                if (len(learn) >= 65):
                    test.append(p)
                else:
                    if (len(test) >= 65):
                        learn.append(p)
                    else:
                        if (rand == 0):
                            test.append(p)
                        else:
                            learn.append(p)
            ans_learn = adaboost(learn)
            ans_test=adaboost(test)
            rate = 0
            rate2=0
            for p in learn:
                if ans_learn.is_right(p):
                    rate += 1
            multi_sum += (rate / len(test) * 100)

            for p2 in test:
                if ans_test.is_right(p2):
                    rate2 += 1
            multi_sum2 += (rate2 / len(test) * 100)

        test_ans.append(multi_sum2)
        learn_ans.append(multi_sum)

    print("learn :")
    for i in range (rules):
        print("the rate of success for {} is {} percent ".format(i,learn_ans[i]/times ))


    print("test :")
    for i in range (rules):
        print("the rate of success for {} is {} percent ".format(i, test_ans[i]/times))


if __name__ == '__main__':

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

    f = open("HC_Body_Temperature.txt", "r")
    points = []
    for x in f:
        points.append(Point_for_HC(x))

    adaboost(points,8)
    run_train(points, 8, 10)




