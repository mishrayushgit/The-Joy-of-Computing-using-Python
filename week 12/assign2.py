def state_of_people(people):
    happy_state = people
    sad_state = 0
    for _ in range(3):
        new_happy_state = happy_state* 0.3 + sad_state*0.5
        new_sad_state = happy_state* 0.7 + sad_state*0.5
        happy_state = int(new_happy_state)
        sad_state = int(new_sad_state)
    print(happy_state," ",sad_state)
input_people = int(input())
state_of_people(input_people)