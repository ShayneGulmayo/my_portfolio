
class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize=floorSize
        self.noOfFloors=noOfFloors
        self.noOfDoors=noOfDoors

    def lightOpen(self):
        print("The light is on.")

    def ovenOpen(self):
        print("The oven is open")

class TownHouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors, noOfWindows):
        super().__init__(floorSize, noOfFloors, noOfDoors)
        self.noOfWindows=noOfWindows

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()

print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

townHouse = TownHouse(200, 2, 5, 15)

print("==Town House==")
print("Floor Size: ", townHouse.floorSize)
print("No. of Floors: ", townHouse.noOfFloors)
print("No. of Doors: ", townHouse.noOfDoors)
print("No. of Windows: ", townHouse.noOfWindows)

print("==Lights==")
townHouse.lightOpen()

print("==Oven==")
townHouse.ovenOpen()

print("==Both==")
townHouse.switchOn()