import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from two_layer_net import TwoLayerNet


#データ読み込み
(x_train, t_train),(x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
#ネットのサイズを決める
network = TwoLayerNet(input_size=784,hidden_size=64,output_size=10)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_data = []
train_accuracy_data = []
test_accuracy_data = []

iter_per_epoch = max(train_size/batch_size,1)
print(iter_per_epoch)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    grad = network.gradient(x_batch,t_batch)
    
    for key in {"W1","b1","W2","b2"}:
        network.params[key] -= grad[key]*learning_rate

    loss = network.loss(x_batch,t_batch)
    train_loss_data.append(train_accuracy_data)
    
    if i%iter_per_epoch == 0:
        train_accuracy = network.accuracy(x_train,t_train)
        test_accuracy = network.accuracy(x_test,t_test)
        train_accuracy_data.append(train_accuracy)
        test_accuracy_data.append(test_accuracy)
        print(train_accuracy, test_accuracy,i/iter_per_epoch)
    