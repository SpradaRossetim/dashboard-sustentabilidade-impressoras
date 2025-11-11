@echo off
echo ========================================
echo Limpando Cache do Streamlit
echo ========================================
echo.

echo Parando processos do Streamlit...
taskkill /F /IM streamlit.exe 2>nul
timeout /t 2 /nobreak >nul

echo.
echo Limpando cache...
rd /s /q .streamlit\cache 2>nul
rd /s /q __pycache__ 2>nul

echo.
echo Cache limpo!
echo.
echo Agora execute: iniciar_dashboard.bat
echo.
pause



