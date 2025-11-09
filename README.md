# 🤖 nopCommerce Test Automation

A Python-based Selenium automation project for the nopCommerce demo e-commerce site.  

It simulates both admin and customer workflows to verify that key features of the website work as expected.  

Built as a first hands-on venture into Selenium WebDriver and Pytest, this project was created to practice automated web testing, reinforce the Page Object Model design, and explore continuous integration basics.  

**_Human-made alert: every line of code was written by a carbon-based lifeform. Zero AI codegen. I only let an AI help punch up this README, because writing docs is not exactly my weekend hobby._**  

---

## 🧠 Concepts Practiced

### Python
- Page Object Model with clean page classes and reusable locators; modular methods for actions and asserts
- Externalized configuration via INI for URLs and credentials, read through a small helper layer
- Structured logging and simple failure artifacts for fast triage
- Lightweight data utilities for randomized inputs to diversify test runs
### Selenium
- Cross-browser WebDriver setup with explicit waits and resilient selectors
- Robust flows for admin and storefront journeys: login, add customer, wishlist, and grid search with table traversal
- Form handling at scale: dropdowns, role assignment, toggles, and validation checks
### Pytest
- Fixtures and CLI-driven environment selection for scalable runs
- Parametrization for fan-out execution and basic load simulation; smoke markers for quick feedback loops
- Data-driven testing from Excel with pass/fail aggregation
- Metadata customization to enrich reports and CI logs
### Jenkins _(exploratory)_
- Simple CI trigger that executes a batch runner on push for smoke coverage and fast feedback

---

## ⚙️ Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/kravvat/nopcommerce-automation.git
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Update `config.ini` (optional):  
Config file is pre-filled with the nopCommerce demo site URL and default admin credentials (provided by the demo). You can adjust these values if you want to run tests against a different environment or user.

4. Run the tests:
    ```bash
    ./run.bat
---

## 📍 Status

✅ Completed learning project – This project has met its objectives as a practice suite for web automation.  
It is considered finished and stable in its current form, demonstrating fundamental skills in Selenium-based testing.  

---

## 📚 License

This project is open for educational use. Attribution appreciated if reused. 

---

## 🔗 Connect with me

- ⚔️ Boot.dev: [kravvat](https://www.boot.dev/u/kravvat)  
- 💼 LinkedIn: [Kacper Stec](https://www.linkedin.com/in/kacper-stec/)  
- 📫 Email: kacperstec3d@gmail.com  

---

Thanks for visiting!  
Have a great day and happy coding!
