class ChristmasLightGrid:

    def deployGrid(self, y=0, x=0):
        self.y = y
        self.x = x

    def getSize(self):
        return f"y={self.y} x={self.x}"

    def turnOnLights(self):
        return "Lights turned on"

    def returnLightsOnCount(self):
        return self.y*self.x