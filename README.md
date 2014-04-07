EyeTrack
========

A PyBrain neural network for the mimicking the human visual cortex during scene, object, and face processing

###Project
EyeTrack relies on EyeTracker data provided by a device (camera/sensors/software) that can sense the distance, direction, and duration of eye movements (saccades) on points in 2-D space. Experiments are conducted by allowing subjects to view images of scenes, faces, and objects naturally, attempting to identify the pattern in the relationship between the picture's contents and eye movement. 

###Methods
Currently using backpropagation neural networks with a tology subject to many changes. The network is currently basic and processes mock data provided from csv random functions. The actual data may require separate networks for each of the processess. I would imagine scene processing would require a higher complexity of topology vs a face network, due to the less uniform nature when we process scenes. 
