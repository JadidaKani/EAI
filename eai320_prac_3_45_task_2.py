# Group no: 45
# Name: Jadida Kalim
# Student no: 21436054
# Name: Thabiso Nkosi
# Student no: 22507745

import csv
import math
import random
import numpy as np

D = 12
H = 9
C = 3
N = 1000000

# function to containing the formula for the activation function for forward propagation
def activationFunction(x):
    y = math.tanh(x)
    return y

"""weight1 contains the weights from the input layer to the hidden layer and weight2 contains the weights from the 
   hidden layer to the output layer. The values stored in these 2 lists were determined by training the ANN using 
   back propagation with a learning rate of 0.01 and 9 neurons in the hidden layer"""

weight1 = [[0.01854004418483155, 2.245161935837877, 0.9252531680273682, 2.26783014349019, 3.7773179287528147, -4.023375873494238, 3.5860892103659667, -5.026899708861212, 3.459622416237192, 3.2658366320825793, 1.936451157944634, -2.7360988037171325, 0.9799766766975652],
           [3.1566903005818063, -1.2216439350339234, -0.8489683866495119, 1.593539228940044, -0.8316447179301418, 0.7305972634764104, -1.3452560813834593, 1.393213427484938, 0.7136234745964736, 1.637535159579318, -3.474948807553473, 2.999234479407354, 0.2363184358440842],
           [0.15401190736397113, -0.29998760621325515, 1.1021057023654484, -0.7541216368604823, 0.5997178657161623, 1.9262195291512687, -0.3664066797576509, 0.021874277715495473, 1.097858801394528, -0.419779297677406, 0.035679418989754866, 0.9207280647544273, 0.12118680633391875],
           [0.2518218455500414, 0.26526147401242084, 0.43786838336802963, 0.6106590827005647, 0.4418884237728734, 0.3576755336207463, 0.3322127916263199, 0.944297655427797, -0.2126080443819603, 0.2918335558785222, 0.14964422890215184, -0.2191825002278453, -0.04039020045432936],
           [0.031248580172814826, -0.3556776503981877, 0.7543319676634085, -0.22366289805802883, 0.30645466892035417, 1.1097688982967484, 0.5242831650948643, 0.6866178871589871, 0.03330847769979997, 0.012036793274465472, -0.09878599349367306, 0.5467909682331791, -0.3876308449438683],
           [0.18313599150289625, 0.8318813594846937, 1.0575765237894286, -3.4951334795215643, 3.3706034887043663, 2.469120286596469, 2.9802783702892888, 3.3234317156387316, -3.9601542160622154, -1.725056191767913, 0.3853392630005473, 3.0259108709111766, 0.9806788972714413],
           [0.2878679042541566, 0.8713860285647924, -0.29826801924211227, -0.1642575915876613, -1.0149248558975306, 1.5964951993159169, 0.0477702352959444, 0.9027893398467581, -0.039454028664563746, -1.2728355179025719, 0.694117980784155, 0.8416407692852933, 0.2067265737720279],
           [0.09550564868065947, 0.10085930846246434, 1.9560418785272002, 0.010953537647881135, -0.5686358185094847, 2.4145970534259886, 5.425543852074563, -0.5897460017487732, -2.252953046004234, -0.020860488286212987, 0.473774380497154, 2.5468775299012343, 1.166628955756823],
           [-0.030247050475054903, 0.6761844923214773, 0.8207362997025109, -0.7842358880861473, 0.7142296802115383, 0.858065151501851, 0.4878312375408887, 1.627141502880031, -1.0333581968888303, 0.42889104855787397, 1.755487760884665, -0.9268866660350763, -0.08945837493860304]]

weight2 = [[0.0781067834146507, 0.09192750276546396, 0.9867228443554478, 0.6490011473108515, -1.10121060485929, -1.9189546849777894, 0.050037513378624957, 0.7015238913125104, -0.23565119137666055, 0.8881994037041069],
           [0.30983208750102803, -1.6121899850210395, -0.17874843978718158, 1.3980932266802168, 0.6893042292216838, 0.08298040255673565, 0.4343596588660604, -0.16385883589842745, -0.6101929078479105, 0.417291496257283],
           [-1.3757383588680892, 0.16915662720207816, 0.22605023105575406, 0.5224461578103976, -0.35149661607926636, 0.18747631192880476, -0.1207515135014702, 0.11091536789649988, 0.051206192505991, 0.8036749958610284]]

