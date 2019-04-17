#test file

echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/catrik3604/test.git
git push -u origin master