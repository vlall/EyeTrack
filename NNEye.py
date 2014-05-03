import EyeObject
from pybrain.datasets.classification import ClassificationDataSet
# below line can be replaced with the algorithm of choice e.g.
# from pybrain.optimization.hillclimber import HillClimber
from pybrain.optimization.populationbased.ga import GA
from pybrain.tools.shortcuts import buildNetwork
 
# create XOR dataset
d = ClassificationDataSet(113)
EyeTrack = EyeObject.ReadExcel("new")
EyeTrack.format_Array()
outter = EyeTrack.get_Outter()
outterLen = len(EyeTrack.get_Outter())

for i in range (outterLen-1):
	d.addSample(outter[i][0:113],outter[i][-1])

	#d.addSample([0., 0.], [0.])

#d.setField('class', [ [1],[2],[3],[4] [5]] )
 
nn = buildNetwork(113, 60, 1)
# d.evaluateModuleMSE takes nn as its first and only argument
ga = GA(d.evaluateModuleMSE, nn, minimize=True)
for i in range(100):
    nn = ga.learn(0)[0]
       
print round(nn.activate([148.8, 924.1, 161.0, 505.7, 667.3, 175.0, 553.7, 561.9, 219.0, 880.4, 1056.5, 57.0, 806.7, 459.4, 67.0, 466.2, 450.2, 401.0, 705.5, 456.9, 230.0, 391.2, 461.7, 525.0, 415.8, 469.9, 283.0, 750.1, 465.7, 262.0, 843.5, 466.9, 460.0, 609.0, 495.7, 320.0, 666.8, 1065.6, 50.0, 637.1, 617.4, 111.0, 466.5, 465.1, 186.0, 422.4, 447.6, 354.0, 473.5, 424.1, 505.0, 594.4, 428.2, 246.0, 674.1, 433.5, 546.0, 578.3, 455.3, 143.0, 402.9, 485.4, 2087.0, 546.4, 498.3, 101.0, 626.2, 829.5, 62.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
