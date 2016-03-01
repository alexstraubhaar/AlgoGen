__author__ = "Alex"
import sys
import math
import random

#Classes
class City:
    def __init__(self, name, x, y):
        self.name = name;
        self.x = x;
        self.y = y;

    def __str__(self):
        return (self.name + " " + self.x + " " + self.y)

    def position(self):
        return self.x, self.y

    def distance(self, dest):
        return math.hypot(self.x - dest.x, self.y - dest.y)


class Chromosome:
    def __init__(self, genes, distances):
        self.genes = genes
        self.eval = evaluate(self, distances)


#Fonctions
def evaluate(population, distances):
    evaluation = 0
    for i in range(len(population.genes) - 1):
        evaluation += distances[population.genes[i]][population.genes[i + 1]]
    return evaluation

def croisement(pere, mere):
    nouveau = father[:random.randint(0, len(pere) - 1)]
    nouveau[len(nouveau):] = [j for j in mere if j not in nouveau]
    return nouveau

def evolution(chromosomes, distances):
    taille = len(chromosomes)

    #Sélection par roue
    nouvellepop = roue(chromosomes, taille)

    #Croisement
    for i in xrange(0, len(nouvellepop), 2):
        pere = nouvellepop[i].genes
        mere = nouvellepop[i + 1].genes

        nouvellepop[len(nouvellepop):] = [Chromosome(croisement(pere, mere), distances)]
        nouvellepop[len(nouvellepop):] = [Chromosome(croisement(mere, pere), distances)]

    #Mutation
    for i in xrange(len(nouvellepop)):
        if random.randint(0, 10) < 1:
            coupe1 = random.randint(1, len(nouvellepop[i].genes) - 2)
            coupe2 = random.randint(coupe1 + 1, len(nouvellepop[i].genes) - 1)

#Récupération des villes dans les fichiers et stockage dans un tableau d'objets 'city'
def cityParse(file):
    cities = []
    for line in file:
        data = []
        for info in line.split(' '):
            data.append(info)
        cities.append(City(data[0], data[1], data[2]))
    return cities

# Sélection par roue
def roue(population, taille):
    moyenne = 0
    for p in population:
        moyenne += p.eval
    moyenne /= taille
    for p in population:
        p.chance = moyenne / p.eval
    nouvellepop = []
    for i in xrange(taille / 2):
        nouvellepop[len(nouvellepop):] = [population.population(random.randint(0, len(population) - 1))]
    population.extend(nouvellepop)
    return nouvellepop


if __name__ == "__main__":
    file = open(sys.argv[1], 'r')
    results = cityParse(file)
