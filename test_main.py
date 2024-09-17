from main import *
import unittest
import sys
from io import StringIO
from datetime import datetime, timedelta

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tasks = {}
        self.exams = {
            "exam 1": "10-01-2024",
            "exam 2": "22-01-2024"
        }
        self.deadlines = {}

    def test_addAction(self):
        addAction("Task 1", "12-12-2023", self.tasks)
        self.assertIn("Task 1", self.tasks)
        self.assertEqual(self.tasks["Task 1"], "12-12-2023")
        

    def test_removeAction(self):
        addAction("Task 2", "12-12-2023", self.tasks)
        removeAction("Task 2", self.tasks)
        self.assertNotIn("Task 2", self.tasks)
    
    def test_viewAction(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # call function and give exams from setup
        viewAction(self.exams)
       
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected_output = (
            "exam 1 : 10-01-2024\n"
            "exam 2 : 22-01-2024\n"
            "\n"
            "\n"
        )

        assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
    
    # my function getValidDate is structured in a way that it 
    # always expects user input and can't use this because of test system
    #def test_getValidDate(self):
        #output = getValidDate(input_function="22-01-2024")
       #self.assertEqual(output, "22-01-2024")

    def test_nextDeadlines(self):
        today = datetime.now().date()
        deadline = today + timedelta(days=10)
        days_remaining = (deadline - today).days
        self.deadlines["Test"] = deadline.strftime('%d-%m-%Y')

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # call function to simulate deadlines
        nextDeadlines(self.deadlines)

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected_output = (
            "\n"
            "\n"
            "Deadlines/exams within the next two weeks: \n"
            f"Test: Due in {days_remaining} day(s)\n"
            "\n"
            "\n"
        )
        assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
        
if __name__ == '__main__':
    unittest.main()