# the dataset(data1.csv) is read in and stored in the list below(data)
data = []
with open('data1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

"""This function uses 1-of-K encoding to encode the values stored in data1.csv and store them in a list called inputs.
   This is used to initialize the input layer of the ANN"""
def setInput():
    inputs = [[0 for i in range(D + 1)] for i in range(N)]
    counter = 0
    while counter < N:
        if data[counter][0][0] == 'R':
            inputs[counter][0] = 1
        elif data[counter][0][0] == 'P':
            inputs[counter][1] = 1
        elif data[counter][0][0] == 'S':
            inputs[counter][2] = 1

        if data[counter][0][1] == 'R':
            inputs[counter][3] = 1
        elif data[counter][0][1] == 'P':
            inputs[counter][4] = 1
        elif data[counter][0][1] == 'S':
            inputs[counter][5] = 1

        if data[counter][0][2] == 'R':
            inputs[counter][6] = 1
        elif data[counter][0][2] == 'P':
            inputs[counter][7] = 1
        elif data[counter][0][2] == 'S':
            inputs[counter][8] = 1

        if data[counter][0][3] == 'R':
            inputs[counter][9] = 1
        elif data[counter][0][3] == 'P':
            inputs[counter][10] = 1
        elif data[counter][0][3] == 'S':
            inputs[counter][11] = 1

        inputs[counter][12] = 1  # Bias value of input layer
        counter += 1

    return inputs

"""This function is used to propagate through the ANN and generate values for the output layer by using weight1 and
   weight2 and the values of the input layer """
def forwardPropagation(input,w1,w2):
    output = [[0 for i in range(C)] for i in range(N)] # initializes the output list that is returned by the function
    count = 0
    while count < len(input):
        inputValues = input[count]
        hiddenLayer = np.zeros(H + 1)
        hiddenLayer[H] = 1  # Bias value of hidden layer

        # generates values for the hidden layer using w1(weight1)
        hiddenNode = 0
        while hiddenNode < H:
            inpNode = 0
            while inpNode < len(inputValues):
                hiddenLayer[hiddenNode] += inputValues[inpNode] * w1[hiddenNode][inpNode]
                inpNode += 1
            hiddenLayer[hiddenNode] = activationFunction(hiddenLayer[hiddenNode])
            hiddenNode += 1

        # generates values for the output layer using w2(weight2)
        outputLayer = np.zeros(C)
        outputNode = 0
        while outputNode < C:
            hiddenNode = 0
            while hiddenNode < len(hiddenLayer):
                outputLayer[outputNode] += hiddenLayer[hiddenNode] * w2[outputNode][hiddenNode]
                hiddenNode += 1
            outputLayer[outputNode] = activationFunction(outputLayer[outputNode])
            outputNode += 1

        outputNode = 0
        while outputNode < C:
            output[count][outputNode] += outputLayer[outputNode]
            outputNode += 1

        count += 1

    return output # returns values of the neurons in the output layer

# The code below is used to run this agent with other agents
if input == '':
    matches = 0  # used to count the number of moves in the game
    object = ""
    history = "XXXX" # stores the values played by each of the 2 agents in the same way in which they are stored in data1.csv
    inputsArray = setInput()  # list used to store the values of the input layer
    outputArray = forwardPropagation(inputsArray, weight1, weight2) # list used to store the values of the output layer
    object = random.choice(['R','P','S'])
    history = history[1:]
    history += object
else:
    matches += 1 # this is to makes sure that the first input value generated by the opponent is not appended to history string
    if matches != 1:
        history = history[1:]
        history += input

        index = -1
        for i, sublist in enumerate(data): # checks to see if the value stored in history can be found in the list, data
            if sublist[0] == history:
                index = i # if it is found the index value is stored
                break

        if index != -1:
            history = history[1:]
            history += object
            list = outputArray[index]
            highestInd = list.index(max(list)) # the highest value in this list is found and is used to determine what move should be played

            if highestInd == 0:
                object = "P"
            elif highestInd == 1:
                object = "S"
            elif highestInd == 2:
                object = "R"

        # if the value stored in history is not found then the object played remians the same and is appended to history
        else:
            object = object
            history = history[1:]
            history += object

    else:
        object = random.choice(['R', 'P', 'S'])

output = object