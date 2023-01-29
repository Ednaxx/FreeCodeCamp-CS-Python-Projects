import random
import copy

class Hat:

    def __init__(self, **balls):
        self.balls = balls
        if len(balls) == 0:
            return "Empty"

        self.contents = []
        for item, amount in balls.items():
            for i in range(amount):
                self.contents.append(item)

        self.backup = self.contents.copy()


    def draw(self, amount):
        self.contents = self.backup.copy()

        if amount >= len(self.contents):
            return self.contents
        
        
        output = []

        for i in range(amount):
            randomBall = random.randrange(0, len(self.contents))
            output.append(self.contents[randomBall])
            self.contents.pop(randomBall)
        
        
        return output



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    successes = 0
    
    for i in range(num_experiments):

        #put balls drawn on a dictionary

        exp = hat.draw(num_balls_drawn).copy()
        expBalls = {}

        for j in range(len(exp)):
            try:
                expBalls[exp[j]] += 1
            except KeyError:
                expBalls[exp[j]] = 1
        
        #verify if balls drawn contains expected balls, add 1 to success counter if so

        check = 0

        for k in expected_balls:
            try:
                if expected_balls[k] <= expBalls[k]:
                    check += 1
                    continue
                else:
                    break
            except KeyError:
                break
        
        if check == len(expected_balls):
            successes += 1
    
    #calculate probability

    probability = successes / num_experiments
    
    
    return probability