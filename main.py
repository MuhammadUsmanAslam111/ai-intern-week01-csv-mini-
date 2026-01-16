import pandas as pd

def read_csv(file_path):
   return pd.read_csv(file_path)

def rename_column(df, old_name, new_name):
    df.rename(columns={old_name: new_name}, inplace=True)
    return df

def calculate_average(df, marks_cols):
    df['Average'] = df[marks_cols].mean(axis=1)
    return df[['Name', 'Average']]

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == "__main__":

    data = read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ai‑intern‑week01‑csv‑mini\student_marks.csv")
    print(data.head())
    # Rename 'Unnamed: 0' to 'Name'
    data = rename_column(data, 'Unnamed: 0', 'Name')
    # Columns for marks
    marks_cols = ['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
    # Calculate average
    avg_data = calculate_average(data, marks_cols)
    # Save to CSV
    output_file = save_csv(avg_data, "student_avg.csv")
    print(f"Average marks saved to {output_file}")
    # Read back to confirm
    data1 = read_csv(output_file)
    print(data1.head())
    