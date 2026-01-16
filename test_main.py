import pytest
import pandas as pd
import main  # this imports your main.py functions

# Sample DataFrame to test functions
sample_data = pd.DataFrame({
    'Unnamed: 0': ['John', 'Alice'],
    'Maths':[50, 80],
    'Physics':[60, 70],
    'Chemistry':[70, 60],
    'English':[80, 90],
    'Biology':[90, 100],
    'Economics':[50, 60],
    'History':[60, 70],
    'Civics':[70, 80]
})

#  Test rename_column function
def test_rename_column():
    df = sample_data.copy()
    df = main.rename_column(df, 'Unnamed: 0', 'Name')
    assert 'Name' in df.columns
    assert 'Unnamed: 0' not in df.columns

#  Test calculate_average function
def test_calculate_average():
    df = sample_data.copy()
    df = main.rename_column(df, 'Unnamed: 0', 'Name')
    marks_cols = ['Maths','Physics','Chemistry','English','Biology','Economics','History','Civics']
    avg_df = main.calculate_average(df, marks_cols)
    
    # Check columns
    assert 'Average' in avg_df.columns
    assert 'Name' in avg_df.columns
    
    # Check average values
    assert round(avg_df.loc[0,'Average'],2) == 65.0
    assert round(avg_df.loc[1,'Average'],2) == 76.25

#  Test save_csv function
def test_save_csv(tmp_path):
    df = pd.DataFrame({'Name':['John'], 'Average':[65.0]})
    file_path = tmp_path / "avg.csv"
    saved_file = main.save_csv(df, file_path)
    
    # Check returned file path
    assert saved_file == file_path
    
    # Check file content
    df2 = pd.read_csv(saved_file)
    assert list(df2['Name']) == ['John']
    assert round(df2['Average'][0],2) == 65.0
