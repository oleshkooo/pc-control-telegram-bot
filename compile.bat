cd modules
pyinstaller -F host.py --hidden-import inputData
rmdir build /s /q
cd dist
move host.exe ../
cd ..
rmdir dist /s /q
del host.spec
host.exe