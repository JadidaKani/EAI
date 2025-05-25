# Group no: 45
# Name: Jadida Kalim
# Student no: 21436054
# Name: Thabiso Nkosi
# Student no: 22507745

import random

# The code below is used to run this agent with other agents
if input == '':
    # this list stores the number of R's,P's or S's played by each agent over two rounds based on the input value(R,P or S)
    tallys = [[1] * 4 for i in range(9)]

    # this list keeps track of the total number of R,P or S played by the opposing agent (as in the number of inputs that
    # are R,P or S) in a match. The 1st index stores the number of Rs, the 2nd index stores the number of Ps and the last
    # index stores the number of Ss
    numRPS = [3, 3, 3]
    history = "XXXX"  # this string stores the histories of moves played by each agent over the 2 previous rounds

    object = random.choice(['R', 'P', 'S'])

else:
    if all(char != 'X' for char in history):

        """The if else statements below check what the value of input is and based on that the variable 'row' , which
                  is basically the row offset, is set."""

        """if it is R, row=0 because from task1 it can be seen that yt, which is basically the variable 'input', is R
           from rows 0-2 in the probabilities array in task1. If input is P row=3 as yt is P from rows 3-5 in the 
           probabilities array in task1. If input is S row=6 as yt is P from rows 6-8 in the probabilities array in task1."""

        if input == 'R':
            row = 0
        elif input == 'P':
            row = 3
        elif input == 'S':
            row = 6

        # this code updates the values of the numRPS list based on the input values and the value of 'row'
        index = int(row / 3)
        numRPS[index] += 1

        # Here the history string is used to count the occurrences of sequences depending on the moves played
        # and the tallys array is updated accordingly
        if history[0] == 'R':
            tallys[row + 0][0] += 1
        elif history[0] == 'P':
            tallys[row + 1][0] += 1
        elif history[0] == 'S':
            tallys[row + 2][0] += 1

        if history[1] == 'R':
            tallys[row + 0][1] += 1
        elif history[1] == 'P':
            tallys[row + 1][1] += 1
        elif history[1] == 'S':
            tallys[row + 2][1] += 1

        if history[2] == 'R':
            tallys[row + 0][2] += 1
        elif history[2] == 'P':
            tallys[row + 1][2] += 1
        elif history[2] == 'S':
            tallys[row + 2][2] += 1

        if history[3] == 'R':
            tallys[row + 0][3] += 1
        elif history[3] == 'P':
            tallys[row + 1][3] += 1
        elif history[3] == 'S':
            tallys[row + 2][3] += 1

    # in the code below the object played by this agent is stored first in the history string.
    history = history[1:]
    history += object
    history = history[1:]
    history += input

    if 'X' in history:
        object = random.choice(['R', 'P', 'S'])
    else:
        # the code below has the same functionality as the code in task1. It is used to find which probability values
        # from the tallys array should be used for the calculations below
        if history[0] == 'R':
            x2 = 0
        elif history[0] == 'P':
            x2 = 1
        elif history[0] == 'S':
            x2 = 2

        if history[1] == 'R':
            y2 = 0
        elif history[1] == 'P':
            y2 = 1
        elif history[1] == 'S':
            y2 = 2

        if history[2] == 'R':
            x1 = 0
        elif history[2] == 'P':
            x1 = 1
        elif history[2] == 'S':
            x1 = 2

        if history[3] == 'R':
            y1 = 0
        elif history[3] == 'P':
            y1 = 1
        elif history[3] == 'S':
            y1 = 2

        total = numRPS[0] + numRPS[1] + numRPS[2]  # stores the total number of R,P and S played by opposing agent

        # this list stores the probabilites p1,p2 and p3 calculated below. p1 is the probability that the opponent will
        # play R, p2 is the probability that the opponent will play P and p3 is the probability that the opponent
        # will play S
        calculatedProb = []

        row = 0  # the row at which input = R starts from
        index = int(row / 3) # used to find the and use the value in a particular index of the numRPS list
        p1 = (numRPS[index] / total) * (tallys[row + x2][0] / numRPS[index]) * (tallys[row + y2][1] / numRPS[index]) * \
             (tallys[row + x1][2] / numRPS[index]) * (tallys[row + y1][3] / numRPS[index])

        row = 3  # the row at which input = P starts from
        index = int(row / 3)
        p2 = (numRPS[index] / total) * (tallys[row + x2][0] / numRPS[index]) * (tallys[row + y2][1] / numRPS[index]) * \
             (tallys[row + x1][2] / numRPS[index]) * (tallys[row + y1][3] / numRPS[index])

        row = 6  # the row at which input = S starts from
        index = int(row / 3)
        p3 = (numRPS[index] / total) * (tallys[row + x2][0] / numRPS[index]) * (tallys[row + y2][1] / numRPS[index]) * \
             (tallys[row + x1][2] / numRPS[index]) * (tallys[row + y1][3] / numRPS[index])

        calculatedProb.append(p1)
        calculatedProb.append(p2)
        calculatedProb.append(p3)

        # the index with the highest value in the list is then found and based on the value of this index the agent determines
        # what object it should play next
        maxVal = max(calculatedProb)
        maxInd = calculatedProb.index(maxVal)

        if maxInd == 0:  # this means that the opponent will play R
            object = 'P'
        elif maxInd == 1:  # this means that the opponent will play P
            object = 'S'
        elif maxInd == 2:  # this means that the opponent will play S
            object = 'R'

output = object

"""
RESULTS & DISCUSSION:

Both agents in Task 1 and Task 2 were run against only_rock.py, only_paper.py, only_scissors.py and beat_common.py.

Initially both tasks played 10 matches against each of the 4 bots. The average number of matches won by each agent
for a certain number of rounds are shown below:

Task1:                                      
No. Rounds:  % Matches won: % Rounds won:
    10          100             82                                 
    100         97.5            91.5
    1000        100             94.9

Task2:                                      
No. Rounds:  % Matches won: % Rounds won:
    10          97.5           76.3                                 
    100         100            93.1
    1000        100            94.8

Both tasks also played 100 matches against each of the 4 bots. The average number of matches won by each agent
for a certain number of rounds are shown below:

Task1:                                      
No. Rounds:  % Matches won: % Rounds won:
    10          98.8            81.8                                 
    100         96.3            90.8
    1000        97.3            93.5

Task2:                                      
No. Rounds:  % Matches won: % Rounds won:
    10          98             73                                 
    100         100            93.2
    1000        100            94.8
    
From the data above it can be seen that when the number of matches increase from 10 to 100 the number of matches won for
10, 100 and 1000 rounds decreases for Task 1 and increases or remains the same for Task2. This is due to the fact that
the probabilities used for calculating and determining which object to play next, is hard coded in Task 1 while Task 2 
implements online learning. Hard coded probabilities are fixed and so Task 1 cannot adapt to new data. Task 2 on the other 
hand has the ability to update and change its data without needing to be retrained from scratch again.

In terms of Task 2, when there are 10 matches being played the number of matches won increases from 97.5% to 100% from 10
to 1000 rounds. When there are 100 matches being played the number of matches won increases from 98% to 100% from 10
to 1000 rounds. Therefore an increase in the number of matches and rounds leads to a higher chance of this agent winning.
This is probably because, since the agent is learning online, with a lower number of rounds and matches it has very little
data or histories of the game to work with and therefore it does not perform as well as it would when there is a higher 
number of matches and rounds, because in this case the agent has more data to work with and train itself on.

Overall the win rates for each agent for the various number of matches and rounds are between 96% and 100%, indicating that 
the naive Bayes Classifier was trained and implemented successfully.

"""