# Group no: 45
# Name: Jadida Kalim
# Student no: 21436054
# Name: Thabiso Nkosi
# Student no: 22507745

import numpy as np
import math
import random

D = 12  # number of neurons in input layer
H = 9   # number of neurons in hidden layer
C = 3   # number of neurons in output layer
learningRate = 0.01  # learning rate
epoch = 5 # maximum number of epochs
errorConvergence = 0.01 # error convergence value

# weights from input layer to hidden layer
weight1 = [[0.01854004418483155, 2.245161935837877, 0.9252531680273682, 2.26783014349019, 3.7773179287528147, -4.023375873494238, 3.5860892103659667, -5.026899708861212, 3.459622416237192, 3.2658366320825793, 1.936451157944634, -2.7360988037171325, 0.9799766766975652],
           [3.1566903005818063, -1.2216439350339234, -0.8489683866495119, 1.593539228940044, -0.8316447179301418, 0.7305972634764104, -1.3452560813834593, 1.393213427484938, 0.7136234745964736, 1.637535159579318, -3.474948807553473, 2.999234479407354, 0.2363184358440842],
           [0.15401190736397113, -0.29998760621325515, 1.1021057023654484, -0.7541216368604823, 0.5997178657161623, 1.9262195291512687, -0.3664066797576509, 0.021874277715495473, 1.097858801394528, -0.419779297677406, 0.035679418989754866, 0.9207280647544273, 0.12118680633391875],
           [0.2518218455500414, 0.26526147401242084, 0.43786838336802963, 0.6106590827005647, 0.4418884237728734, 0.3576755336207463, 0.3322127916263199, 0.944297655427797, -0.2126080443819603, 0.2918335558785222, 0.14964422890215184, -0.2191825002278453, -0.04039020045432936],
           [0.031248580172814826, -0.3556776503981877, 0.7543319676634085, -0.22366289805802883, 0.30645466892035417, 1.1097688982967484, 0.5242831650948643, 0.6866178871589871, 0.03330847769979997, 0.012036793274465472, -0.09878599349367306, 0.5467909682331791, -0.3876308449438683],
           [0.18313599150289625, 0.8318813594846937, 1.0575765237894286, -3.4951334795215643, 3.3706034887043663, 2.469120286596469, 2.9802783702892888, 3.3234317156387316, -3.9601542160622154, -1.725056191767913, 0.3853392630005473, 3.0259108709111766, 0.9806788972714413],
           [0.2878679042541566, 0.8713860285647924, -0.29826801924211227, -0.1642575915876613, -1.0149248558975306, 1.5964951993159169, 0.0477702352959444, 0.9027893398467581, -0.039454028664563746, -1.2728355179025719, 0.694117980784155, 0.8416407692852933, 0.2067265737720279],
           [0.09550564868065947, 0.10085930846246434, 1.9560418785272002, 0.010953537647881135, -0.5686358185094847, 2.4145970534259886, 5.425543852074563, -0.5897460017487732, -2.252953046004234, -0.020860488286212987, 0.473774380497154, 2.5468775299012343, 1.166628955756823],
           [-0.030247050475054903, 0.6761844923214773, 0.8207362997025109, -0.7842358880861473, 0.7142296802115383, 0.858065151501851, 0.4878312375408887, 1.627141502880031, -1.0333581968888303, 0.42889104855787397, 1.755487760884665, -0.9268866660350763, -0.08945837493860304]]

# weights from hideen layer to output layer
weight2 = [[0.0781067834146507, 0.09192750276546396, 0.9867228443554478, 0.6490011473108515, -1.10121060485929, -1.9189546849777894, 0.050037513378624957, 0.7015238913125104, -0.23565119137666055, 0.8881994037041069],
           [0.30983208750102803, -1.6121899850210395, -0.17874843978718158, 1.3980932266802168, 0.6893042292216838, 0.08298040255673565, 0.4343596588660604, -0.16385883589842745, -0.6101929078479105, 0.417291496257283],
           [-1.3757383588680892, 0.16915662720207816, 0.22605023105575406, 0.5224461578103976, -0.35149661607926636, 0.18747631192880476, -0.1207515135014702, 0.11091536789649988, 0.051206192505991, 0.8036749958610284]]

