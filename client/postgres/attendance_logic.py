from client.postgres.postgres_conn import get_connection

def get_employee_attendance(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance WHERE emp_id = %s", (emp_id,))
    row = cursor.fetchone()
    return {'emp_id': row[0], 'status': row[1]}
