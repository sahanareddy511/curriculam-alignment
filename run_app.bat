@echo off
cd /d "%~dp0"
echo ======    ======================================
echo      SKILL-TWIN ENGINE - STARTUP SCRIPT
echo ============================================
echo.

echo [1/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies. Please check your python installation.
    pause
    exit /b
)

echo.
echo [2/3] Downloading spaCy English model...
python -m spacy download en_core_web_sm
if %errorlevel% neq 0 (
    echo Error downloading spaCy model.
    pause
    exit /b
)

echo.
echo [3/3] Starting Flask Application...
echo.
echo Open your browser to: http://127.0.0.1:5000
echo.
python app.py
pause