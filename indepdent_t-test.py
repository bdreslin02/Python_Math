import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plot 

def import_data(file_path): 
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print("Error reading the file:", e)
        return None
    
def user_input_data():
    group1_data = input("Enter data for Group 1 as comma-separated values: ")
    group2_data = input("Enter data for Group 2 as comma-separated values: ")
    group1 = [float(x.strip()) for x in group1_data.split(',')]
    group2 = [float(x.strip()) for x in group2_data.split(',')]
    return group1, group2

data_source = input("Choose the source of your data(1: User input, 2: Import from file): ")

if data_source == '1':
    group1, group2 = user_input_data()
elif data_source == '2':
    file_path = input("Enter file path (CSV/Excel): ")
    data = import_data(file_path)
    if data is not None:
        group1 = data['Group1'].values
        group2 = data['Group2'].values
    else:
        exit()

levene_stat, levene_p = stats.levene(group1, group2)

t_stat, t_p = stats.ttest_ind(group1, group2)

mean_group1 = round(np.mean(group1), 3)
std_group1 = round(np.std(group1, ddof=1), 3)
mean_group2 = round(np.mean(group2), 3)
std_group2 = round(np.std(group2, ddof=1), 3)

descriptive_stats = pd.DataFrame({
    'Group 1': [mean_group1, std_group1],
    'Group 2': [mean_group2, std_group2]
}, index = ['Mean', 'Standard Deviation'])

print("Descriptive Statistics:")
print(descriptive_stats)

print("\nLevene's Test for Equality of Variances:")
print("Levene Statistic:", levene_stat)
print("Levene p-value:", levene_p)

t_stat = round(t_stat, 3)
t_p = round(t_p, 3)

print("\nInferential Statistics:")
print("t-statistic:", t_stat)
print("t-test p-value:", t_p)

plot.figure(figsize = (8, 6))
plot.subplot(2, 1, 1)
plot.plot(['Group 1'], [mean_group1], marker = 'o', linestyle = '-', color = 'b')
plot.title("Mean of Group 1")
plot.xlabel("Group 1")
plot.ylabel("Mean")
plot.grid(True)

plot.figure(figsize = (8, 6))
plot.subplot(2, 1, 2)
plot.plot(['Group 2'], [mean_group1], marker = 'o', linestyle = '-', color = 'r')
plot.title("Mean of Group 2")
plot.xlabel("Group 2")
plot.ylabel("Mean")
plot.grid(True)

plot.tight_layout()

plot.show()
