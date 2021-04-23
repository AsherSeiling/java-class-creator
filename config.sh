pyinstaller main.py --onefile
cd dist


# Remove End of file
cd ..
rm -rf dist
rm -rf build
rm -rf __pycache__
rm -f main.spec