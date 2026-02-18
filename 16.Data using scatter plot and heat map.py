import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
np.random.seed(0) 
x = np.random.rand(100) * 10   
y = np.random.rand(100) * 10   
heatmap_data = np.random.rand(10, 10) 
plt.figure(figsize=(12, 6))   
plt.subplot(1, 2, 1)   
plt.scatter(x, y, color='blue', alpha=0.7) 
plt.title("Scatter Plot") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.subplot(1, 2, 2)   
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', cbar=True) 
plt.title("Heatmap") 
plt.tight_layout()   
plt.show()
