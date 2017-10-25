import random as rd
#get grid
def grid_creator(n):
    grid = []
    temp = []
    with open('read.txt') as f:
        temp = f.read().splitlines() 
    for i in range(0,n):
        grid.append([])
    for i,string in enumerate(temp):
            for j in string:
                grid[i].append(j)   
    return grid


def grid_traverser(grid):
    n = len(grid)
    intersect = []
    for i,row in enumerate(grid):
    	for j,elem in enumerate(row):
    		try:
    			if elem == "_":
    				if i==0 and j==0:
    					if (grid[i][j+1]=="_" and grid[i+1][j]=="_"):
    						intersect.append((i,j))

    				elif i == 0  and (j != 0 and j!= n-1):
    					if (grid[i][j+1]=="_" and grid[i+1][j]=="_") or (grid[i][j-1]=="_" and grid[i+1][j]=="_") :
    						intersect.append((i,j))
    				
    				elif i == 0 and j == n-1:
    					if(grid[i][j-1]=="_" and grid[i+1][j]=="_"):
    						intersect.append((i,j))
    				elif i==n-1 and j==0:
    					if (grid[i][j+1]=="_" and grid[i-1][j]=="_"):
    						intersect.append((i,j))

    				elif i == n-1  and (j != 0 and j!= n-1):
    					if (grid[i][j+1]=="_" and grid[i-1][j]=="_") or (grid[i][j-1]=="_" and grid[i-1][j]=="_") :
    						intersect.append((i,j))
    				
    				elif i == n-1 and j == n-1:
    					if(grid[i][j-1]=="_" and grid[i-1][j]=="_"):
    						intersect.append((i,j))
    				elif j == 0 and (i != 0 and i!= n-1):
    					if (grid[i-1][j]=="_" and grid[i][j+1]=="_") or (grid[i+1][j]=="_" and grid[i][j+1]=="_"):
    						intersect.append((i,j))
    				elif j == n-1 and (i != 0 and i!= n-1):
    					if (grid[i-1][j]=="_" and grid[i][j-1]=="_") or (grid[i+1][j]=="_" and grid[i][j-1]=="_"):
    						intersect.append((i,j))
    				elif (grid[i][j+1]=="_" and grid[i+1][j]=="_") or (grid[i][j+1]=="_" and grid[i-1][j]=="_") or (grid[i][j-1]=="_" and grid[i+1][j]=="_") or (grid[i][j-1]=="_" and grid[i-1][j]=="_"):
    					intersect.append((i,j))
    		except IndexError:
    			continue
    return intersect





string_list = ['monk','komodo','concremat','casi','miamis','sachs','cunjam','tallmam','hatim']

def left_counter(grid,coord):
        counter_hl = 1
        i  = 1
        temp = coord
        while temp[1] != 0 and grid[temp[0]][temp[1]-1] != '+' :
        		temp = (coord[0],coord[1]-i)
        		counter_hl = counter_hl + 1
        		i = i + 1
        return ((temp[0],temp[1]),counter_hl)

def right_counter(grid,coord):
        counter_hr = 0
        i  = 2
        try:
        	temp = grid[coord[0]][coord[1]+1]
        except:
        	return counter_hr
        while temp != '+':
            try:
               counter_hr = counter_hr + 1
               temp = grid[coord[0]][coord[1]+i]
               
               i = i + 1
            except IndexError:
               break
        return counter_hr


def top_counter(grid,coord):
        counter_vt = 1
        i  = 1
        temp = coord
        while temp[0] != 0 and grid[temp[0]-1][temp[1]] != '+' :
        		temp = (coord[0]-i,coord[1])
        		counter_vt = counter_vt + 1
        		i = i + 1
        return ((temp[0],temp[1]),counter_vt)

def down_counter(grid,coord):
        counter_vd = 0
        i  = 2
        try:
        	temp = grid[coord[0]+1][coord[1]]
        except:
        	return counter_vd
        while temp != '+':
        	try:
        		counter_vd = counter_vd + 1
        		temp = grid[coord[0]+i][coord[1]]
        		i = i + 1
        	except IndexError:
        		break
        return counter_vd

    




def fill_up(grid,string_list):
    ints = grid_traverser(grid)
    x = True
    while x == True:
    	rd.shuffle(ints)
    	for coord in ints:
    			top_end , vt = top_counter(grid,coord)
    			vd = down_counter(grid,coord)
    			left_end,hl = left_counter(grid,coord)
    			hr = right_counter(grid,coord)
    			verti = vt + vd
    			hori = hr + hl
    			for_fit_hori = []
    			for_fit_verti = []
    			for string in string_list:
    				if grid[top_end[0]][top_end[1]].isalpha():
    					if len(string) == verti and string[0] == grid[top_end[0]][top_end[1]]:
    						for_fit_verti.append(string)
    						
    				
    				if grid[left_end[0]][left_end[1]].isalpha():
    					if len(string) == hori and string[0] == grid[left_end[0]][left_end[1]]:
    						for_fit_hori.append(string)
    						


    				elif len(string) == verti:
    					if string not in for_fit_verti:
    						for_fit_verti.append(string)
    						
    				elif len(string) == hori:
    					if string not in for_fit_hori:
    						for_fit_hori.append(string)
    						
    			counter = 0			
    			for verti_str in for_fit_verti:
    				for hori_str in for_fit_hori:
    					if hori_str[coord[1] - left_end[1]] == verti_str[coord[0] - top_end[0]]:
    						counter = counter + 1
    						if counter == 1:
    							for i in range(0,len(verti_str)):
    								grid[top_end[0]+i][top_end[1]] = verti_str[i]
    							for i in range(0,len(hori_str)):
    								grid[left_end[0]][left_end[1]+i] = hori_str[i]
    						else:
    							break
    	else:
    		x = False						
    	
    return grid

solved = fill_up(grid_creator(10),string_list)

for row in solved:
	for elem in row:
		print(elem,end = " ")
	print('\n')


