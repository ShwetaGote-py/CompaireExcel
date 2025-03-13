import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from compare_excel_files import compare_excel_files, save_comparison_result

class TestCompareExcelFiles(unittest.TestCase):

    def setUp(self):
        # Create sample data for testing
        self.df1 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        self.df2 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 7]
        })
        self.df3 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })

        # Save the sample data to Excel files
        self.file1 = 'test_file1.xlsx'
        self.file2 = 'test_file2.xlsx'
        self.file3 = 'test_file3.xlsx'
        self.df1.to_excel(self.file1, index=False)
        self.df2.to_excel(self.file2, index=False)
        self.df3.to_excel(self.file3, index=False)

    def test_compare_excel_files_different(self):
        # Compare two different files
        result = compare_excel_files(self.file1, self.file2)
        expected_result = pd.DataFrame({
            'B': {'self': 6, 'other': 7}
        }, index=[2])
        assert_frame_equal(result, expected_result)

    def test_compare_excel_files_identical(self):
        # Compare two identical files
        result = compare_excel_files(self.file1, self.file3)
        expected_result = pd.DataFrame()
        assert_frame_equal(result, expected_result)

    def tearDown(self):
        # Clean up the created files
        import os
        os.remove(self.file1)
        os.remove(self.file2)
        os.remove(self.file3)

if __name__ == '__main__':
    unittest.main()