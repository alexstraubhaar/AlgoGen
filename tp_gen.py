__author__ = "Alex"
import sys
import math
import gen

class city:
    def __init__(self, name, x, y):
        self.name = name;
        self.x = x;
        self.y = y;

    def __str__(self):
        return (self.name + " " + self.x + " " + self.y)

"""Récupération des villes dans les fichiers et stockage dans un tableau d'objets 'city'"""
def cityParse(file):
    cities = []
    for line in file:
        data = []
        for info in line.split(' '):
            data.append(info)
        cities.append(city(data[0], data[1], data[2]))
    return cities

def distance(city1, city2):
    return math.sqrt(math.pow(int(city2.x) - int(city1.x), 2) + math.pow(int(city2.y) - int(city1.y), 2))



if __name__ == "__main__":
    file = open(sys.argv[1], 'r')
    results = cityParse(file)
    print(distance(results[0], results[1]))
