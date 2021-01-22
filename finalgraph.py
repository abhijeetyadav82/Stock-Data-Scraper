import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

def animate(i):
	df = pd.read_csv('stock_data.csv')
	ys = df.iloc[1:, 2].values
	xs = list(range(1,len(ys)+1))
	ax1.clear()
	ax1.plot(xs,ys)
	ax1.set_title('Apple', fontsize=12)

	df = pd.read_csv('stock_data.csv')
	ys = df.iloc[1:, 3].values
	ax2.clear()
	ax2.plot(xs,ys)
	ax2.set_title('Tesla', fontsize=12)

	df = pd.read_csv('stock_data.csv')
	ys = df.iloc[1:, 4].values
	ax3.clear()
	ax3.plot(xs,ys)
	ax3.set_title('Microsoft', fontsize=12)

	df = pd.read_csv('stock_data.csv')
	ys = df.iloc[1:, 5].values
	ax4.clear()
	ax4.plot(xs,ys)
	ax4.set_title('Amazon', fontsize=12)
 
ani = animation.FuncAnimation(fig, animate,interval=1000)
plt.tight_layout()
plt.show()