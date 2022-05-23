import anime_functions


while True:
    try:
        answer = anime_functions.answer('anime.txt')
        count = 1
        count_limit = 2
        
        titles = anime_functions.anime_picker('anime.txt')

        hints_one = anime_functions.hint_giver('anime.txt', count, count_limit)
        guess = str(input(f'Guess the anime, hint is {hints_one}: '))

        if guess == answer:
            print('Correct')
            print(f'Attemps were {count}.')
            break

        elif guess != answer:
            count += 1
            hints_two = anime_functions.hint_giver('anime.txt', count, count_limit)
            print(f'Try again here is a hint: {hints_two}')
            
            guess2 = str(input('Guess again: '))
            if guess2 == answer:
                print('Nice job on attempt 2')
                print(f'Attemps were {count}.')
                break
            elif guess2 != answer:
                count +=1
                if count >= 3:
                    print(f'Sorry the answer was {answer}')
                    exit()
    
    except ValueError as ve:
        print('Please put a correct input, Error' + str(ve))
    
    except Exception as e:
        print('The following error has occured: ' + str(e))
            



 # variable will increment every loop iteration
   # your code



