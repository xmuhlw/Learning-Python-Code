import matplotlib.pyplot as plt

x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]
w = 1.0

def forward(x): #前馈计算
    return x*w

def loss(x,y): #Mean Square Error
    y_pred = forward(x)
    return (y_pred - y) ** 2

loss_list = []
Epoch_list = []

def gradient(x,y):
    return 2*x*(x*w-y)

print('Predict(before training)',4,forward(4))

for epoch in range(100):
    for x,y in zip(x_data,y_data):
        grad = gradient(x,y)
        w = w - 0.01 * grad
        print('\grad',x,y,grad)
        l = loss(x,y)
        loss_list.append(l)
        Epoch_list.append(epoch)
        
        
print('Predict(after training)',4,forward(4))
plt.plot(Epoch_list,loss_list)
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.show()



