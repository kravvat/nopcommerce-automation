@echo off
call .venv\Scripts\activate
echo Starting Test Suit...
pytest -s -v -m "sanity" --html .\reports\test_report.html --browser firefox
pause
echo Test Suit completed 
