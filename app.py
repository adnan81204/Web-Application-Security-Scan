from flask import Flask, render_template, request
from scanner import scan_site
from report_generator import generate_html_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        results = scan_site(url)
        generate_html_report(results, url)
        return render_template("report.html")

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Web Security Scanner</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f0f2f5;
                font-family: 'Segoe UI', sans-serif;
            }
            .scanner-box {
                max-width: 600px;
                margin: 100px auto;
                padding: 30px;
                background: white;
                border-radius: 12px;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
                color: #0d6efd;
            }
            footer {
                text-align: center;
                font-size: 14px;
                margin-top: 20px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="scanner-box">
            <h2>🛡️ Web Application Security Scanner</h2>
            <form method="post">
                <div class="mb-3">
                    <label for="url" class="form-label">Enter the URL to scan:</label>
                    <input type="text" name="url" class="form-control" id="url" placeholder="e.g., http://testphp.vulnweb.com" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">🚀 Start Scan</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)

