cd ..
cd modules && pyinstaller -w host.py -i "../icons/botIcon.ico" --hidden-import inputData
cd dist
move host ..\
cd ..
move host ..\compiled\
rmdir dist /s /q
rmdir build /s /q
del "host.spec"
cd ..
