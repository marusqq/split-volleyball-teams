import json
import random


def main():
    
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    
    scrim = True
    if scrim:
        iterations = 40
    else:
        iterations = 10000
    i = 0
    copy_data = data
    final_diff = 999999

    while i < iterations:
        second_team = []
        #print('Iteration', iterations, end = '\t')
        
        #get first team randomly
        first_team = random.sample(copy_data, k = int(len(data) / 2))
        
        for member in copy_data:
            if member not in first_team:
                second_team.append(member)

        #calculate score for first team
        diff1 = 0
        for member in first_team:
            diff1 += member['score']

        #calculate score for second team
        diff2 = 0
        for member in second_team:
            diff2 += member['score']

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

        #copy data    
        copy_data = data

        #lose one iteration
        i += 1

        if not iterations % 1000 or scrim:
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
    