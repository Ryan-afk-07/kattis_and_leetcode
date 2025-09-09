grid = []
n = int(input())
while True:
    line = input()
    if line:
        grid.append(list(line))
    else:
        break

print(grid)
print(type(n))
spy_house_dict = {}
''' similar to how it was done for the puzzle question, placing the entire map into a list of lists,
then finding out the conditions or the difference in coordinates from a Spy (S) to a House (H)'''

for i in range(n):
    for j in range(n):
        if grid[i][j] == ".":
            pass
        elif "H" in spy_house_dict and grid[i][j] == "H":
            spy_house_dict[grid[i][j]].append([i,j])
        elif "S" in spy_house_dict and grid[i][j] == "S":
            spy_house_dict[grid[i][j]].append([i,j])
        elif grid[i][j] == "S":
            spy_house_dict[grid[i][j]] = []
            spy_house_dict[grid[i][j]].append([i,j])
        elif grid[i][j] == "H":
            spy_house_dict[grid[i][j]] = []
            spy_house_dict[grid[i][j]].append([i,j])
        else:
            pass

print(spy_house_dict.items())
'''ensuring that for each Spy, their distance to each House is considered'''
max_man = []
for i in spy_house_dict["S"]:
    man_dist = []
    for j in spy_house_dict["H"]:
        man_dist.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
    max_man.append(min(man_dist))

print(max(max_man))
        
