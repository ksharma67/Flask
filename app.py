import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app) 

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/api", methods=["POST"])
@cross_origin(origin=os.getenv('http://localhost:3000'))
def api():
    """Example API route."""
    data = request.json
    label = data.get("label")
    # Simulate some processing
    result = f"Processed node with label: {label}"
    return jsonify({"message": result})

@app.route("/run_flow", methods=["POST"])
@cross_origin(origin=os.getenv('http://localhost:3000'))
def run_flow():
    """Route to run all nodes in the flow one by one."""
    data = request.json
    nodes = data.get("nodes", [])
    results = []

    for node in nodes:
        label = node.get("data", {}).get("label")
        if not label:
            continue
        
        # Simulate processing for each node
        result = f"Processed node with label: {label}"
        results.append({"node_id": node.get("id"), "result": result})

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))