cd ..
pyinstaller -w -F "PC Control Bot.py" -i "icons\botIcon.ico"
cd dist
move "PC Control Bot.exe" ../compiled/
cd ..
rmdir dist /s /q
rmdir build /s /q
del "PC Control Bot.spec"