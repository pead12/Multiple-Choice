from Questions import Question

print("\nWelcome to the quiz about astrophysics, there are 9 questions.\n")

question_prompts = [
    "How many planets are in our solar system?\n (a) 6\n (b) 7\n (c) 8\n (d) 9\n\n",
    "In what time does the moon rotate once?\n(a) 1 day\n(b) it does not rotate\n(c) 16 days\n(d) 27 days\n\n",
    "How far away is the sun?\n(a) 568.000km\n(b) 1.4 million km\n(c) 8 million km\n(d) 150 million km\n\n",
    "How old is the universe?\n (a) 5.9 billion years\n (b) 13.8 billion years\n (c) 8.7 billion years\n (d) 17.2 billion years\n\n",
    "How many stars are in the milky way?\n (a) 200 billion\n (b) 400 billion\n (c) 1 trillion\n (d) 3.5 trillion\n\n",
    "What will happen with the universe in the future?\n (a) it will increase\n (b) it will decrease\n (c) it is going to stay the same\n (d) it will first increase and at a certain point, it will decrease.\n\n",
    "How does a star with 8 times the mass of the sun end?\n (a) as a black dwarf\n (b) as a neutron star\n (c) as a black hole\n (d) as a pulsar\n\n",
    "What colour does the moon get during a total eclipse?\n (a) orange\n (b) blue\n (c) red\n (d) yellow\n\n",
    "Why is pluto not a planet anymore?\n (a) his size is too small\n (b) he doesn´t have a moon\n (c) he is not a globe\n (d) he doesn´t have enough mass \n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "d"),
]
score = 0

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + " out of " + str(len(questions)) + " correct! You loser!")


test(questions)


