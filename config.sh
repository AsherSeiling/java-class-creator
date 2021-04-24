pyinstaller main.py --onefile
cd dist
mv ./main .././jvclass
# Remove End of file
cd ..
rm -rf dist
rm -rf build
rm -rf __pycache__
rm -f main.spec
rm -f /usr/local/bin/jvclass
mv ./jvclass /usr/local/bin