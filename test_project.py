import pytest
import io
import sys
import tempfile
import os
import csv
from unittest.mock import patch, Mock
from project import search_book,check_read_books,recommend_book


# We need to mimic the behaviour of the API

def test_search_book():
    with patch('builtins.input', side_effect=['title', 'author']):

        with patch('requests.get') as mock_get:
            mock_response = Mock()
            expected_data = {
                'docs': [
                    {
                        'author_name': ['Test Author'],
                        'title': 'Test Title',
                        'first_publish_year': 2020
                    }
                ]
            }
            mock_response.status_code = 200
            mock_response.json.return_value = expected_data
            mock_get.return_value = mock_response
            # Mock pentru inquirer.list_input
            with patch('inquirer.list_input', side_effect=['No, exit the program']):
                captured_output = io.StringIO()
                sys.stdout = captured_output
                search_book()
                sys.stdout = sys.__stdout__
                output = captured_output.getvalue()

                assert "Author: Test Author, Title: Test Title, First Publish Year: 2020" in output
                mock_get.assert_called_once_with('https://openlibrary.org/search.json?title=title&author=author')




def test_check_read_books():
    test_data = "Title,Author's Name,Publish Year"


    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        csv_file_path = temp_csv.name
        temp_csv.write(test_data)

    captured_output = io.StringIO()
    with patch('sys.stdout', new=captured_output):
        check_read_books(csv_file=csv_file_path)

    output = captured_output.getvalue()


    assert "Title" in output
    assert "Author's Name" in output
    assert "Publish Year" in output
    assert "File is empty" not in output


    os.remove(csv_file_path)


def test_check_want_read_books():

    test_data_want_to_read = "Title,Author's Name,Publish Year"


    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        csv_file_path = temp_csv.name
        temp_csv.write(test_data_want_to_read)

    captured_output = io.StringIO()
    with patch('sys.stdout', new=captured_output):
        check_read_books(csv_file=csv_file_path)

    output = captured_output.getvalue()


    assert "Title" in output
    assert "Author's Name" in output
    assert "Publish Year" in output
    assert "File is empty" not in output


    os.remove(csv_file_path)


def test_recommend_book():

    test_data = """Title, Author's Name, Publish Year
Test Title 1,Test Author 1,2020
Test Title 2,Test Author 2,2021
Test Title 3,Test Author 3,2022"""


    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_csv:
        csv_file_path = temp_csv.name
        temp_csv.write(test_data)

    captured_output = io.StringIO()
    with patch('sys.stdout', new=captured_output):
        with patch('random.choices', return_value=[["Test Title 2", "Test Author 2", "2021"]]):
            recommend_book(csv_file=csv_file_path)

    output = captured_output.getvalue()
    print(f"Captured output: {output}")


    assert "Test Title 2" in output
    assert "Test Author 2" in output
    assert "2021" in output
    assert "Cannot give recommendation" not in output


    os.remove(csv_file_path)



if __name__ == "__main__":
    pytest.main()



