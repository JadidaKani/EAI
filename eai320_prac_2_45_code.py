# Group no: 45
# Name: Jadida Kalim
# Student no: 21436054
# Name: Thabiso Nkosi
# Student no: 22507745

import random
import csv
import matplotlib.pyplot as plt

POPULATION = 1000  # variable used to set the initial population size
CHROMOSOME_LENGTH = 81  # sets the number of genes in an individual
MUTATION_RATE = 0.01  # sets the mutation rate

# This is a list called dictionary which stores lists of each of the 81 different sequences in the order in which
# they are visited by breadth first search (BFS) algorithm in a search tree of depth 4.
dictionary = [['RRRR'], ['RRRP'], ['RRRS'], ['RRPR'], ['RRPP'], ['RRPS'], ['RRSR'], ['RRSP'],
              ['RRSS'], ['RPRR'], ['RPRP'], ['RPRS'], ['RPPR'], ['RPPP'], ['RPPS'], ['RPSR'],
              ['RPSP'], ['RPSS'], ['RSRR'], ['RSRP'], ['RSRS'], ['RSPR'], ['RSPP'], ['RSPS'],
              ['RSSR'], ['RSSP'], ['RSSS'], ['PRRR'], ['PRRP'], ['PRRS'], ['PRPR'], ['PRPP'],
              ['PRPS'], ['PRSR'], ['PRSP'], ['PRSS'], ['PPRR'], ['PPRP'], ['PPRS'], ['PPPR'],
              ['PPPP'], ['PPPS'], ['PPSR'], ['PPSP'], ['PPSS'], ['PSRR'], ['PSRP'], ['PSRS'],
              ['PSPR'], ['PSPP'], ['PSPS'], ['PSSR'], ['PSSP'], ['PSSS'], ['SRRR'], ['SRRP'],
              ['SRRS'], ['SRPR'], ['SRPP'], ['SRPS'], ['SRSR'], ['SRSP'], ['SRSS'], ['SPRR'],
              ['SPRP'], ['SPRS'], ['SPPR'], ['SPPP'], ['SPPS'], ['SPSR'], ['SPSP'], ['SPSS'],
              ['SSRR'], ['SSRP'], ['SSRS'], ['SSPR'], ['SSPP'], ['SSPS'], ['SSSR'], ['SSSP'],
              ['SSSS']]

