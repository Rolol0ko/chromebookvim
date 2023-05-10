import numpy as np
import time

gender = ['Heeeey', 'Hi', 'Hello', "Sup'", 'Greetings', 'Howdy', "What's buzzin cuzzin?",]
verbs = ['run you over', 'throw you off a bridge', 'shoot you', 'eat a table', 'paint a porch', 'run a marathon', 'blow you up', 'kick you', 'charge a laptop', 'iron a t-shirt', 'smash your mother', 'commit homocide', 'cut your hair off', 'cut my hair off', 'take you to the cemetary', 'start a cult', 'consume your flesh',]
nouns = ['water bottle', 'desk', 'chair', 'laptop', 'vent', 'house', 'ball', 'ronan', 'recyling bin', 'ice chai tea latte', 'backpack', 'goverment building', 'smartphone', 'mother', 'shingle', 'orange', 'banana', 'apple', 'strawberry', 'pinapple',]

while True:
    verb = np.random.choice(verbs)
    noun = np.random.choice(nouns)
    #gender = np.random.choice(gender)

    print("Heeeey, are you a " + noun + "? Because I want to " + verb + ".")

    time.sleep(3)
