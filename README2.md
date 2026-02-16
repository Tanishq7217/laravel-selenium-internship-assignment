# Laravel + Selenium Automation Internship Assignment

## Overview

This project includes:

- Laravel login page
- Integration of HTML calendar template as `/html-page` route
- Selenium automation script to auto-fill login form

---

## Technologies Used

- Laravel
- PHP
- MySQL (if used)
- Selenium (Python)
- ChromeDriver

---

## Setup Instructions

### 1. Laravel Setup

```bash
composer install
cp .env.example .env
php artisan key:generate
php artisan serve
```

Open:
http://127.0.0.1:8000

Calendar Page:
http://127.0.0.1:8000/html-page

---

### 2. Selenium Setup

Install dependencies:

```bash
pip install selenium
```

Run:

```bash
python selenium_script.py
```

The script will:
- Open login page
- Fill random email & password
- Close browser automatically
