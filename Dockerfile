# Base image Python
FROM python:3.13-slim

# Cài Playwright + trình duyệt
RUN pip install --upgrade pip \
    && pip install playwright behave behave-html-formatter pyyaml \
    && playwright install --with-deps

# Copy project
WORKDIR /app
COPY . /app

# Tạo thư mục chứa report
RUN mkdir -p reports

# Default command khi chạy container
CMD ["behave", "-f", "behave_html_formatter:HTMLFormatter", "-o", "reports/report.html"]
