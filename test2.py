import random
import itertools

actions = ["touch other player's butt", "lift left leg", "lift right arm", "lift right leg", "lift left leg", "touch other player's sweet spot", "touch other player's breast", "put your face between the other player's legs"]

for element in itertools.cycle(actions):
    intimate_actions = actions[random.randint(0,7)]
    print(intimate_actions)
