import pandas as pd

def compare_excel_files(file1, file2, sheet_name=0):
    # Read the Excel files
    df1 = pd.read_excel(file1, sheet_name=sheet_name)
    df2 = pd.read_excel(file2, sheet_name=sheet_name)
    #df1 = pd.read_csv(file1)
    #df2 = pd.read_csv(file2)

    df1, df2 = df1.align(df2, join='outer', axis=0, fill_value=None)
    df1, df2 = df1.align(df2, join='outer', axis=1, fill_value=None)

    # Compare the two DataFrames
    comparison_result = df1.compare(df2)

    return comparison_result

def save_comparison_result(result, output_file):
    with pd.ExcelWriter(output_file) as writer:
        result.to_excel(writer, sheet_name='Comparison Result')

if __name__ == "__main__":
    file1 = 'File1.xlsx'
    file2 = 'File2.xlsx'
    output_file = 'comparison_result.xlsx'

    result = compare_excel_files(file1, file2)
    save_comparison_result(result, output_file)
    print(f'Comparison result saved to {output_file}')