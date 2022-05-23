import random
from datetime import date


def file_reader(file):
    new_list = []
    with open(file,'r') as text:
        reader = text.readlines()
        for line in reader:
            new_list.append(line.rstrip())
    return new_list


def answer(file):
    new_list = file_reader(file)
    random.seed(date.today())
    correct = random.choice(new_list)
    return correct
    


def anime_picker(file):
    
    new_list = file_reader(file)
    correct = answer(file)
    while True:
        
        ani = random.sample(new_list,5)
        if ani.count(correct) > 0:
            break
            
        else:
           ani = random.sample(new_list,5)

    for count, anime in enumerate(ani, start=1):
        print(f'{count}. {anime}\n')



def hint_giver(file,count,count_limit):
    b = list(answer(file))

    if count < count_limit:
        return(b[0])
    elif count == count_limit:
        return(b[-1])


    


if __name__ == '__main__':
    #hi('anime.txt')
    answer('anime.txt')
    anime_picker('anime.txt')
    #answer('anime.txt')
    #hint_text('anime.txt')
    #hint_giver('anime.txt', 2,3)