import matplotlib.pyplot as plt

x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]
w = 1.0

def forward(x): #前馈计算
    return x*w

def cost(xs,ys): #Mean Square Error
    cost = 0
    for x,y in zip(xs,ys):
        y_pred = forward(x)
        cost += (y_pred - y) ** 2
    return cost/len(xs)
loss_list = []
Epoch_list = []
def gradient(xs,ys):
    grad = 0
    for x,y in zip(x_data,y_data):
        grad += 2*x*(x*w-y)
    return grad/len(xs)

print('Predict(before training)',4,forward(4))
for epoch in range(100):
    cost_val = cost(x_data,y_data)
    grad_val = gradient(x_data,y_data)
    w -= 0.05*grad_val
    loss_list.append(cost_val)
    Epoch_list.append(epoch)
    print('Epoch:',epoch,'w=',w,'loss',cost_val)
    
print('Predict(after training)',4,forward(4))
plt.plot(Epoch_list,loss_list)
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.show()



