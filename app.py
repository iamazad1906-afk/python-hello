from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Python!</h1>
    <p>My first Python web app is running on Azure.</p>
    """

if __name__ == "__main__":
    app.run()
