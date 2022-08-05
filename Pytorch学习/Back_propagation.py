import torch
x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

w = torch.Tensor([1.0])
w.requires_grad = True # 需要计算w梯度

def forward(x):
    return x*w

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y) ** 2 # 调用一次loss函数，就构建一次计算图

print('predict(before training)',4,forward(4).item())

for epoch in range(100):
    for x,y in zip(x_data,y_data):
        l = loss(x,y) 
        l.backward() #backward,compute grad for Tensor whose requires_grad set to True
        print('\tgrad:',x,y,w.grad.item()) #.item()的作用是将grad变成标量
        w.data = w.data - 0.01 * w.grad.data #做一个纯数值的计算
        w.grad.data.zero_() # 要对w的Tensor里面的grad要清零！
    print('progress:',epoch,l.item())
print('predict(after training',4,forward(4).item())
