import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plot
from scipy.interpolate import make_interp_spline
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Create a function to import data from a file
def import_data(file_path): 
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print("Error reading the file:", e)
        return None

# Create a function to allow users to manually input data
def user_input_data():
    group1_data = entry_group1.get()
    group2_data = entry_group2.get()

    try:
        group1 = [float(x.strip()) for x in group1_data.split(',')]
        group2 = [float(x.strip()) for x in group2_data.split(',')]
        return group1, group2
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input data. Please enter numeric values separated by commas.")
        return None, None

# Create a function to allow users to choose their desired source of data
def choose_data_source():
    source_choice = data_source_var.get()

    if source_choice == "User Input":
        group1, group2 = user_input_data()
        if group1 is not None and group2 is not None:
            perform_t_test(group1, group2)
    elif source_choice == "Input Data":
        file_path = filedialog.askopenfilename(title="Select CSV/Excel file")
        if file_path:
            data = import_data(file_path)
            if data is not None: 
                group1 = data['Group 1'].values
                group2 = data['Group 2'].values 
                perform_t_test(group1, group2)
    else:
        messagebox.showerror("Input Error", "Please choose a data source.")

# Create a function that performs the statistical tests
def perform_t_test(group1, group2):
    try:
        # Calculate descriptive statistics, round to three significant figures
        global n_group1, n_group2, mean_group1, mean_group2, std_group1, std_group2
        n_group1 = len(group1)
        n_group2 = len(group2)
        mean_group1 = round(np.mean(group1), 3)
        std_group1 = round(np.std(group1, ddof = 1), 3)
        mean_group2 = round(np.mean(group2), 3)
        std_group2 = round(np.std(group2, ddof = 1), 3)

        # Run Levene's test, round to three significant figures
        global levene_stat, levene_p
        levene_stat, levene_p = stats.levene(group1, group2)
        levene_stat = round(levene_stat, 3)
        levene_p = round(levene_p, 3)

        # Run the t-test, round to three significant figures
        global df, t_stat, t_p, equality_of_variances, mean_difference, std_error, confidence_interval, t_critical, lower_bound, upper_bound
        df = (n_group1 + n_group2) - 2
        t_stat, t_p = stats.ttest_ind(group1, group2)
        t_stat = round(t_stat, 3)
        t_p = round(t_p, 3)
        mean_difference = mean_group1 - mean_group2
        std_error = np.sqrt((std_group1**2 / n_group1) + (std_group2**2 / n_group2))
        confidence_interval = 0.95
        t_critical = stats.t.ppf((1 + confidence_interval) / 2, df)
        lower_bound = mean_difference - (t_critical * std_error)
        upper_bound = mean_difference + (t_critical * std_error)

        # Define p-value cutoffs for significance
        equality_of_variances = levene_p > 0.05
        t_test_significant = t_p < 0.05

        create_table(n_group1, n_group2, mean_group1, mean_group2, std_group1, std_group2, levene_stat, levene_p, t_stat, df, t_p, mean_difference, lower_bound, upper_bound)

        # Create statistical significance decision message
        decision = ""
        if equality_of_variances:
            if t_test_significant:
                decision += "Equality of variances: Passed, groups are homogenous\nT-Test: Significant"
            else:
                decision += "Equality of variances: Passed, groups are homogenous\nT-Test: Not significant"
        else:
            decision += "Equality of variances: Failed, groups are not homogenous\nT-Test: Not performed"

        result_var.set(decision)

        # Create a figure
        plot.figure(figsize = (8, 6))

        # Create a smoothed line graph for group 1
        plot.subplot(2, 1, 1)
        x_smooth = np.linspace(1, len(group1), 300)
        spl = make_interp_spline(range(1, len(group1) + 1), group1, k = 3)
        y_smooth = spl(x_smooth)
        plot.plot(x_smooth, y_smooth, color = 'b')
        plot.title("Group 1 Data")
        plot.xlabel("Data Point")
        plot.ylabel("Value")
        plot.grid(True)

        # Create a smoothed line graph for group 2
        plot.subplot(2, 1, 2)
        x_smooth = np.linspace(1, len(group2), 300)
        spl = make_interp_spline(range(1, len(group2) + 1), group2, k = 3)
        y_smooth = spl(x_smooth)
        plot.plot(x_smooth, y_smooth, color = 'r')
        plot.title("Group 2 Data")
        plot.xlabel("Data Point")
        plot.ylabel("Value")
        plot.grid(True)

        plot.tight_layout()

        plot.show()
    except Exception as e: 
        result_var.set("Error performing t-test:\n" + str(e))

