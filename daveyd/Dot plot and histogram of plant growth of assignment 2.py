import pandas as pd
import matplotlib.pyplot as plt

growth_data = {
    'Music On': [304, 317, 332, 299, 0, 257, 387, 308, 206, 0, 174, 47, 317, 278, 0, 214, 157, 286,
                 188, 0, 69, 0, 236, 43, 0],
    'Music Off': [292, 292, 282, 3, 94, 270, 364, 149, 324, 164, 47, 316, 274, 2, 0, 288, 287, 319,
                  128, 0, 324, 75, 213, 219, 0]
}

df_growth = pd.DataFrame(growth_data)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df_growth['Music On'], bins=12, color='lightcoral', edgecolor='darkred', alpha=0.8)
plt.title('Histogram: Growth with Music')
plt.xlabel('Growth Value')
plt.ylabel('Frequency')
plt.grid(True, axis='y', linestyle='-', linewidth=0.7, alpha=0.8)

plt.subplot(1, 2, 2)
plt.hist(df_growth['Music Off'], bins=12, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
plt.title('Histogram: Growth without Music')
plt.xlabel('Growth Value')
plt.ylabel('Frequency')
plt.grid(True, axis='y', linestyle='-', linewidth=0.7, alpha=0.8)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(df_growth['Music On'], [0] * len(df_growth['Music On']), color='gold', alpha=0.6, s=70)
plt.title('Dot Plot: Growth with Music')
plt.xlabel('Growth Value')
plt.yticks([])  # Remove y-axis ticks
plt.axhline(0, color='black', linestyle='-', linewidth=1)

plt.subplot(1, 2, 2)
plt.scatter(df_growth['Music Off'], [0] * len(df_growth['Music Off']), color='royalblue', alpha=0.6, s=70)
plt.title('Dot Plot: Growth without Music')
plt.xlabel('Growth Value')
plt.yticks([])  # Remove y-axis ticks
plt.axhline(0, color='black', linestyle='-', linewidth=1)

plt.tight_layout()
plt.show()
