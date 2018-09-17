from uuid import uuid4
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from varmap import VarMap


class FFPolicy(object):
    """
    Basic feedforward policy. Default for most agents.
    """
    def __init__(self,
                 input_dim,
                 output_dim,
                 depth=3,
                 hidden_width=None):
        self.depth = depth

        hidden_width = hidden_width or (int(input_dim * 0.75) + 1)

        model = Sequential()
        model.add(Dense(hidden_width, input_dim=input_dim))
        model.add(Activation('tanh'))
        model.add(Dense(hidden_width))
        model.add(Activation('tanh'))
        model.add(Dense(output_dim))
        model.add(Activation('softmax'))
        model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        self.model = model
        self.weight_shapes = self.get_weight_shapes()
        self.total_params = self.get_total_params()

    def set_model_weights(self, weights):
        weights = self.get_subarrays_from_shapes(weights)
        self.model.set_weights(weights)

    def get_weight_shapes(self):
        weights = self.model.get_weights()
        shapes = []

        for thing in weights:
            shapes.append(thing.shape)

        return shapes

    def get_total_params(self):
        total = 0

        for shape in self.weight_shapes:
            if len(shape) == 1:
                total += shape[0]
            elif len(shape) == 2:
                total += shape[0] * shape[1]

        return total

    def get_subarrays_from_shapes(self, arr_1d):
        slices = []
        idx = 0

        for i, shape in enumerate(self.weight_shapes):
            if len(shape) == 1:
                num = shape[0]
            elif len(shape) == 2:
                num = shape[0] * shape[1]

            if i == 0:
                slc = np.array(arr_1d[:num]).reshape(shape)
                idx += num
            elif i == len(self.weight_shapes) - 1:
                slc = np.array(arr_1d[idx:]).reshape(shape)
            else:
                slc = np.array(arr_1d[idx:idx + num]).reshape(shape)
                idx += num

            slices.append(slc)

        return slices