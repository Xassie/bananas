@echo off
color 0A

move "Folder 1"\This1file.txt "Folder 2"\

del "'bout to commit massacre"\*.jpg /f /q

xcopy "Folder 1"\*.jpg "'bout to commit massacre"\ /s /y

start "" "https://stackoverflow.com/"
Timeout /t 1
start "" "https://i.imgur.com/8NIxBDF.gif"
Timeout /t 1
start "" "https://myanimelist.net/profile/Xassie"

echo. > res.txt
for %%i in (.\"Folder 1"\*) do (
	echo %%~nxi >> res.txt
)

cls
echo Wake up, Neo...
echo The Matrix has you...
echo.
timeout /t 5