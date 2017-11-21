from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import time
import tensorflow as tf
import dataset
import autoencoder


def main():
	input_dim = 784
	hid_dim = 4

	lrn_rate = 0.01
	momentum = 0
	batch_size_train = 64
	epoch_max = 10
	
	train_size = 3000
	#reg_lambda = 1.0 / train_size
	reg_lambda = 0

	# Redundant for autoencoder
	class_num = 10

	train_file_name = '../../hw1_data/digitstiny.txt'
	val_file_name = '../../hw1_data/digitstiny.txt'
	test_file_name = '../../hw1_data/digitstiny.txt'

	log_file_name = './log/log_test_01.txt'

	ae_machine = autoencoder(input_dim, hid_dim, class_num, lrn_rate, momentum, batch_size_train, epoch_max, reg_lambda, train_file_name, val_file_name, test_file_name, log_file_name)

	ae_machine.train()


if __name__ == '__main__':
	tf.app.run(main = main, argv = None)
