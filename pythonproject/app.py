from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

locations = []  # To store submitted locations temporarily

@app.route('/')
def consent():
    return render_template('consent.html')

@app.route('/dashboard')
def dashboard():
    # Pass locations with names to dashboard
    return render_template('dashboard.html', locations=locations)

@app.route('/submit-location', methods=['POST'])
def submit_location():
    data = request.get_json()
    if data and "lat" in data and "lng" in data:
        locations.append({
            "name": data.get("name", "Anonymous"),
            "lat": data["lat"],
            "lng": data["lng"]
        })
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
