python3 -m pip install --upgrade pip
pip install wheel
python setup.py bdist_wheel sdist
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
pip install  --force-reinstall ./dist/my_minipack-1.0.0-py3-none-any.whl