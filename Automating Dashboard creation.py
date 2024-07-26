import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data from Excel file
excel_file = "nba1.xlsx"
df = pd.read_excel(excel_file)



# Define your dashboard functions
def plot_bar_chart(df, column, ax):
    sns.countplot(data=df, x=column, color='#0DD6FF', edgecolor='Black', ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column, fontsize=8)
    ax.set_ylabel("Count", fontsize=8 )
    ax.tick_params(rotation=45)
    ax.set_facecolor('#090B4D')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)
# Add labels inside the bars
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 8), 
                    textcoords = 'offset points',
                    color='white')  # Adjust the position and font properties as needed

def plot_histogram(df, column, ax):
    sns.histplot(data=df, x=column, bins=20, kde=True, ax=ax)
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column, fontsize=6)
    ax.set_ylabel("Frequency")
    ax.set_facecolor('#F2F2F2')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)
def plot_boxplot(df, x_column, y_column, ax):
    sns.boxplot(data=df, x=x_column, y=y_column, ax=ax)
    ax.set_title(f"Boxplot of {y_column} by {x_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.tick_params(rotation=45)
    ax.set_facecolor('#F2F2F2')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)
def plot_pie_chart(df, column, ax):
    data = df[column].value_counts()
    ax.pie(data, labels=data.index, startangle=450)
    ax.set_title(f"Pie Chart of {column}")
    ax.set_facecolor('#0000FF')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)
def plot_stacked_bar_chart(df, column1, column2, ax):
    data = df[[column1, column2]].groupby(column1)[column2].sum()
    data.plot(kind='bar', stacked=True, ax=ax, color=['#1a81aa', '#FF4500'], edgecolor='Black')
    ax.set_title(f"Stacked Bar Chart of {column1} and {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.tick_params(rotation=45)
    ax.set_facecolor('#e6f2ff')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)

def plot_doughnut_chart(df, column, ax):
    data = df[column].value_counts()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
    ax.set_title(f"Doughnut Chart of {column}")
    ax.set_aspect('equal')
    ax.set_facecolor('#f0f0f0')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)
    
def plot_kpi_line_chart(df, column, ax):
    df[column].plot(ax=ax, color='red', marker='o', linestyle='-')
    ax.set_title(f"KPI Line Chart: {column}")
    ax.set_xlabel("Index")
    ax.set_ylabel(column)
    ax.grid(True)
    ax.set_facecolor('#ffcce6')  # Set background color    
    #adding label size 
    ax.tick_params(labelsize=7)
    
def plot_bubble_chart(df, x_column, y_column, size_column, ax):
    sns.scatterplot(data=df, x=x_column, y=y_column, size=size_column, ax=ax)
    ax.set_title(f"Bubble Chart: {x_column} vs {y_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    #adding label size 
    ax.tick_params(labelsize=7)
    
def plot_second_stacked_bar_chart(df, column1, column2, ax):
    data = df[[column1, column2]].groupby(column1)[column2].sum()
    data.plot(kind='bar', stacked=True, ax=ax, color=['#FFD700', '#32CD32'], edgecolor='Black')
    ax.set_title(f"Second Stacked Bar Chart of {column1} and {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.tick_params(rotation=45)
    ax.set_facecolor('#f0f0f0')  # Set background color
    #adding label size 
    ax.tick_params(labelsize=7)

# Create a figure and subplots
fig, axes = plt.subplots(3, 3, figsize=(18, 10), facecolor='#ccffff')  # Default size for most plots

# adding sub title for the dashboard
plt.suptitle("Interactive Dashboard for NBA Data Analysis", fontsize=10)

# Example dashboard
while True:
    print("Dashboard Options:")
    print("1. Plot Bar Chart")
    print("2. Plot Histogram")
    print("3. Plot Boxplot")
    print("4. Plot Pie Chart")
    print("5. Plot Stacked Bar Chart")
    print("6. Plot Doughnut Chart")
    print("7. Plot KPI Chart")
    print("8. Plot Bubble Chart")
    print("9. plot second stacked Bar chart")
    print("10.Exit")
    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        column = input("Enter column name to plot bar chart: ")
        plot_bar_chart(df, column, axes[0, 0])
    elif choice == "2":
        column = input("Enter column name to plot histogram: ")
        plot_histogram(df, column, axes[0, 1])
    elif choice == "3":
        x_column = input("Enter x-axis column name: ")
        y_column = input("Enter y-axis column name: ")
        plot_boxplot(df, x_column, y_column, axes[0, 2])
    elif choice == "4":
        column = input("Enter column name to plot pie chart: ")
        plot_pie_chart(df, column, axes[1, 0])
    elif choice == "5":
        column1 = input("Enter column name for stacking (x-axis): ")
        column2 = input("Enter column name for stacking (y-axis): ")
        plot_stacked_bar_chart(df, column1, column2, axes[1, 1])
    elif choice == "6":
        column = input("Enter column name to plot doughnut chart: ")
        plot_doughnut_chart(df, column, axes[1, 2])
    elif choice == "7":
        column = input("Enter column name for KPI chart: ")
        plot_kpi_line_chart(df, column, axes [2, 0])
    elif choice == "8":
        x_column = input("Enter x-axis column name for bubble chart: ")
        y_column = input("Enter y-axis column name for bubble chart: ")
        size_column = input("Enter size column name for bubble chart: ")
        plot_bubble_chart(df, x_column, y_column, size_column, axes[2, 1])
    elif choice == "9":
        column1 = input("Enter column name for second stacking (x-axis): ")
        column2 = input("Enter column name for second stacking (y-axis): ")
        plot_second_stacked_bar_chart(df, column1, column2, axes[2, 2])
    elif choice == "10":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")


# Adjust layout and show plot
plt.tight_layout()
plt.show()
