from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer, LinearLayer, SigmoidLayer
from pybrain.datasets 	         import SupervisedDataSet
 
'''
from pybrain.datasets.classification import ClassificationDataSet
# below line can be replaced with the algorithm of choice e.g.
# from pybrain.optimization.hillclimber import HillClimber
from pybrain.optimization.populationbased.ga import GA
from pybrain.tools.shortcuts import buildNetwork
 
# create XOR dataset
d = ClassificationDataSet(2)
d.addSample([0., 0.], [0.])
d.addSample([0., 1.], [1.])
d.addSample([1., 0.], [1.])
d.addSample([1., 1.], [0.])
d.setField('class', [ [0.],[1.],[1.],[0.]])
 
nn = buildNetwork(2, 3, 1)
# d.evaluateModuleMSE takes nn as its first and only argument
ga = GA(d.evaluateModuleMSE, nn, minimize=True)
for i in range(100):
    nn = ga.learn(0)[0]
       
In [68]: nn.activate([0,0])
Out[68]: array([-0.07944574])
 
In [69]: nn.activate([1,0])
Out[69]: array([ 0.97635635])
 
In [70]: nn.activate([0,1])
Out[70]: array([ 1.0216745])
 
In [71]: nn.activate([1,1])
Out[71]: array([ 0.03604205])

Detailed metowrk topology, weights, connections- examined later.
this function just prints our final data. Move to separate file later.
'''
def printConnections(n):
    for mod in n.modules:
        for conn in n.connections[mod]:
            print conn
            for cc in range(len(conn.params)):
                print conn.whichBuffers(cc), conn.params[cc]

# Data object (113 inputs, 1 output)
ds = ClassificationDataSet(113,1)

'''
Open the data in the csv. Each row is one trial, each column is input or output (depending on network. 
For this network, the first 113 columns are inputs, second 2 outputs as defined by the above data object.
'''
tf = open('new347.csv','r')

# Read all info on the csv. 
for line in tf.readlines():
    data = [(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:113])
    outdata = tuple(data[62358:])
    ds.addSample(indata,outdata)

'''
Make the actual neural networks
TOPOLOGY: 113 in, 60 hidden-0,1 out. Hidden layers subject to change
'''
n = buildNetwork(ds.indim,50,ds.outdim,recurrent=False)

#change learningrate based on gradient
t = BackpropTrainer(n,learningrate=.1,momentum=0.25,verbose=True)

# 100 iterations
t.trainOnDataset(ds,10000)
#runTraining(convergence=0)
t.testOnData(verbose=True)

# Our prediction given 113 inputs, will print 2 estimated outputs. SHOULD OUTPUT 1, 4
guess = n.activate((148.8,924.1,161.0,505.7,667.3,175.0,553.7,561.9,219.0,880.4,1056.5,57.0,806.7,459.4,67.0,466.2,450.2,401.0,705.5,456.9,230.0,391.2,461.7,525.0,415.8,469.9,283.0,750.1,465.7,262.0,843.5,466.9,460.0,609.0,495.7,320.0,666.8,1065.6,50.0,637.1,617.4,111.0,466.5,465.1,186.0,422.4,447.6,354.0,473.5,424.1,505.0,594.4,428.2,246.0,674.1,433.5,546.0,578.3,455.3,143.0,402.9,485.4,2087.0,546.4,498.3,101.0,626.2,829.5,62.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)) 
print 'Final weights:',n.params

print n['in'], n['out'], n['h0'], n['h1']
print (printConnections(n))

# Print our Guess 
print '\nGUESS???' + str(guess)
#saveNetwork('final.txt')
#t.trainUntilConvergence(dataset=None, maxEpochs=None, verbose=None, continueEpochs=10, validationProportion=0.50)
#t.trainUntilConvergence(ds)
