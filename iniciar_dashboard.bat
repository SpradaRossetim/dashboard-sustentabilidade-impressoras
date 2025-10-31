@echo off
echo ========================================
echo Dashboard de Sustentabilidade
echo ========================================
echo.
echo Ativando ambiente virtual...
call printer_config_env\Scripts\activate.bat
echo.
echo Iniciando dashboard web...
echo.
echo O dashboard sera aberto em: http://localhost:8501
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
streamlit run streamlit_dashboard.py
pause





