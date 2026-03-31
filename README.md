# 🐍 Python API Automation Suite

This repository contains a robust automated testing suite designed to validate REST endpoints, developed with **Python** and **Pytest**. It features professional-grade reporting and advanced HTTP session management.

## 🛠️ Tech Stack
- **Language:** Python 3.14.3
- **Testing Framework:** Pytest
- **HTTP Library:** Requests (implemented with Session and Custom Headers management)
- **Reporting:** **Allure Reports** (Interactive Dashboard) & Pytest-html
- **CI/CD:** Integrated with GitHub Actions

## 🎯 Test Scenarios
1. **GET Users:** Validation of 200 OK status and data integrity.
2. **POST Create User:** Verification of successful resource creation (201 Created).
3. **Negative Testing (404):** Error handling validation for non-existent users.
4. **Functional POST:** Simulation of content creation (Posts) with schema validation.
5. **Security/Invalid Route:** Verification of system behavior against undefined endpoints.

## 🔧 Engineering Notes (Troubleshooting & Architecture)
To ensure test stability against network protections (WAF/Cloudflare), I implemented an architecture based on `requests.Session()`. This includes custom `User-Agent` configurations to emulate real browser behavior, preventing 403/401 errors during automated execution.

The suite is now integrated with **Allure Framework**, providing a high-level executive dashboard to analyze test trends, execution times, and root cause analysis of failures.

## 📊 View Live Report
You can view the interactive execution report here:
👉 **[Link to your Allure Report on your Portfolio]**

## 🚀 Execution & Reporting
1. **Activate Environment:** `.\venv\Scripts\activate`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run Tests & Generate Data:**
   ```bash
   python -m pytest --alluredir=allure-results