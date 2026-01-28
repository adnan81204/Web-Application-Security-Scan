#  Web Application Security Scanner

A lightweight **Web Application Security Scanner** built using **Python and Flask** that scans a target URL for common web vulnerabilities such as **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Outdated JavaScript Libraries**, and generates a **detailed HTML and PDF security report**.

---

## Features

- SQL Injection detection using common payloads  
- Cross-Site Scripting (XSS) detection  
- Detection of outdated JavaScript libraries (jQuery, Bootstrap)  
- Automatic HTML report generation  
- PDF report generation using `wkhtmltopdf`  
- Simple and clean web interface using Bootstrap  

---

## Technologies Used

- Python 3
- Flask
- Requests
- BeautifulSoup4
- pdfkit
- Bootstrap 5

---

## How It Works

1. User enters a target URL in the web interface  
2. The scanner checks for:
   - SQL Injection vulnerabilities  
   - Cross-Site Scripting (XSS)  
   - Outdated JavaScript libraries  
3. Scan results are analyzed  
4. A detailed HTML report is generated  
5. The report is converted into a PDF file  

---

## Installation & Setup

### Step 1: Clone the Repository
git clone https://github.com/adnan81204/Web-Application-Security-Scan
cd Web-Application-Security-Scan

### Step 2: Install Dependencies
pip install -r requirements.txt

### Step 3: Install wkhtmltopdf (Required for PDF)
**Windows**
Download from: https://wkhtmltopdf.org/downloads.html
Install to:
C:\tools\wkhtmltopdf\bin\wkhtmltopdf.exe

**Linux**
sudo apt install wkhtmltopdf

### Step 4: Run the Application
python app.py
Open your browser and visit:
http://127.0.0.1:5000
---
## Output
templates/report.html → Detailed scan report
report_pdf/report.pdf → Downloadable PDF security report

## Disclaimer

This tool is strictly for educational and ethical testing purposes only.
Scan only websites you own or have explicit permission to test.
Unauthorized scanning may be illegal.

# Future Enhancements

-CSRF vulnerability detection

-Directory traversal scanning

-Authentication testing

-OWASP Top 10 coverage

-Report download from UI

## Author

Shaik Adnan Tousef

## License

This project is licensed under the MIT License.

### Happy Ethical Hacking!



