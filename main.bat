@echo off
setlocal EnableDelayedExpansion

:menu
cls
echo Select a Python script to run:
echo.

set i=1
for %%f in (*.py) do (
    echo !i! - %%f
    set "scripts_list[!i!]=%%f"
    set /a i+=1
)

echo 0 - Exit
echo.

set /p choice="Enter the number of the script you want to run: "
echo.

if %choice% == 0 (
    echo Exiting...
    goto :eof
)

set script_to_run=!scripts_list[%choice%]!

if not defined script_to_run (
    echo Invalid choice. Please try again.
    pause
    goto :menu
)

echo Running %script_to_run%
echo.
python %script_to_run%
echo.
pause
goto :menu
