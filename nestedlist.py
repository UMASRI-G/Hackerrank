if __name__ == '__main__':
    nested_list = [] 
for _ in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])
score_list = [] 
for sublist in nested_list:
    score_list.append(sublist[1])
sortedScore = sorted(set(score_list)) 
lowest = []
secondLowest = []
for score in sortedScore: 
    if len(lowest) == 0:
        lowest.append(score) 
    elif score > lowest[0]:
            secondLowest.append(score)
            break
answer = []
for sublist in nested_list:
    if sublist[1] == secondLowest[0]:
        answer.append(sublist[0])
for x in sorted(answer):       
    print(x)
