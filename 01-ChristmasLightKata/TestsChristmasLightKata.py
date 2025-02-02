from ChristmasLightGrid import ChristmasLightGrid

import pytest

@pytest.fixture()
def lightGrid():
    lightGrid = ChristmasLightGrid()
    return lightGrid

def test_deployGrid(lightGrid):
    lightGrid.deployGrid(1000, 1000)
    assert lightGrid.getSize() == "y=1000 x=1000"

def test_turnOnAllLightsReturnsMessage(lightGrid):
    lightGrid.turnOnLights()
    assert lightGrid.turnOnLights() == "Lights turned on"

def test_returnHowManyLightsTurnedOn(lightGrid):
    lightGrid.deployGrid(1000, 1000)
    lightGrid.returnLightsOnCount()
    assert lightGrid.returnLightsOnCount() == 1000000