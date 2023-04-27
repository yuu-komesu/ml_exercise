import numpy as np
from numpy import sin, pi
# フォント設定
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

x=np.zeros(1, dtype=float)
def true_function(x):
    y = sin(pi * x * 0.8) * 10
    return y
    
plt.figure(0)
plt.plot(x, true_function(x))
plt.show()