import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import unittest
from main import calculate_benefits
import pandas as pd

class TestPensionEngine(unittest.TestCase):

    def test_high_experience_pension(self):
        # Case: 25 years service, 60,000 salary
        # Expected Pension: (60000 * 25) / 70 = 21428.57
        mock_data = pd.Series({'Salary': 60000, 'Years': 25})
        result = calculate_benefits(mock_data)
        self.assertEqual(result[0], 21428.57)

    def test_low_experience_no_pension(self):
        # Case: 8 years service (Below the 10-year limit)
        # Expected Pension: 0
        mock_data = pd.Series({'Salary': 45000, 'Years': 8})
        result = calculate_benefits(mock_data)
        self.assertEqual(result[0], 0)

    def test_gratuity_threshold(self):
        # Case: 4 years service (Below the 5-year limit for gratuity)
        # Expected Gratuity: 0
        mock_data = pd.Series({'Salary': 50000, 'Years': 4})
        result = calculate_benefits(mock_data)
        self.assertEqual(result[1], 0)

if __name__ == '__main__':
    unittest.main()