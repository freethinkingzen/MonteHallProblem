
# This program test the results of the Monte Hall Problem
# since the results are counterintuitive to most people

import random


ROUNDS = 1000

if __name__ =="__main__":

    keep_door = 0       # Successful rounds when keeping door choice
    switch_door = 0     # Successful rounds when switching door choice

    for i in range(ROUNDS): # Perform number of rounds based on constant
        
        doors = [0] * 3
        prize_door = random.randrange(0,3)
        chosen_door = random.randrange(0,3)
        doors[prize_door] = 1
        
        zonk_doors = [i for i, x in enumerate(doors) if x == 0 if i != chosen_door]
        montes_door = random.choice(zonk_doors)

        if(prize_door == chosen_door):
            keep_door += 1
        
        switch_to = set([0,1,2]).difference([chosen_door, montes_door])
        switch_to = switch_to.pop()

        if(prize_door == switch_to):
            switch_door += 1
        
    keep_success = (keep_door/ROUNDS) * 100
    switch_success = (switch_door/ROUNDS) * 100

    print("ROUNDS:", ROUNDS)
    print("Keep: {:0.2f}%".format(keep_success))
    print("Switch: {:0.2f}%".format(switch_success))


