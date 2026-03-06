from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/pipeline')
def pipeline_status():
    return jsonify({"ci_cd": "github actions working", "deployed": "vishalemmadi1234-ux"})


@app.route('/')
def home():
    return jsonify({
        "message": "Flask CI/CD Pipeline Demo - Terraform Edition",
        "status": "Deployed on AWS EC2 via GitHub Actions + Terraform",
        "version": os.getenv('APP_VERSION', '2.0.0')
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
# Trigger ci/cd pipeline test
