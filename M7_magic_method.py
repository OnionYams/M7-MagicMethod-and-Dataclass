

class Astronaut:
    def __init__(self,name,status,flight):
        self.__name = name
        self.__status = status
        self.__flight = flight

    def __str__(self):
        return (f"{self.__name}, {self.__status}")

    def __gt__(self,other):
            return self.flight > other.flight
    def __eq__(self,other):
            return self.flight == other.flight
    def __ge__(self,other):
            return self.flight >= other.flight


    @property
    def name(self):
        return self.__name
    @property
    def status(self):
        return self.__status
    @property
    def flight(self):
        return self.__flight
    
import csv

astros =  open("astronauts.csv")
astroDict = csv.DictReader(astros)

astroList = []
for astro in astroDict:
    astroList.append(Astronaut(astro["Name"],astro["Status"],astro["Space Flight (hr)"] ))


for astro in astroList:
    print(astro)

print(astroList[100] > astroList[50])
print(astroList[100] >= astroList[50])
print(astroList[100] == astroList[50])
