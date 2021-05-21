from flask import Flask, jsonify

# Import app code
app = Flask(__name__)

# After creating the app, so that cors can import it

@app.route("/")
def root():
    return "server 1"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
