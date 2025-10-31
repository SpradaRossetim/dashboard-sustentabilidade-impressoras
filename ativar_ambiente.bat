@echo off
echo Ativando ambiente virtual para scanner de impressora...
call printer_config_env\Scripts\activate.bat
echo Ambiente ativado! Agora você pode executar os scripts:
echo.
echo Para scan basico:
echo python printer_config.py
echo.
echo Para scan avancado:
echo python printer_advanced.py
echo.
cmd /k




