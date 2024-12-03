template_puzzle = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "."]]


puzzle = []
while True:
    line = input()
    print(line)
    if line:
        puzzle.append(list(line))
    else:
        break

letter_dict = {}
#placing the letters which are out of place into a dict, and noting down their present positions     
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == ".":
            pass
        elif puzzle[i][j] != template_puzzle[i][j]:
            letter_dict[puzzle[i][j]] = list([i, j])
        else:
            pass


letters = [str(key) for key in letter_dict.keys()]
#finding out the difference between their noted new placements and the ones in template
for i in range(len(template_puzzle)):
    for j in range(len(template_puzzle[i])):
        if template_puzzle[i][j] in letters:
            letter_dict[template_puzzle[i][j]][0] -= i
            letter_dict[template_puzzle[i][j]][1] -= j

scatter = 0
for key, value in letter_dict.items():
    scatter += abs(value[0])
    scatter += abs(value[1])

print(letter_dict)
print(scatter)
