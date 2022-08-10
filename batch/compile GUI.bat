cd ..
cd GUI && pyinstaller -w GUI.py -i "..\icons\botIcon.ico"
cd dist
move GUI ..\
cd ..
move GUI ..\compiled\
rmdir dist /s /q
rmdir build /s /q
del "GUI.spec"
cd ..
