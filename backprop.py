from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.datasets import SupervisedDataSet

#Data 
ds = SupervisedDataSet(8,8)

tf = open('my_file.csv','r')

for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:8])
    outdata = tuple(data[8:])
    ds.addSample(indata,outdata)

n = buildNetwork(ds.indim,8,8,ds.outdim,recurrent=True)
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)
t.trainOnDataset(ds,100)
t.testOnData(verbose=True)
guess = n.activate((1,2,3,4,5,6,7,8)) 
print 'Final weights:',n.params
print '\n\n\n\nGUESS???' + str(guess)