# function to containing the formula for the activation function
def activationFunction(x):
    y = math.tanh(x)
    return y

# function with the derivative of the activation function
def derivative(x):
    y = 1 - math.tanh(x) ** 2
    return y

# This function implements both the forward propagation and back propagation algorithms and is used to train the ANN.
# It returns the updated weights and L2 loss value
def backPropagation(input,output,w1,w2,rate,maxEpoch,errConv,moves):
    iterations = 0
    lossValues = np.zeros(maxEpoch) # array that stores L2 loss values
    errConvChecks = 1 # variable used to check if error convergence is reached

    while iterations < maxEpoch and errConvChecks > errConv:

        dataCounter = 0
        while dataCounter <= moves:
            inputVal = input[dataCounter]
            hiddenLayer = np.zeros(H + 1)
            hiddenLayer[H] = 1  # Bias value

            # Forward propagation implementation
            hiddenNodeCounter = 0
            while hiddenNodeCounter < H:
                inpNode = 0
                while inpNode < len(inputVal):
                    hiddenLayer[hiddenNodeCounter] += inputVal[inpNode] * w1[hiddenNodeCounter][inpNode]
                    inpNode += 1
                hiddenLayer[hiddenNodeCounter] = activationFunction(hiddenLayer[hiddenNodeCounter])
                hiddenNodeCounter += 1

            outputLayer = np.zeros(C)
            outputNodeCounter = 0
            while outputNodeCounter < C:
                hiddenNode = 0
                while hiddenNode < len(hiddenLayer):
                    outputLayer[outputNodeCounter] += hiddenLayer[hiddenNode] * w2[outputNodeCounter][hiddenNode]
                    hiddenNode += 1
                outputLayer[outputNodeCounter] = activationFunction(outputLayer[outputNodeCounter])
                outputNodeCounter += 1

            #Back propagation implementation
            outputGradient = np.zeros(C)
            outputNodeCounter = 0
            while outputNodeCounter < C:
                outputGradient[outputNodeCounter] = (output[dataCounter][outputNodeCounter] - outputLayer[outputNodeCounter]) * derivative(outputLayer[outputNodeCounter])
                outputNodeCounter += 1

            hiddenGradient = np.zeros(H)
            hiddenNodeCounter = 0
            while hiddenNodeCounter < H:
                hiddenError = 0
                outputNodeCounter = 0
                while outputNodeCounter < C:
                    hiddenError += outputGradient[outputNodeCounter] * w2[outputNodeCounter][hiddenNodeCounter]
                    outputNodeCounter += 1
                hiddenGradient[hiddenNodeCounter] = hiddenError * derivative(hiddenLayer[hiddenNodeCounter])
                hiddenNodeCounter += 1

            #  updating the weights of hidden layer to output layer
            outputNodeCounter = 0
            while outputNodeCounter < C:
                hiddenNodeCounter = 0
                while hiddenNodeCounter < H + 1:
                    w2[outputNodeCounter][hiddenNodeCounter] += rate * outputGradient[outputNodeCounter] * hiddenLayer[hiddenNodeCounter]
                    hiddenNodeCounter += 1
                outputNodeCounter += 1

            #  updating the weights of input layer to hidden layer
            hiddenNodeCounter = 0
            while hiddenNodeCounter < H:
                inpNode = 0
                while inpNode < len(inputVal):
                    w1[hiddenNodeCounter][inpNode] += rate * hiddenGradient[hiddenNodeCounter] * inputVal[inpNode]
                    inpNode += 1
                hiddenNodeCounter += 1

            #  L2 loss calculation
            outputNodeCounter = 0
            while outputNodeCounter < C:
                lossValues[iterations] += (output[dataCounter][outputNodeCounter] - outputLayer[outputNodeCounter]) ** 2
                outputNodeCounter += 1
            lossValues[iterations] *= 0.5

            if iterations >= 1:
                errConvChecks = lossValues [iterations] - lossValues[iterations - 1]

            dataCounter += 1
        iterations += 1

    return w1, w2, lossValues

