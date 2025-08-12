from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# store locations in memory (for now)
locations = []

@app.route('/')
def consent_page():
    return render_template('consent.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', locations=locations)

@app.route('/submit-location', methods=['POST'])
def submit_location():
    data = request.get_json()
    locations.append(data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
