from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure Cloud Project</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f8fc;
            color: #222;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 55px 30px;
        }

        .header {
            text-align: center;
            margin-bottom: 45px;
        }

        .header h1 {
            margin: 0;
            font-size: 42px;
            color: #0879c9;
        }

        .header p {
            margin-top: 12px;
            font-size: 21px;
            color: #444;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
        }

        .card {
            background: white;
            border-radius: 14px;
            padding: 45px 20px;
            text-align: center;
            box-shadow: 0 5px 18px rgba(0,0,0,0.12);
            min-height: 190px;
        }

        .icon {
            font-size: 35px;
            margin-bottom: 12px;
        }

        .card h2 {
            margin: 0 0 18px;
            color: #0879c9;
            font-size: 25px;
        }

        .card p {
            margin: 0;
            font-size: 17px;
            line-height: 1.5;
        }

        .success {
            text-align: center;
            margin-top: 45px;
            font-size: 20px;
            font-weight: bold;
            color: #178a2d;
        }

        @media (max-width: 900px) {
            .cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 600px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .header h1 {
                font-size: 32px;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <div class="header">
            <h1>☁️ Azure Cloud Project</h1>
            <p>Python Web Application deployed on Microsoft Azure</p>
        </div>

        <div class="cards">

            <div class="card">
                <div class="icon">🌐</div>
                <h2>Web App</h2>
                <p>Python application hosted on Azure</p>
            </div>

            <div class="card">
                <div class="icon">💻</div>
                <h2>Virtual Machine</h2>
                <p>Windows VM configured in Azure</p>
            </div>

            <div class="card">
                <div class="icon">🗄️</div>
                <h2>Storage</h2>
                <p>Azure Storage Account</p>
            </div>

            <div class="card">
                <div class="icon">🔐</div>
                <h2>Private Endpoint</h2>
                <p>Private connection to Storage</p>
            </div>

        </div>

        <div class="success">
            ✅ Deployment Successful
        </div>

    </div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
