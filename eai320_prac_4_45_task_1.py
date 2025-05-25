# Group no: 45
# Name: Jadida Kalim
# Student no: 21436054
# Name: Thabiso Nkosi
# Student no: 22507745

import random

"""The hard coded values below are all the probabilities obtained when training the agent on data1.csv. The probabilities
   below were calculated by adding 1 count to every sample."""

# The probabilities of yt (the last column in data1.csv) being R,P or S
probYtR = 0.3413279280486476
probYtP = 0.33440299037308663
probYtS = 0.3242690815782658

# The list below contains the probabilities that xt-2, yt-2, xt-1, yt-1, are either R,P or S given that the value
# of yt is either R,P or S. The 4 values in each of the inner arrays are the probabilities of xt-2, yt-2, xt-1, yt-1
# given a certain value (R,P or S) of yt
probabilities = [[0.3312913271868069, 0.8639355933097199, 0.26596177903559887, 0.8656582613357708],     #R|R
                 [0.33114777151796937, 0.06785495603973855, 0.26656822849374945, 0.06764987651282772],  #P|R
                 [0.3375609012952237, 0.06820945065054156, 0.46746999247065163, 0.06669186215140142],   #S|R
                 [0.33686297494662176, 0.06974157162251873, 0.4703922776505206, 0.0688743623021118],    #R|P
                 [0.3313756332123227, 0.8614797581383109, 0.26424466068192554, 0.8621824967255373],     #P|P
                 [0.33176139184105546, 0.06877867023917035, 0.2653630616675538, 0.06894314097235098],   #S|P
                 [0.33166292495189226, 0.07156646272265259, 0.2628904129866285, 0.07050254107662703],   #R|S
                 [0.3364922040755909, 0.071116223417378, 0.4734636354665219, 0.07079242117728327],      #P|S
                 [0.3318448709725169, 0.8573173138599695, 0.26364595154684956, 0.8587050377460897]]     #S|S

# The code below is used to run this agent with other agents
if input == '':
    history = "XXXX" # this string stores the histories of moves played by each agent over the 2 previous rounds
    object = random.choice(['R', 'P', 'S'])

else:
    # in the code below the object played by this agent is stored first in the history string. This is because this is
    # how the histories are stored in the csv file on which the agent is trained on
    history = history[1:]
    history += object
    history = history[1:]
    history += input

    # if the character X is in the history string the object plays randomly because in order for the agent to play properly
    # based on how it was trained with the Naive Bayes Classifier all 4 fields of the string need to be either R,P or S
    if 'X' in history:
        object = random.choice(['R', 'P', 'S'])
    else:
        """the code in this else statement helps in finding which probability values from the probabilities array should 
           be used for the calculations below. From the probabilities array above it can be seen that yt is R in the 
           1st 3 rows, P in the middle 3 and S in the last 3 rows. When yt is R, the 1st row is the probability that the 
           game histories are R|R, the 2nd row is the probability that the game histories are P|R, the 3rd row is the 
           probability that the game histories are S|R. This is the same for when yt is P and S as well. Based on these
           findings various offsets are set depending on each of the characters in the history string. This is done below."""

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

        # this list stores the probabilites p1,p2 and p3 calculated below. p1 is the probability that the opponent will
        # play R, p2 is the probability that the opponent will play P and p3 is the probability that the opponent
        # will play S
        calculatedProb = []

        row = 0  # the row at which yt = R starts from
        p1 = probYtR * probabilities[row + x2][0] * probabilities[row + y2][1] * probabilities[row + x1][2] * \
             probabilities[row + y1][3]

        row = 3  # the row at which yt = P starts from
        p2 = probYtP * probabilities[row + x2][0] * probabilities[row + y2][1] * probabilities[row + x1][2] * \
             probabilities[row + y1][3]

        row = 6  # the row at which yt = S starts from
        p3 = probYtS * probabilities[row + x2][0] * probabilities[row + y2][1] * probabilities[row + x1][2] * \
             probabilities[row + y1][3]

        calculatedProb.append(p1)
        calculatedProb.append(p2)
        calculatedProb.append(p3)

        # the index with the highest value in the list is then found and based on the value of this index the agent determines
        # what object it should play next
        maxVal = max(calculatedProb)
        maxInd = calculatedProb.index(maxVal)

        if maxInd == 0: # this means that the opponent will play R
            object = 'P'
        elif maxInd == 1: # this means that the opponent will play P
            object = 'S'
        elif maxInd == 2: # this means that the opponent will play S
            object = 'R'

output = object
