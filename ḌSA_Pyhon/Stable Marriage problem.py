def stable_marriage(n, men_preferences, women_preferences):
  
    men_status = {man: -1 for man in range(n)}
    women_status = {woman: -1 for woman in range(n)}
    engaged_count = 0

    while engaged_count < n:
        for man in range(n):
            if men_status[man] == -1:  
                woman = men_preferences[man][men_status[man] + 1]
                men_status[man] += 1

               
                if women_status[woman] == -1:
                    women_status[woman] = man
                    engaged_count += 1
                else:
                   
                    current_engaged_man = women_status[woman]
                    if women_preferences[woman].index(man) < women_preferences[woman].index(current_engaged_man):
                        men_status[current_engaged_man] = -1
                        women_status[woman] = man
                    else:
                        men_status[man] -= 1

    return women_status


n = 4 
men_preferences = [[1, 0, 2, 3], [3, 2, 1, 0], [0, 1, 2, 3], [1, 0, 3, 2]]
women_preferences = [[2, 1, 0, 3], [1, 2, 3, 0], [3, 0, 1, 2], [2, 1, 3, 0]]

stable_matching = stable_marriage(n, men_preferences, women_preferences)
print("Stable matching:", stable_matching)
