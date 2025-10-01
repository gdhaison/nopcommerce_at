# NopCommerce Playwright Test Automation

Demo video is stored in this link: https://drive.google.com/file/d/11KzjHFMxElKx4y8rgMn4DkvLaZRiwEI3/view?usp=sharing

This project provides a **from-scratch Playwright test framework** to automate core user journeys on [nopCommerce demo site](https://demo.nopcommerce.com).

- **Supports:** Local & Docker execution
- **Design:** Page Object Model (POM)
- **Artifacts:** HTML reports, screenshots, videos, traces, logs
- **Ready for:** CI/CD, production use

---

## 📦 Prerequisites

### Local Environment
- Python 3.10+ (recommended via [Homebrew](https://brew.sh) on Mac)
- Node.js (only if you want to use Playwright CLI directly)
- Git

### Docker Environment
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

---

## 🚀 Setup & Run (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/nopcommerce_at.git
cd nopcommerce_at
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows (PowerShell)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4. Run Tests

You can run tests on different browsers by specifying the browser with the `-D browser` option. For example:

- To run tests on **Firefox**:
  ```bash
  behave -D browser=firefox -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/report.html
  ```
- To run tests on **Chromium**:
  ```bash
  behave -D browser=chromium -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/report.html
  ```

#### Run All Tests
```bash
behave -D browser=firefox -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/report.html
```

#### Run Tests by Tag
```bash
behave -D browser=firefox -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/report.html -t @flaky
```

#### Run Tests in Parallel
```bash
behavex run --parallel-processes 4 --parallel-scheme scenario --formatter behave_html_formatter:HTMLFormatter --formatter-outdir reports
```

---

## 🐳 Setup & Run (Docker)

### 1. Build Docker Image
```bash
docker build -t nopcommerce-tests .
```

### 2. Run Tests (Headless)
```bash
docker run --rm -e DOCKER_ENV=true -v $(pwd):/app -v $(pwd)/reports:/app/reports nopcommerce-tests
```

---

## 📊 View Reports

After running tests, open the HTML report:
```bash
open reports/report.html
```

---

## 🗂️ Artifacts: Traces, Screenshots, and Logs

After each test run, the framework automatically captures useful artifacts for debugging:

- **Screenshots:** Captured on test failure and saved in the `reports/` directory (e.g., `reports/screenshot_*.png`).
- **Logs:** Test execution logs are stored in the `reports/logs/` directory.
- **Videos:** (If enabled) Saved in the `reports/` directory.

> These artifacts help you quickly diagnose test failures by providing visual and step-by-step context.

---

## 📋 Test Coverage

- Register new account
- Forgot password workflow
- Request password reset (verify reset link from email)
- Search product
- Explore product by category (Computers → Notebooks)
- Sort products by Price
- Filter by Manufacturer
- Filter by Price

_Additional tests have been added to increase coverage._

---

## 🛠 Features

- Page Object Model (POM)
- HTML reporting
- Screenshot, video, and trace capture on failure
- Configurable test environments
- Ready for CI/CD pipelines
- Optional Docker + VNC support

---

## ⚡ CI/CD

Example GitHub Actions workflow included: `.github/workflows/ci.yml`

Tests run automatically on each push or pull request.

---

## 📁 Project Structure

```
behave.ini                # Behave configuration
config.yaml               # Project configuration
Dockerfile                # Docker build file
docker-compose.yml        # Docker Compose setup
pytest.ini                # Pytest configuration
README.md                 # Project documentation
requirements.txt          # Python dependencies

features/                 # Gherkin feature files and step definitions
  environment.py          # Behave environment hooks
  explore_product.feature # Feature: Explore product
  forgot_password.feature # Feature: Forgot password
  register.feature        # Feature: Register
  search_product.feature  # Feature: Search product
  steps/                  # Step definition Python files

output/                   # Output and temporary files
  failing_scenarios.txt   # List of failing scenarios
  overall_status.json     # Overall test status
  report.json             # Test report in JSON
  behave/                 # Behave outputs
  outputs/                # Additional outputs
  reports/                # Additional reports
  temp/                   # Temporary files

reports/                  # HTML reports and screenshots
  register.html           # Register feature report
  report.html             # Main test report
  screenshot_*.png        # Screenshots captured on failure

 tests/                   # Test utilities and page objects
  pages/                  # Page Object Model classes
  utils/                  # Utility modules

```

---
