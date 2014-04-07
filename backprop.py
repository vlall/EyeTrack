from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.datasets 	import SupervisedDataSet
 
'''
Detailed metowrk topology, weights, connections- examined later.
this function just prints our final data. Move to separate file later.
'''
def printConnections(n):
    for mod in n.modules:
        for conn in n.connections[mod]:
            print conn
            for cc in range(len(conn.params)):
                print conn.whichBuffers(cc), conn.params[cc]

# Data object (8 inputs, 8 outputs)
ds = SupervisedDataSet(8,8)

'''
Open the data in the csv. Each row is one trial, each column is input or output (depending on network. 
For this network, the first 8 columns are inputs, second 8 outputs as defined by the above data object.
'''
tf = open('my_file.csv','r')

# Read all info on the csv. 
for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:8])
    outdata = tuple(data[8:])
    ds.addSample(indata,outdata)

'''
Make the actual neural networks
TOPOLOGY: 8 in, 8 hidden-0, 8 hidden-1, 8 out. Hidden layers subject to change
'''
n = buildNetwork(ds.indim,8,8,ds.outdim,recurrent=True)

#change learningrate based on gradient
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)

# 100 iterations
t.trainOnDataset(ds,100)
t.testOnData(verbose=True)

# Our prediction given 8 inputs, will print 8 estimated outputs
guess = n.activate((1,2,3,4,5,6,7,8)) 

print 'Final weights:',n.params

# Print our Guess 
print '\nGUESS???' + str(guess)
print (printConnections(n))

#print n['in'], n['out'], n[h0], n['h1']
