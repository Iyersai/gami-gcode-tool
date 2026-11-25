@echo off
rem Double-click to start the GAMI G-Code Generator in the browser.
rem Close this window (or press Ctrl+C) to stop the app.
title GAMI G-Code Generator
cd /d "%~dp0"

set "VENV_PY=%~dp0..\.venv\Scripts\python.exe"
if exist "%VENV_PY%" (
    "%VENV_PY%" -m streamlit run app.py
) else (
    python -m streamlit run app.py
)
pause
