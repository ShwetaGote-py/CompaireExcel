# Excel File Comparison

This project provides a Python script to compare two Excel files and generate a comparison result. It also includes unit tests to ensure the functionality works as expected.

## Features

- Compare two Excel files and identify differences.
- Align DataFrames by their indexes and columns before comparison.
- Save the comparison result to a new Excel file.

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/excel-file-comparison.git
    cd excel-file-comparison
    ```

2. Install the required packages:
    ```sh
    pip install pandas
    ```

## Usage

1. Place your Excel files in the project directory.
2. Update the file names in the script if necessary.
3. Run the script:
    ```sh
    python compare_excel_files.py
    ```

The comparison result will be saved to `comparison_result.xlsx`.

## Unit Tests

Unit tests are provided to ensure the functionality works as expected.

1. Run the tests:
    ```sh
    python -m unittest discover
    ```

## Example

Here's an example of how to use the script:

```python
import pandas as pd

def compare_excel_files(file1, file2, sheet_name=0):
    # Read the Excel files
    df1 = pd.read_excel(file1, sheet_name=sheet_name)
    df2 = pd.read_excel(file2, sheet_name=sheet_name)

    # Align the DataFrames by their indexes and columns
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
