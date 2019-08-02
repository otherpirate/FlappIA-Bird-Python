from random import uniform

BIAS = 1


class Neuron(object):
    def __init__(self, weights, error, output):
        self.weights = weights
        self.error = error
        self.output = output
        self.connections = len(weights)


class Layer(object):
    def __init__(self, neurons):
        self.neurons = neurons


class RNA(object):

    def __init__(self, hidden_layers, neuron_input, neuron_hidden, neuron_output):
        neurons = []
        neuron_input = neuron_input + BIAS
        for _ in range(neuron_input):
            neurons.append(Neuron([], 0, 1.0))
        self.input_layer = Layer(neurons)

        total_weights = 0
        self.hidden_layers = []
        neuron_hidden = neuron_hidden + BIAS
        for _ in range(hidden_layers):
            neurons = []
            for i in range(neuron_hidden):
                size = neuron_hidden
                if i == 0:
                    size = neuron_input
                neuron = self._build_hidden_neuron(size)
                neurons.append(neuron)
                total_weights += size
            self.hidden_layers.append(Layer(neurons))

        neurons = []
        for i in range(neuron_output):
            neuron = self._build_hidden_neuron(neuron_output)
            neurons.append(neuron)
            total_weights += neuron_output
        self.hidden_layer = Layer(neurons)

        self.total_weights = total_weights

    @staticmethod
    def _build_hidden_neuron(size):
        weights = []
        for i in range(size):
            value = uniform(0.0, 2.0)
            weights.append(value)
        return Neuron(weights, 0, 1)
