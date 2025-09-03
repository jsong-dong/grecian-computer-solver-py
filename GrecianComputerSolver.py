#NOTES: gear0 is the biggest gear on the bottom, gear4 is the smallest gear on the top
#Each tuple represents a column on the gear
#The first element of each tuple is the number closest to the center, and the last element of each tuple is the number furthest away
#The number 0 represents the gear's position being empty

#Feel free to edit these gears and make your own Grecian puzzle!

gear0 = [
(11,5,4,3),
(14,6,6,4),
(11,7,6,12),
(14,8,3,2),
(11,9,3,5),
(14,10,14,10),
(14,11,14,7),
(11,12,21,16),
(14,13,21,8),
(11,14,9,7),
(14,15,9,8),
(11,4,4,8)
]

gear1 = [
(16,9,3,10),
(2,0,12,0),
(7,9,3,1),
(0,20,26,0),
(9,12,6,9),
(0,3,0,0),
(7,6,2,12),
(14,0,13,0),
(11,14,9,6),
(0,12,0,0),
(8,3,17,10),
(0,8,19,0)
]

gear2 = [
(13,6,0,0),
(9,15,10,0),
(7,4,0,0),
(13,9,8,0),
(21,18,0,0),
(17,11,22,0),
(4,26,0,0),
(5,14,16,0),
(0,1,0,0),
(7,12,9,0),
(8,0,0,0),
(9,21,5,0),
]

gear3 = [
(3,0,0,0),
(0,7,0,0),
(6,15,0,0),
(0,0,0,0),
(11,0,0,0),
(11,14,0,0),
(6,0,0,0),
(11,9,0,0),
(0,0,0,0),
(6,12,0,0),
(17,0,0,0),
(4,7,0,0)
]

gear4 = [
(3,0,0,0),
(0,0,0,0),
(6,0,0,0),
(0,0,0,0),
(10,0,0,0),
(0,0,0,0),
(7,0,0,0),
(0,0,0,0),
(15,0,0,0),
(0,0,0,0),
(8,0,0,0),
(0,0,0,0)
]


def turn(gear,n):
    """ Returns the gear turned counterclockwise by n columns
        gear: a list of tuples
        n: a nonnegative integer
    """
    return gear[n:]+gear[:n]

def display(slot0,slot1,slot2,slot3,slot4):
    """ Returns the number displayed on the gear in the mechanical puzzle
        slot0, slot1, slot2, slot3, slot4: a nonnegative integer
    """
    slots = (slot4,slot3,slot2,slot1,slot0)
    for num in slots:
        if num != 0:
            return num
        
def sum_column(clmn0,clmn1,clmn2,clmn3,clmn4): 
    """ Returns the sum of the displayed numbers on one column on the gear
        clmn0,clmn1,clmn2,clmn3,clmn4: a tuple of length 4
    """
    sum_clmn = 0
    for i in range(0,4):
        sum_clmn += display(clmn0[i],clmn1[i],clmn2[i],clmn3[i],clmn4[i])
    return sum_clmn

def num_sum_forty_two(gear0,gear1,gear2,gear3,gear4): #returns number of columns that sum to 42
    """ Returns the number of columns in the puzzle that sum to 42
        gear0,gear1,gear2,gear3,gear4: a list with 12 tuples
    """
    sum_num = 0
    for i in range(0,12):
        if sum_column(gear0[i],gear1[i],gear2[i],gear3[i],gear4[i]) == 42:
            sum_num += 1
    return sum_num

def solve(gear0,gear1,gear2,gear3,gear4):
    """ Returns a list that indicates how many times each gear must be turned counterclockwise to solve the puzzle
        The first element of the returned list applies to the bottommost gear, and the last element applies to the topmost gear
        gear0,gear1,gear2,gear3,gear4: a list with 12 tuples
    """
    for b in range(0,12):
        for c in range(0,12):
            for d in range(0,12):
                for e in range(0,12):
                    if num_sum_forty_two(gear0,turn(gear1,b),turn(gear2,c),turn(gear3,d),turn(gear4,e)) == 12:
                        return [0,b,c,d,e]

#we solve the puzzle!!! \(^ O ^)/
print("Number of counterclockwise turns:", solve(gear0,gear1,gear2,gear3,gear4))
print()
print("Full solution:")
print(gear0)
print(turn(gear1,11))
print(turn(gear2,2))
print(turn(gear3,7))
print(turn(gear4,7))
