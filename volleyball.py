import json
import random


def main():
    
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    input_yes = False
    if input_yes:
        iterations = input("Iterations:/t")
    else:
        iterations = 10000
    i = 0

    final_diff = 999999
    members = []

    while i < iterations:
        second_team = []
        #print('Iteration', iterations, end = '\t')
        
        for member in data:
            members.append(member)

        #get first team randomly
        first_team = random.sample(members, k = int(len(members) / 2))
        
        for member in members:
            if member not in first_team:
                second_team.append(member)

        #calculate score for first team
        diff1 = 0
        for member in first_team:
            diff1 += data[member]

        #calculate score for second team
        diff2 = 0
        for member in second_team:
            diff2 += data[member]

        #difference
        diff = abs(diff1 - diff2)

        #if diff is lower, keep new
        if diff <= final_diff:
            #print('new team found!, skill difference:', diff, 'teams below:')
            final_first_team = first_team
            final_second_team = second_team
            final_diff = diff
        #else:
            #print('last team was better built')

        #lose one iteration
        i += 1

    print('\n-----------------------')
    print('Iteration', iterations)
    print('-----------------------')
    print('team1:')
    for gamer in final_first_team:
        print(gamer['name'], end = ' ')
    print('\n-----------------------')
    print('team2:')
    for gamer in final_second_team:
        print(gamer['name'], end = ' ')
    print('\n-----------------------')
    print('skill diff:', final_diff)
    print('-----------------------\n\n')

    
main()
    