data = []  # this list helps store all the data read from the csv file
with open('data1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        data.append(row)

# This function uses the information read from the csv files to calculate how many times the opponent's next move is an R,
# P or S for each of the 81 sequences stored in the list (dictionary) above. It then returns a list containing all of the
# information gathered for each sequence
def getScores():
    x = 0
    scores = []  # A list used to store the lists of each sequence and their scores

    # The while loop loops through each and every sequence in dictionary and tries to find each specific sequence in the
    # list data in order to calculate the values for numR, numP and numS for each sequence in the dictionary.
    while x < CHROMOSOME_LENGTH:
        y = 0
        numR = 0  # stores the number of times the opponents next move is R for a specific sequence
        numP = 0  # stores the number of times the opponents next move is P for a specific sequence
        numS = 0  # stores the number of times the opponents next move is S for a specific sequence
        individual_scores = []  # A list used to store the values of numR, numP and numS for a specific sequence

        while y < len(data):
            if dictionary[x][0] == data[y][0]:
                if data[y][1] == "R":
                    numR += 1
                elif data[y][1] == "P":
                    numP += 1
                elif data[y][1] == "S":
                    numS += 1
            y += 1

        individual_scores.append(numR)
        individual_scores.append(numP)
        individual_scores.append(numS)

        scores.append(individual_scores)
        x += 1

    return scores

# This function randomly generates an initial population of size "POPULATION" and each individual contains 81 genes. It
# returns a list of all the randomly generated individuals
def initialization(size, numGenes):
    population = []
    i = 0
    while i < size:
        individual = ""
        j = 0
        while j<numGenes :
            gene = random.choice(['R', 'P', 'S'])
            individual += gene
            j += 1
        population.append(individual)
        i += 1

    return population

# This function returns a list with all the fitness scores of every individual in a population. In order to calculate the
# fitness of an individual, dictionary and the list returned from getScores is used. The fitness value is calculated based
# on the findings from getScores. If for example it was found that for a certain sequence R was played or played most of
# the time by the opponent, the gene corresponding to that sequence in the individual should be P because P beats R
# and we are trying to find a pseudo optimal solution that can be used to beat the opponent.
def fitnessFunction(s, pop, size):
    fitness = []  # list to store fitness values of each individual in the population
    i = 0

    # the finess values for each individual is initially set to 0
    while i<size:
        fitness.append(0)
        i += 1

    i = 0
    while i<size:
        str = pop[i]
        j = 0
        while j < len(s):
            sublist = s[j]
            maxNum = max(sublist)
            maxIndex = sublist.index(maxNum)
            if maxIndex == 0 and maxNum != 0:
                if str[j] == 'P':
                    fitness[i] += 1
            elif maxIndex == 1 and maxNum != 0:
                if str[j] == 'S':
                    fitness[i] += 1
            elif maxIndex == 2 and maxNum != 0:
                if str[j] == 'R':
                    fitness[i] += 1
            j += 1
        i += 1

    return fitness

# This function returns a list of selected parents. The individuals are ordered in descending order according to their
# fitness values and the top 50% of the individuals are selected and returned to be the parents of the next generation
def selection(pop, fitness):
    combinedList = list(zip(pop, fitness))
    combinedList.sort(key=lambda x: x[1], reverse=True)
    keeping = (len(pop))//2
    selected = []
    i = 0

    while i < keeping:
        selected.append(combinedList[i][0])
        i += 1

    return selected

# The crossover function returns a list of individuals that were produced by crossing over the genes of each of the parents
# with one another. The top 2 fittest parents also form part of the list that is returned and the individuals in the
# returned list become become part of the next generation
def crossover(parents):
    children = parents[:2]
    i = 2
    parent1 = parents[0]
    parent2 = parents[1]
    crossPoint = random.randint(1, len(parent1) - 1) # a random crossover point is selected to produce the new children

    child1 = parent1[:crossPoint] + parent2[crossPoint:]
    child2 = parent2[:crossPoint] + parent1[crossPoint:]
    children.append(child1)
    children.append(child2)

    while i< len(parents):
        parent1 = parents[random.randint(0,1)]
        parent2 = parents[i]
        crossPoint = random.randint(1, len(parent1) - 1) # a random crossover point is selected to produce the new children

        child1 = parent1[:crossPoint] + parent2[crossPoint:]
        child2 = parent2[:crossPoint] + parent1[crossPoint:]

        children.append(child1)
        children.append(child2)

        i += 1

    return children

# This function mutates the genes of the individuals within a population, depending on MUTATION_RATE. The second highest
# and highest fitness values within a population are found and individuals with these fitness values do not undergo mutation
def mutation(rate, pop, fitness):
    mutated = []
    topInd = []
    i = 0

    index = sorted(range(len(fitness)), key=lambda i: fitness[i], reverse=True)

    while i < len(index):
        if fitness[index[i]] != fitness[index[0]]:
            topInd.append(index[i])
            break
        if fitness[index[0]] == fitness[index[i]]:
            topInd.append(index[i])
        i += 1

    i = 0
    lastInd = len(topInd)-1
    lastIndNum = fitness[topInd[lastInd]]
    while i < len(fitness):
        if fitness[i] == lastIndNum:
            topInd.append(i)
        i += 1

    for i, ind in enumerate(pop):
        mutatedInd = ''
        for j, gene in enumerate(ind):
            if random.random() < rate:
                if i not in topInd:
                    if gene == 'R':
                        mutatedGene = random.choice(['P','S'])
                    elif gene == 'P':
                        mutatedGene = random.choice(['R','S'])
                    elif gene == 'S':
                        mutatedGene = random.choice(['R','P'])
                else:
                    mutatedGene = gene
            else:
                mutatedGene = gene
            mutatedInd += mutatedGene
        mutated.append(mutatedInd)

    return mutated

# This function is the function that basically runs the genetic algorithm and performs selection, crossover and mutation
# over a specified number of generations given a randomly generated initial population. If an individual has a fitness
# equal to the maximum fitness value calculated in this function then a string is returned of that individual as that
# is the optimal solution generated. The plotting function ,which used to help plot the graphs, is also called from within
# this function.
def GA(pop):
    maxGeneration = 100
    gen = 0
    i = 0
    zeros = 0
    fittestIndividual = []  # a list which stores the maximum fitness value in a population for each generation. This is used to help plot the graphs and is passed in as a parameter into the plotting function
    averageFitness = []  # a list which stores the average fitness value of a population for each generation. This is used to help plot the graphs and is passed in as a parameter into the plotting function
    scores = getScores()

    # calculates the number of sequences from the 81 sequences that have not been played according to the csv file read
    while i < len(scores):
        sublist = scores[i]
        maxNum = max(sublist)

        if maxNum == 0:
            zeros += 1
        i += 1

    maxFitness = CHROMOSOME_LENGTH - zeros  # calculates the maximum fitness that should be reached by the fittest individual

    while gen < maxGeneration:
        popFitness = fitnessFunction(scores, pop, len(pop))

        fittestIndividual.append(max(popFitness))
        average = sum(popFitness)//len(popFitness)
        averageFitness.append(average)

        parents = selection(pop, popFitness)  # Selection
        children = crossover(parents)  # Crossover
        childrenFitness = fitnessFunction(scores,children, len(children))

        mutated = mutation(MUTATION_RATE, children, popFitness)  # Mutation
        mutatedFitness = fitnessFunction(scores,mutated, len(mutated))

        if max(mutatedFitness) == maxFitness and (gen == maxGeneration-1):
            gen += 1
            #plotting(gen, fittestIndividual, averageFitness)  # called in order to plot the graphs
            maxIndex = childrenFitness.index(max(childrenFitness))
            string = children[maxIndex]
            newString = ','.join(string)   # seperates the genes with a comma between them. This string is returned so that it can be pasted in as the optimimal strategy returned by the csv file into the text file for data1 and data2
            return newString,string

        elif max(mutatedFitness) != maxFitness and (gen == maxGeneration-1):
            gen += 1
            #plotting(gen, fittestIndividual, averageFitness) # called in order to plot the graphs

        pop = mutated
        gen += 1

    return "",""

# This function helps plot the graphs required to show the effectiveness of the Genetic Algorithm
def plotting(maxGen,fittest,avgFitness):
    generations = range(0, maxGen)
    plt.plot(generations, fittest, label='Fittest Individual Fitness')
    plt.plot(generations, avgFitness, label='Average Fitness')
    plt.xlabel('Number of Generations')
    plt.ylabel('Fitness Values Generated')
    plt.legend()
    plt.xticks(range(0, maxGen + 1, 5))
    min_y = min(min(fittest), min(avgFitness))
    plt.yticks(range(int(min_y), 47, 1))
    plt.show()

# The code below this comment is used to run this agent with other agents
if input == '':
    matches = 0
    object = ""
    history = "XXXX"
    same = []  # this list stores the first 15 input values and is used to determine if the same values are constantly played
    population = initialization(POPULATION, CHROMOSOME_LENGTH)  # sets the initial population
    solution,solutionString = GA(population)  # calls GA function in order to get pseudo-optimal solution

    # This is there to make sure that solutionString is never empty
    while(solution == ""):
        population = initialization(POPULATION, CHROMOSOME_LENGTH)
        solution, solutionString = GA(population)

    object = random.choice(['R', 'P', 'S'])
    history = history[1:]
    history += object
else:
    matches += 1
    if matches != 1:  # this is to make sure that the first input value generated is not appended to history string
        history = history[1:]
        history += input

        if len(same) < 15:
            same.append(input)  # first 15 input values are stored

        # This is used to check if the current value in history is one of the sequences stored in dictionary
        # if it is, the index of that sequence is found and the move that would beat the move in the same index in
        # solutionString is played. If it isn't object remains the same.
        try:
            index = dictionary.index([history])
            history = history[1:]
            history += object
            index = dictionary.index([history])

            if solutionString[index] == "R":
                object = "P"
            elif solutionString[index] == "P":
                object = "S"
            elif solutionString[index] == "S":
                object = "R"

        except:
            object = object
            history = history[1:]
            history += object

    else:
        object = random.choice(['R', 'P', 'S'])

# This if statement checks if all the input values for the first 10 matches are the same. If they are then, depending
# on the constant value that is being played, the indexes for certain sequences are found and the move at that
# particular index in solutionString is played
if len(same) == 15:
    if all(element == same[0] for element in same):
        if same[0] == "R":
            index = dictionary.index(['PRPR'])
            object = solutionString[index]
        elif same[0] == "P":
            index = dictionary.index(['SPSP'])
            object = solutionString[index]
        elif same[0] == "S":
            index = dictionary.index(['RSRS'])
            object = solutionString[index]

output = object
















