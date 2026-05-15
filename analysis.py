import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Analysis
total_records = len(df)
survival_rate = df["Survived"].mean() * 100
average_age = df["Age"].mean()
class_distribution = df["Pclass"].value_counts()

# Print outputs
print("Total Records:", total_records)
print("Survival Rate: {:.2f}%".format(survival_rate))
print("Average Age: {:.2f}".format(average_age))

print("\nClass-wise Distribution:")
print(class_distribution)

# Save outputs
with open("output.txt", "w") as f:
    f.write(f"Total Records: {total_records}\n")
    f.write(f"Survival Rate: {survival_rate:.2f}%\n")
    f.write(f"Average Age: {average_age:.2f}\n\n")
    f.write("Class-wise Distribution:\n")
    f.write(str(class_distribution))