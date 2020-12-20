import numpy as np

from blueprint import datasets, estimators, activation_functions, loss_functions, plot_utils


if __name__ == '__main__':
  # set random number generator seed
  np.random.seed(0)

  # set floating point formatting when printing
  np.set_printoptions(formatter = {'float': '{:.5f}'.format})

  # load data
  dataset = datasets.logic_gate_and

  x = dataset.input
  d = dataset.output

  # define the estimator parameters
  n = 1e-3
  g = activation_functions.heaviside
  epochs = 1e3

  # create the estimator
  estimator = estimators.Perceptron(n, g, epochs)

  # train the estimator
  w = estimator.train(x, d)

  # evaluate the estimator
  accuracy = estimator.evaluate(x, d, w)

  # plot epoch vs error
  plot_utils.line(estimator.plot_data_x, estimator.plot_data_y, x_label = 'epoch', y_label = 'error')
