ss=15
ts=20
Fs=25
nu = int(input(print("Enter num of units:")))
x=nu*ss
y=nu*ts
z=nu*Fs
xgst=x*(0.05)
ygst=y*(0.05)
zgst=z*(0.05)

if nu in range(1, 100):
      print("Free of cost")
elif nu in range(101, 200):
      print("Total bill: ", x+xgst)
elif nu in range(201, 300):
      print("Total bill: ", y+ygst)
else: 
      print("Total bill: ", z+zgst)


