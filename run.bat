@echo off
call .venv\Scripts\activate
echo Starting Test Suit...
pytest -s -v -m "smoke" --html .\reports\test_report.html --browser firefox
echo Test Suit completed 
pause
