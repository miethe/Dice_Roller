import random

class Dice_Roller:

    def roll_n_d_x(self, n_count, x_die_size):
        rolls = []
        for _ in range(n_count):
            #randrange is [x,y)
            rolls.append(random.randrange(1,x_die_size+1))
        return rolls
    
    def drop_lowest(self, rolls):
        if not rolls:
            return rolls
        rolls.sort()
        return rolls[1:]
    
    def drop_low_and_tally(self, rolls):
        return sum(drop_lowest(rolls))

    def roll_ndx_y_times(self, times_rolled, die_size, total_iterations, drop_lowest = False):
        total_rolls = []
        if times_rolled is 0 or die_size is 0 or total_iterations is 0:
            return total_rolls
        
        for _ in range(total_iterations):
            rolls = self.roll_n_d_x(times_rolled, die_size)
            total_rolls.append(self.drop_low_and_tally(rolls))
            
        if drop_lowest:
            total_rolls.sort()
            return total_rolls[1:]
        else:
            return total_rolls

def _average(lst):
    return sum(lst) / len(lst)
