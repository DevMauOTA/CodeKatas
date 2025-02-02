from ChristmasLightGrid import ChristmasLightGrid

import pytest

@pytest.fixture()
def lightGrid():
    lightGrid = ChristmasLightGrid()
    return lightGrid

def test_deployGridSizeY(lightGrid):
    lightGrid.deployGrid(1000)
    assert lightGrid.GetSizeY() == 1000
