@echo off
echo ========================================
echo Dashboard de Sustentabilidade
echo ========================================
echo.
echo Ativando ambiente virtual...
call printer_config_env\Scripts\activate.bat
echo.
echo Verificando dependencias...
python -c "import streamlit, plotly, pandas; print('Dependencias OK')"
echo.
echo Iniciando dashboard...
echo.
echo O dashboard sera aberto em: http://localhost:8501
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
streamlit run streamlit_dashboard.py
pause




