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

    def replace_values(self, values):
        for i in range(len(values)):
            self.neurons[i].output = values[i]


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
        for _ in range(neuron_output):
            neuron = self._build_hidden_neuron(neuron_hidden)
            neurons.append(neuron)
            total_weights += neuron_output
        self.hidden_layer = Layer(neurons)

        self.total_weights = total_weights
        self.output_layer = Layer(neurons)

    def calculate_output(self):
        for i in range(len(self.hidden_layers[0].neurons) - BIAS):
            total = 0
            for j, neuron in enumerate(self.input_layer.neurons):
                total += neuron.output * self.hidden_layers[0].neurons[i].weights[j]
            self.hidden_layers[0].neurons[i].output = self.limit_sum_value(total)

        for k in range(1, len(self.hidden_layers)):
            for i in range(len(self.hidden_layers[k].neurons) - BIAS):
                total = 0
                for j in range(len(self.hidden_layers[k-1].neurons) - BIAS):
                    total += self.hidden_layers[k-1].neurons[j].output * self.hidden_layers[k].neurons[i].output.weights[j]
                self.hidden_layers[k].neurons[i].output = self.limit_sum_value(total)

        k = len(self.hidden_layers) - 1
        for neuron in self.output_layer.neurons:
            total = 0
            for j in range(len(self.hidden_layers[k-1].neurons)):
                total += self.hidden_layers[k-1].neurons[j].output * neuron.weights[j]
            neuron.output = self.limit_sum_value(total)

    @property
    def should_jump(self):
        return self.output_layer.neurons[0].output > 0.0

    @staticmethod
    def limit_sum_value(value):
        if value < 0:
            return 0
        elif value > 10000:
            return 10000
        return value

    @staticmethod
    def _build_hidden_neuron(size):
        weights = []
        for i in range(size):
            value = uniform(0.0, 2.0)
            weights.append(value)
        return Neuron(weights, 0, 1)
