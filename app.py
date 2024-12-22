from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route for testing
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask REST API!"}), 200

# Sample GET route
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Test Item",
        "description": "This is a test item for the API.",
    }
    return jsonify(sample_data), 200

# Sample POST route
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data}), 201

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Run the application on all available IPs (0.0.0.0) to make it accessible externally
    app.run(host='0.0.0.0', port=5000)
