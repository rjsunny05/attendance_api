from unittest.mock import patch, MagicMock
from client.postgres.attendance_logic import get_employee_attendance

@patch('client.postgres.attendance_logic.get_connection')
def test_get_employee_attendance(mock_get_conn):
    # Create fake cursor and connection
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = [123, 'Present']
    
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_get_conn.return_value = mock_conn

    # Call the function and validate the result
    result = get_employee_attendance(123)
    assert result == {'emp_id': 123, 'status': 'Present'}
