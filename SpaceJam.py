from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as Spacejamclasses
import DefensePaths as DefensePaths
from panda3d.core import *
from panda3d.core import Vec3

class xz():
    circleIncrement = 0

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetScene()

    def DrawCloudDefense(self, centralObject, droneName): 
        unitVec = DefensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()  
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 10)
        #self.Drone = Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, 'Drone', "./Assets/DroneDefender/Drones.jpg", position, 50)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1): 
        unitVec = DefensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()  
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 5)

    def DrawAxisDronesXY(self, centralObject, droneName):
        unitVec = DefensePaths.axisDronesXY ()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()  
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 5)

    def DrawAxisDronesXZ(self, centralObject, droneName):
        unitVec = DefensePaths.axisDronesXZ ()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()  
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 5)

    def DrawAxisDronesYZ(self, centralObject, droneName):
        unitVec = DefensePaths.axisDronesYZ ()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()  
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 5)

    def DrawCircleXZ(self, centralObject, droneName):
        unitVec = DefensePaths.axisDronesXZ()
        unitVec.normalize()
        position = unitVec * 300 + centralObject.modelNode.getPos()
        Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/Drones.jpg", position, 5)

    def SetScene(self):
        self.Universe = Spacejamclasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/Universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/Planet1.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/Planet2.jpg", (0, 6000, 0), 300)
        self.Planet3 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/Planet3.jpg", (500, -5000, 200), 500)
        self.Planet4 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/Planet4.jpg", (300, 6000, 500), 150)
        self.Planet5 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/Planet5.jpg", (700, -2000, 100), 500)
        self.Planet6 = Spacejamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/Planet6.jpg", (0, -900, -1400), 700)
        self.SpaceStation1 = Spacejamclasses.Station(self.loader, "./Assets/Space Station/spaceStation.egg", self.render, 'Space Station', "./Assets/Space Station/SpaceStation1_Dif2.png", (1500, 1000, -100), 40)
        self.Hero = Spacejamclasses.Player(self.loader, "./Assets/Spaceships/theBorg.x", self.render, 'Hero', "./Assets/Spaceships/theBorg.jpg", Vec3(1000, 1200, -50), 10)
        #self.Drone = Spacejamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, 'Drone', "./Assets/DroneDefender/Drones.jpg", Vec3(1000, 100, 0), 50)

def Scene(self):
    fullCycle = 60
    for j in range(fullCycle):
        Spacejamclasses.Drone.droneCount += 1
        nickName = "Drone" + str(Spacejamclasses.Drone.droneCount)
        self.DrawCloudDefense(self.Planet1, nickName)
        self.DrawBaseballSeams(self.Planet2, nickName, j, fullCycle, 2)
        self.DrawAxisDronesXY(self.Planet3, nickName)
        self.DrawAxisDronesXZ(self.Planet3, nickName)
        self.DrawAxisDronesYZ(self.Planet3, nickName)
        
app = SpaceJam()
app.run()