def create_table(n_group1, n_group2, mean_group1, mean_group2, std_group1, std_group2, levene_stat, levene_p, t_stat, df, t_p, mean_difference, lower_bound, upper_bound):
    global stats_frame
    stats_frame = ttk.Frame(window)
    stats_frame.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nsew")

    # Create a table for descriptive statistics
    descriptive_stats = ttk.Treeview(stats_frame, columns=("Group", "N", "Mean", "Std. Deviation"))
    descriptive_stats.heading("Group", text="Group")
    descriptive_stats.heading("N", text="N")
    descriptive_stats.heading("Mean", text="Mean")
    descriptive_stats.heading("Std. Deviation", text="Std. Deviation")
    descriptive_stats.insert("", "end", values=("Group 1", n_group1, mean_group1, std_group1))
    descriptive_stats.insert("", "end", values=("Group 2", n_group2, mean_group2, std_group2))
    descriptive_stats.grid(row = 0, column = 0, padx = 10, pady = 5)

    # Create a table for inferential statistics
    inferential_stats = ttk.Treeview(stats_frame, columns=("Variances", "F", "Sig.", "t", "df", "Sig. (2-tailed)", "Mean Difference", "Lower Bound", "Upper Bound"))
    inferential_stats.heading("Variances", text="")
    inferential_stats.heading("F", text="F")
    inferential_stats.heading("Sig.", text="Sig.")
    inferential_stats.heading("t", text="t")
    inferential_stats.heading("df", text="df")
    inferential_stats.heading("Sig. (2-tailed)", text="Sig. (2-tailed)")
    inferential_stats.heading("Mean Difference", text="Mean Difference")
    inferential_stats.heading("Lower Bound", text="Lower Bound")
    inferential_stats.heading("Upper Bound", text="Upper Bound")
    inferential_stats.insert("", "end", values=("Equal variances assumed", levene_stat, levene_p, t_stat, df, t_p, mean_difference, lower_bound, upper_bound))
    inferential_stats.grid(row = 1, column = 0, padx = 10, pady = 5)

def on_resize(event):
    # Update the column and row weights to make the tables responsive
    stats_frame.columnconfigure(0, weight = 1)
    stats_frame.columnconfigure(1, weight = 1)
    stats_frame.rowconfigure(0, weight = 1)

# Create a GUI window
window = tk.Tk()
window.title("T-Test Results")

# Create a variable to store data source choice
data_source_var = tk.StringVar()
data_source_var.set("User Input")

# Create and place input fields and labels
label_data_source = ttk.Label(window, text = "Select Data Source:")
label_data_source.grid(row = 0, column = 0, padx = 5, pady = 5)
data_source_menu = ttk.OptionMenu(window, data_source_var, "User Input", "Import Data")
data_source_menu.grid(row = 0, column = 1, padx = 5, pady = 5)

label_group1 = ttk.Label(window, text = "Group 1 Data:")
label_group2 = ttk.Label(window, text = "Group 2 Data:")

entry_group1 = ttk.Entry(window, width = 40)
entry_group2 = ttk.Entry(window, width = 40)

label_group1.grid(row = 1, column = 0, padx = 5, pady = 5)
entry_group1.grid(row = 1, column = 1, padx = 5, pady = 5)
label_group2.grid(row = 2, column = 0, padx = 5, pady = 5)
entry_group2.grid(row = 2, column = 1, padx = 5, pady = 5)

# Create a button to calculate statistics
calculate_button = ttk.Button(window, text = "Run independent-samples t-test", command = choose_data_source)
calculate_button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 10)

# Create a label to display the results
result_var = tk.StringVar()
result_label = ttk.Label(window, textvariable=result_var, wraplength = 600)
result_label.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 5)

# Make the window resizable
window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 1)

# Bind the resize event to the on_resize function
window.bind("<Configure>", on_resize)

# Start the GUI application
window.mainloop()