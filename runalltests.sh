echo '================================================================================================================='
cd pagegroups/todo/tst
python3 -m unittest discover -f
cd ../../..
cd Library/tst
python3 -m unittest discover -f
cd ../..
cd tst
python3 -m unittest discover -f
cd ..
