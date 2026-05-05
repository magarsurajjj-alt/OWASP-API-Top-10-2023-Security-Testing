from flask import Flask, request, jsonify

app = Flask(__name__)

# In a real API, sensitive data would be stored in a database and would only be accessible to authorized users
# However, for the purposes of this example, we will use a dictionary to store the data
sensitive_data = {
    1: {
        'name': 'John Doe',
        'ssn': '123-45-6789',
        'salary': 100000
    },
    2: {
        'name': 'Jane Smith',
        'ssn': '987-65-4321',
        'salary': 75000
    }
}

# This endpoint retrieves sensitive data based on the provided record ID
# It is vulnerable to Broken Object Level Authorization attacks because it does not properly check the user's authorization to access the data
@app.route('/data/<int:record_id>')
def get_sensitive_data(record_id):
    # Get the user ID from the request headers
    user_id = request.headers.get('user_id')
    
    # If the user ID matches the record ID, return the sensitive data
    if user_id and int(user_id) == record_id:
        return jsonify(sensitive_data[record_id])
    else:
        # If the user ID does not match the record ID, return a 403 Forbidden error
        return jsonify({'error': 'You are not authorized to access this data.'}), 403
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9873)