# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

# incident flux
Load(Filename='/home/8cz/Workbench/MANTID/PD67_PlaczekCorrection/data/fluxSmoothedNOM161959.nxs', OutputWorkspace='influx')
CropWorkspace(InputWorkspace='influx',
              OutputWorkspace='influx',
              XMin=0.10000000000000001,
              XMax=2.8999999999999999)
              
Load(Filename='/home/8cz/Workbench/MANTID/PD67_PlaczekCorrection/data/inputwsNOM_164109.nxs', OutputWorkspace='inputwsNOM_164109')
SetSampleMaterial(InputWorkspace='inputwsNOM_164109',
                  ChemicalFormula='Cs-Cl',
                  SampleMassDensity=3.9990000000000001)

CalculatePlaczek(
    InputWorkspace="inputwsNOM_164109",
    IncidentSpectra="influx",
    LambdaD=1.44,
    Order=2,
    SampleTemperature=943.15,
    ScaleByPackingFraction=False,
    CrystalDensity=0.01,
    OutputWorkspace="NOM_P2",
)