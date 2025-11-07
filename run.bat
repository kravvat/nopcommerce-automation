@echo off
call .venv\Scripts\activate
echo Starting Test Suit...
pytest -s -v -n auto -m "beta" --html .\reports\test_report.html --browser firefox
echo Test Suit completed 
