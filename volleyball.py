import json
import random
from subprocess import call

def bruteforce(iter, data):
    members = []
    final_diff = 999999
    i = 0
    teams1 = []
    teams2 = []

    for member in data:
        if '#' not in str(member):
            members.append(member)

    while i < iter:
        second_team = []
        #print('Iteration', i, end = '\t')
        
        #get first team randomly
        first_team = []
        first_team = random.sample(members, k = int(len(members) / 2))
        #print(first_team)
        
        for member in members:
            if member not in first_team:
                second_team.append(member)

        #print(second_team)
        #calculate score for first team
        diff1 = 0
        for member in first_team:
            diff1 += data[member]
        #print('level of first team', diff1)

        #calculate score for second team
        diff2 = 0
        for member in second_team:
            diff2 += data[member]
        #print('level of second team', diff2)

        #print(diff1, 'vs', diff2)
        #difference
        diff = abs(diff1 - diff2)
        #print('diff', diff)

        #if diff is lower, keep new
        #print('diff=', diff, 'final_diff =', final_diff)
        if diff <= final_diff:
            
            final_first_team = first_team
            final_second_team = second_team
            final_diff = diff
            if final_diff == 0:
                add_to_possible_team_list = True
                final_diff = 999999999
            else:
                add_to_possible_team_list = False

            teams1, teams2 = confirm_teams(teams1, teams2, final_first_team, final_second_team, final_diff, iters_done = add_to_possible_team_list)
        # else:
        #     print('last team was better built')

        #lose one iteration
        i += 1

    return final_first_team, final_second_team, final_diff, teams1, teams2

def setup(filename):

    with open(filename) as json_file:
        data = json.load(json_file)
    
    input_yes = False
    if input_yes:
        iterations = int(input("Iterations? \t"))
    else:
        iterations = 1000

    return data, iterations

def confirm_teams(possible_team1, possible_team2, team1, team2, diff = None, iters_done = False):

    if iters_done:
        possible_team1.append(team1)
        possible_team2.append(team2)
    
    print('team1:')
    for gamer in sorted(team1):
        print(gamer, end = ' ')
    print('\n-----------------------')
    print('team2:')
    for gamer in sorted(team2):
        print(gamer, end = ' ')
    if diff is not None:
        print('\n-----------------------')
        print('skill diff:', diff)
    print('-----------------------\n\n')

    return possible_team1, possible_team2

def remove_copy_teams(teams1, teams2):
    teams1_no_dup = []
    teams2_no_dup = []

    for team in teams1:
        if team not in teams1_no_dup:
            teams1_no_dup.append(sorted(team))

    for team in teams2:
        if team not in teams2_no_dup:
            teams2_no_dup.append(sorted(team)) 

    print('POSSIBLE VARIATIONS:')
    for i in range(len(teams1_no_dup) - 1):
        print('-----------------------')
        print('team1:')
        print(teams1_no_dup[i], end = '\t')
        print('')

        print('team2:')
        print(teams2_no_dup[i], end = '\t')
        print('')
        print('------------------------')
        


def main():
    
    data, iterations = setup('data.json')
    final_first_team, final_second_team, final_diff, teams1, teams2 = bruteforce(iter = iterations, data = data)
    print('FINAL SCORES:')
    teams1, teams2 = confirm_teams(teams1, teams2, final_first_team, final_second_team, final_diff, True)
    remove_copy_teams(teams1, teams2)
    

main()
    