# This function is used to propagate through the ANN and generate values for the output layer by using weight1 and
# weight2 and the values of the input layer o
def forwardPropagation(input,w1,w2,moves):
    output = [[0 for i in range(C)] for i in range(moves+1)] # initializes output list. This is the list that is returned
    count = 0
    while count <= moves:
        inputValues = input[count]
        hiddenLayer = np.zeros(H + 1)
        hiddenLayer[H] = 1  # Bias

        # generates values for the hidden layer
        hiddenNode = 0
        while hiddenNode < H:
            inpNode = 0
            while inpNode < len(inputValues):
                hiddenLayer[hiddenNode] += inputValues[inpNode] * w1[hiddenNode][inpNode]
                inpNode += 1
            hiddenLayer[hiddenNode] = activationFunction(hiddenLayer[hiddenNode])
            hiddenNode += 1

        # generates values for the output layer
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

    return output

# The code implemented below is used to run this agent with other agents
if input == '':
    matches = 0  # counts the number of moves in the game(1 move = both players played)
    object = ""
    history = "XXXX" # stores the values played by each of the 2 agents for 2 moves
    inputsArray = [[0 for i in range(D + 1)] for i in range(1000000)] # initializes list for input layer
    outputsArray = [[0 for i in range(C)] for i in range(1000000)] # initializes list for output layer
    dataIn = [] # used to store histroy values
    dataOut = [] # used to store predictions of what the opponent is going to play
    object = random.choice(['R','P','S'])
    history = history[1:]
    history += object
else:
    matches += 1
    print(matches)
    if matches >= 2: # matches should be >= 2 in order to make sure the string, hostory does not contain the character 'X' in it
        history = history[1:]
        history += input
        dataIn.append(history)
        dataOut.append(history[-1]) # last character in history is appended because according to the dataset provided for the other tasks, most of the time the opponents next move is the same as the move played by it in the last game
        num = matches - 2 # used to index correctly

        # 1-of-K encoding for inputsArray based on values in dataIn
        if dataIn[num][0] == 'R':
            inputsArray[num][0] = 1
        elif dataIn[num][0] == 'P':
            inputsArray[num][0] = 1
        elif dataIn[num][0] == 'S':
            inputsArray[num][2] = 1

        if dataIn[num][1] == 'R':
            inputsArray[num][3] = 1
        elif dataIn[num][1] == 'P':
            inputsArray[num][4] = 1
        elif dataIn[num][1] == 'S':
            inputsArray[num][5] = 1

        if dataIn[num][2] == 'R':
            inputsArray[num][6] = 1
        elif dataIn[num][2] == 'P':
            inputsArray[num][7] = 1
        elif dataIn[num][2] == 'S':
            inputsArray[num][8] = 1

        if dataIn[num][3] == 'R':
            inputsArray[num][9] = 1
        elif dataIn[num][3] == 'P':
            inputsArray[num][10] = 1
        elif dataIn[num][3] == 'S':
            inputsArray[num][11] = 1

        inputsArray[num][12] = 1

        # 1-of-K encoding for inputsArray based on values in dataOut
        if dataOut[num] == 'R':
            outputsArray[num][0] = 1
        elif dataOut[num] == 'P':
            outputsArray[num][1] = 1
        elif dataOut[num] == 'S':
            outputsArray[num][2] = 1

        outputs = [[0 for i in range(C)] for i in range(num+1)] # this list stores the predicted values that are going to be played by the opponent after back propagation and froward propagation are complete
        # training, backpropagation, forward propagation take place after every 100 moves
        if matches % 100 == 0:
            weight1,weight2,loss = backPropagation(inputsArray,outputsArray,weight1,weight2,learningRate,epoch,errorConvergence,num)
            outputs = forwardPropagation(inputsArray,weight1,weight2,num)

        index = -1
        if history in dataIn:
            index = dataIn.index(history)
            history = history[1:]
            history += object
            list = outputs[index]
            highestInd = list.index(max(list))

            if highestInd == 0:  # R
                object = "P"
            elif highestInd == 1:  # P
                object = "S"
            elif highestInd == 2:  # S
                object = "R"

        # if the value stored in history is not found in dataIn then the object played remains the same a
        else:
            object = object
            history = history[1:]
            history += object

    else:
        object = random.choice(['R', 'P', 'S'])

output = object




