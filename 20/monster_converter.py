import enum

a = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

class enumVal(enum.Enum):
    X = '#'
    O = '.'
    A = ' '



monster = []
for i in a.split("\n"):
    if not i:
        continue
    monster.append([enumVal(j).name for j in i])

monster_x_count = sum([val.count('X') for val in monster])
print(monster)
print(monster_x_count)


b = """
O X O X O O X O X X X O O O X O X O X O O X X X X X 

X X X O O O O X O O X O O O O X O O O X O O O O O O 

X X O X X O X X O X O X O X O O X X X X X X X O O O 

X X X O X X X X X X O O O X O X X X X X X O X O O X 

X X O X O O O O X X O X X O X X X O X O O O X O X X 

O O O X X X X X X X X X O X O O O X O X X X X X O X 

O O O O X O O X X O O O X X O O X O O X O X X X O O 

O X X X X O O O X X O O X O O O O O O X O O O O O O 

O X X O O O X X O O X X O X O O X O O X O X X X O O 

X O O X O X X O O O X O O X X X O X X O X X O O O O 

X O X X X X O O O X O X X X X O X O O X O X X X O O 

X X X O X O X O O O O X O X X X X X X X O X O O X X 

X O X X X X O O O O O X X O O X X O X X X X X X O X 

X X O O X X O X O O O O X O O O X X O X O X O X O O 

O O O X O O X O X O X O X O X X O X O X X X O X X X 

O X O X O O O O O X O X X O X O O X O X X X O X X O 

X X X O X O O O O X O O X O X X O O X X X X X X O O 

O O X O X O X O X X X O X X O X O O X X O O O X X X 

O X O X O X X X O O X X O X X O X X O O X O X X O O 

O X X X X O X X X X O X O O O X X O X O X O O X O X 

O O X O X O O X O O O X O X O X O O X X X X O X X X 

X O O X X X X O X O O X O X O X O X X X X O X X X O 

X X X X X O O X X X X X X O O O X O X X O O O O X X 

X O X X O O X O O O X O O O X O O O X X X X O O O X 

O X O X X X O O O X X O O X X O O O X X X X O X X O 

O O O X X X O O O O X X O O O X O O O O X O O X X X 
"""

monster = []
for i in b.split("\n"):
    if not i:
        continue
    monster.append([j for j in i.split(' ') if j])

monster_x_count = sum([val.count('X') for val in monster])
print(monster)
print(monster_x_count)