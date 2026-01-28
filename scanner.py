import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def scan_sql_injection(url):
    print("🔍 Checking for SQL Injection...")
    payloads = ["' OR '1'='1", "' OR 1=1--", "' OR '1'='1' --"]
    for payload in payloads:
        try:
            full_url = f"{url}?id={payload}"
            res = requests.get(full_url)
            if "sql" in res.text.lower() or "error" in res.text.lower():
                print("⚠️ Potential SQL Injection vulnerability detected!")
                return True
        except:
            continue
    print("✅ No SQL Injection vulnerability found.")
    return False

def scan_xss(url):
    print("🔍 Checking for Cross-Site Scripting (XSS)...")
    xss_payload = "<script>alert('XSS')</script>"
    full_url = f"{url}?input={xss_payload}"
    try:
        res = requests.get(full_url)
        if xss_payload in res.text:
            print("⚠️ Potential XSS vulnerability detected!")
            return True
    except:
        pass
    print("✅ No XSS vulnerability found.")
    return False

def scan_outdated_libs(url):
    print("🔍 Checking for Outdated JavaScript Libraries...")
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        scripts = soup.find_all("script", src=True)
        old_libs = []
        for script in scripts:
            src = script['src']
            if "jquery-1." in src or "bootstrap-3." in src:
                old_libs.append(src)

        if old_libs:
            print(f"⚠️ Outdated libraries found: {old_libs}")
        else:
            print("✅ No outdated libraries found.")
        return old_libs
    except:
        print("⚠️ Failed to check for outdated libraries.")
        return []

def scan_site(url):
    print("="*50)
    print(f"🔎 Starting scan for: {url}")
    print("="*50)

    results = {}

    results['SQL Injection'] = scan_sql_injection(url)
    results['XSS'] = scan_xss(url)
    results['Outdated Libraries'] = scan_outdated_libs(url)

    print("\n✅ Scan completed. Summary:")
    print("-" * 50)
    for k, v in results.items():
        print(f"{k}: {v}")
    print("-" * 50)
    return results

if __name__ == "__main__":
    site = input("Enter the site URL (e.g., http://example.com/page): ")
    results = scan_site(site)

    from report_generator import generate_html_report
    generate_html_report(results, site)

