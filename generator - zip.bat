for /f "tokens=* delims=" %%i in ('dir /s /b /a:d *.git') do (
rd /s /q "%%i"
)

for /f "tokens=* delims=" %%i in ('dir /s /b /a:d *.idea') do (
rd /s /q "%%i"
)

del /s *.zip
python addons_zip_generator.py