import re
from collections import deque
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def part_1(data):
    toggles = []
    for i, line in enumerate(data):
        # Binary representatioon of indicator_goal
        indicator_goal = ''.join('1' if x == '#' else '0' for x in re.findall(r"[\.|#]+", line)[0])
        # Making binary representations of the schematics and converting to base 10
        schematics = list(map(lambda s: tuple(map(int, s.split(','))), re.findall(r"\(([,|\d]+)\)", line)))
        schematics = set([int("".join(["1" if i in s else "0" for i in range(len(indicator_goal))]),2) for s in schematics])
        # Converting the indicator goal to base 10 aswell
        indicator_goal = int(indicator_goal,2)

        # Now an XOR will be able to make the transformations

        known_states = {0}
        indicators = deque()

        flag = True
        for s in schematics:
            if s == indicator_goal:
                toggles.append(1)
                flag = False
                break
            indicators.append((s, {s}))
            known_states.add(s)

        while flag:
            indicator, transformations = indicators.popleft()
            for s in schematics - transformations:
                state = indicator^s
                if state in known_states:
                    continue
                if state == indicator_goal:
                    toggles.append(len(transformations)+1)
                    flag = False
                    break
                indicators.append((state, transformations | {s}))
                known_states.add(state)

    return sum(toggles)





def part_2(data):
    toggles = []
    for line in data:
        joltage_goal = np.array(list(map(int,re.findall(r"\{([,|(\d)]+)\}", line)[0].split(","))))
        schematics = list(map(lambda s: tuple(map(int, s.split(','))), re.findall(r"\(([,|\d]+)\)", line)))
        schematics_v = np.ndarray(shape=(len(schematics),len(joltage_goal)), dtype=int)

        # Converting schematics to vector representation
        for i_s, s in enumerate(schematics):
            v = np.zeros(shape=len(joltage_goal),dtype=int)
            for i in s:
                v[i] = 1
            schematics_v[i_s] = v

        # Modeling this as ILP(Integer Linear Programming)
        # If each schematic is a vector v and the target joltage is a vector c then:
        # x1*v1 + x2*v2 + x3*v3 + ... xn*vn = [c1, c2, c3, ... cn]
        # Where each x is the number of times a schematic vector needs to be added to become the target joltage vector
        # The objective then becomes to minimize x1 + x2 + x3 + ... xn
        # Since we cant remove a vector once it is added we must set a bound x >= 0
        # We can't use a fractional amount of a schematic, so all variables must be integers (integrality constraint)


        # Transposing the schematic vectors to effectively make a matrix like this:
        # [v1_1, v2_1, v3_1, ... vn_1]
        # [v1_2, v2_2, v3_2, ... vn_2]
        # [v1_3, v2_3, v3_3, ... vn_2]
        schematics_v_t = schematics_v.transpose()

        # The objective coefficients which is simply the coefficient of the x which is one for all in this problem
        objective_coefficients = np.ones(shape=len(schematics), dtype=int)

        # Settig up the bounds to make sure we keep x >= 0
        bounds = Bounds(lb=0, ub=np.inf)
        # This effectively squeezes the solution space to be exactly the joltage_goal, making sure we only get the correct solution
        constraints = LinearConstraint(schematics_v_t, joltage_goal, joltage_goal)
        # Enforcing integrality(Only integers allowed) Each one forces that x to be an integer
        integrality = np.ones(shape=len(schematics),dtype=int)

        # Solving the ILP
        solution = milp(objective_coefficients, integrality=integrality, bounds=bounds, constraints=constraints)
        
        toggles.append(solution.fun)
    
    return int(sum(toggles))

if __name__=='__main__':
    with open('day_10/data.txt') as f:
        data = f.read().splitlines()


    print(part_1(data)) # 425
    print(part_2(data)) # 15883

