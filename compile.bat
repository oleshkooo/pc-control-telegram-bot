cd modules
pyinstaller -F host.py -i ../misc/icon.ico --hidden-import inputData
rmdir build /s /q
cd dist
move host.exe ../
cd ..
rmdir dist /s /q
del host.spec
host.exe