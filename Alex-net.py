import tensorflow as tf

input = []

with tf.variable_scope('layer1'):
    weight = tf.get_variable(name = 'weight', shape = [11, 11, 3, 96], initializer = tf.contrib.layers.xavier_initializer())
    convolution_operation_layer1 = tf.nn.conv2d(input = input, filter = [11, 11, 3, 96], strides = [1, 1, 1, 1], padding = 'VALID', name = 'convolution_operation_layer1 ')
    bias = tf.get_variable(name = 'bias', shape = [])

    pool