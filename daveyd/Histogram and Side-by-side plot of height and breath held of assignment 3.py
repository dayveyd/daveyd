import pandas as pd
import matplotlib.pyplot as plt

experiment_data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'BreathHoldDuration': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 9.09, 51.15, 58.32,
                          22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'HeightInCm': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158, 166, 175, 160, 165, 166, 170, 170, 172]
}

study_df = pd.DataFrame(experiment_data)

plt.figure(figsize=(15, 8))

plt.subplot(1, 2, 1)
plt.hist(study_df['BreathHoldDuration'], bins=10, color='indigo', edgecolor='black', alpha=0.8)
plt.title('Breath-Holding Time Distribution')
plt.xlabel('Duration (seconds)')
plt.ylabel('Number of Observations')
plt.grid(True, linestyle='-', alpha=0.5)

plt.subplot(1, 2, 2)

males_breath_time = study_df[study_df['Gender'] == 'Male']['BreathHoldDuration']
females_breath_time = study_df[study_df['Gender'] == 'Female']['BreathHoldDuration']

plt.scatter(males_breath_time, [0] * len(males_breath_time), color='teal', label='Males', alpha=0.7, s=120, edgecolor='black', marker='o')
plt.scatter(females_breath_time, [1] * len(females_breath_time), color='tomato', label='Females', alpha=0.7, s=120, edgecolor='black', marker='D')

plt.title('Comparison of Breath-Holding Time by Gender')
plt.yticks([0, 1], ['Male', 'Female'])
plt.xlabel('Breath-Holding Time (seconds)')
plt.legend(loc='upper left')
plt.axhline(y=0, color='gray', linewidth=0.5)

plt.tight_layout()

plt.show()