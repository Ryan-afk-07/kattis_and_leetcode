class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Idea: pointer problem. Follow the rules
        1. Path MUST start with a single slash. So rule will be that if there is no slash at the start, add a slash. If there are too many. Remove those slashes. For this set 2 pointers. 1 at the first index. Then check for more slashes. If there are, continue the pointer. Continue until there is no more slashes. Then slice the extra slashes, and place both pointers as the same
        2. For single and double periods. Remove them. Have a count variable to check. 
        """
        if path[-1] != "/":
            path = path + "/"
        prev = 0
        end = 1
        current_direc = ""
        parent_direc = ""
        while end < len(path):
            #scenario1: if first value is not a slash, add a slash
            if path[prev] != '/' and prev == 0:
                path = '/' + path
                prev = 0
                end = 1
            
            if "/" not in path[end:]:
                break
            #letting end pointer go to the next slash value
            while path[end] != '/':
                #print('yes')
                current_direc = current_direc + path[end]
                end += 1
                #print(end)
            
            #scenario2: if the current_direc is None - likely duplicate '/' string. remove it. Same for '.' - just one dot
            if current_direc == "" or current_direc == ".":
                path = path[:prev+1] + path[end+1:]
                end = prev + 1
                current_direc = ""
            
            #scenario3: if current_direc is "..". check if it has a previous directory. If it has, remove it. If not, just remove the two dots
            elif current_direc == "..":
                if parent_direc == "":
                    path = path[:prev+1] + path[end+1:]
                    current_direc = ""
                    end = prev + 1
                    #print('2',path, prev, end)
            #scenario4: there is a previous directory. Make sure to slice away that previous directory, and then realign the 2 pointers and get back the earlier directory before the parent directory that has been removed.
                else:
                    path = path[:prev - len(parent_direc)] + path[end+1:]
                    prev = prev - len(parent_direc) - 1
                    end = prev + 1
                    temp_prev = prev - 1
                    #print('3',path, prev, end)
                    parent_direc = ""
                    #getting back the parent directory of the deleted parent directory. In case there are duplicate .. (i.e. /../../)
                    while path[temp_prev] != "/":
                        parent_direc = path[temp_prev] + parent_direc
                        temp_prev -= 1
                    current_direc = ""
            else:
                parent_direc = current_direc
                current_direc = ""
                prev = end
                end += 1
            #print(path, parent_direc, "Parent", current_direc, "Current", prev, end)
        if path[-1] == "/" and len(path) > 1:
            path = path[:len(path)-1]
        return path


        """
        There is a solid solution. Remember the .SPLIT() FUNCTION!?
        God damn it. HAHA. This will make things easier alr.
        Use the split to split up all the directory and then list them in a list.
        If the current cell index is a '..', then pop then previous one. FK SAKE. 
        At the end, just join all the rest tgt
        """

            





                
            
        