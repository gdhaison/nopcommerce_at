# NopCommerce Playwright Test Automation

This project provides a **from-scratch Playwright test framework** to automate core user journeys on [nopCommerce demo site](https://demo.nopcommerce.com).

It supports running locally (with virtual environment) and inside Docker (CI/CD friendly).
The framework follows **Page Object Model (POM)**, generates HTML reports, captures artifacts (screenshot, video, trace), and is production-ready.

---

## 📦 Prerequisites

* **Option 1: Local environment**

  * Python 3.10+ (recommended via [Homebrew](https://brew.sh) on Mac)
  * Node.js (only if you want to use Playwright CLI directly)
  * Git

* **Option 2: Docker environment**

  * [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

---

## 🚀 Setup & Run (Local)

### 1. Clone repository

```bash
git clone https://github.com/<your-username>/nopcommerce_at.git
cd nopcommerce_at
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows (PowerShell)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run tests

```bash
pytest --headed   # run with browser UI
pytest            # run headless
```

### 5. View reports

After run, open:

```
reports/index.html
```

---

## 🐳 Setup & Run (Docker)

### 1. Build image

```bash
docker build -t nopcommerce-tests .
```

### 2. Run tests (headless)

```bash
docker run --rm -e DOCKER_ENV=true -v $(pwd):/app -v $(pwd)/reports:/app/reports nopcommerce-tests
```
---

## 📋 Test Coverage (mandatory flows)

* Register new account
* Forgot password workflow
* Request password reset (verify reset link from email)
* Search product
* Explore product by category (Computers → Notebooks)
* Sort products by Price
* Filter by Manufacturer
* Filter by Price

Additional tests have been added to increase coverage.

---

## 🛠 Features

* Page Object Model (POM)
* HTML reporting
* Screenshot, video, and trace capture on failure
* Configurable test environments
* Ready for CI/CD pipelines
* Optional Docker + VNC support

---

## 📹 Demo

* Sample run video: `demo.mp4`
* Sample report: `reports/index.html`

---

## ⚡ CI/CD

Example GitHub Actions workflow included: `.github/workflows/ci.yml`

Run tests automatically on each push or pull request.

---

## 📌 Notes

* For debugging locally, run with `--headed` (browser visible).
* In Docker, prefer headless for CI, or use the provided `docker-compose.yml` with VNC to watch UI.
