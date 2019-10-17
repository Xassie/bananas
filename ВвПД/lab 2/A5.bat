@echo off
echo. > res.txt
for %%i in (.\"Folder 1"\*) do (
	echo %%~nxi >> res.txt
)