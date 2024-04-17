from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestConsoleCommands(unittest.TestCase):
    def test_do_create_user(self):
        """Test do_create method with User class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create User name=\"anas\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  

        
    def test_do_create_place(self):
        """Test do_create method with Place class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create Place city_id=\"123\" user_id=\"456\" name=\"my_place\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  

    def test_do_create_state(self):
        """Test do_create method with State class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create State name=\"California\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  

    def test_do_create_city(self):
        """Test do_create method with City class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create City state_id=\"789\" name=\"San Francisco\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  

    def test_do_create_amenity(self):
        """Test do_create method with Amenity class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create Amenity name=\"WiFi\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  

    def test_do_create_review(self):
        """Test do_create method with Review class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create Review place_id=\"111\" user_id=\"222\" text=\"Great place!\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  
    
    def test_do_all_no_args(self):
        """Test do_all method without arguments"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()

    def test_do_all_with_args(self):
        """Test do_all method with arguments"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all User")
            output = mock_stdout.getvalue().strip()

if __name__ == '__main__':
    unittest.main()
