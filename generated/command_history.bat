rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script.
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/errors.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/ctypes_library.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/mock_helper.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/__init__.py.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/session.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/enums.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/attributes.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
python3 -m build --template  /c/Users/Administrator/Desktop/Git/nimi-python/build/templates/functions.rst.mako --dest-dir  /c/Users/Administrator/Desktop/Git/nimi-python/docs/nifake/ --metadata  /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/metadata 
cp /c/Users/Administrator/Desktop/Git/nimi-python/src/nifake/tests/test_session.py /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/tests/test_session.py
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
rm  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
 rm -Rf /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake/* && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/nifake/* /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake && cp -Rf /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/setup.py /c/Users/Administrator/Desktop/Git/nimi-python/generated/nifake 
touch  /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/generated_files_copy_done
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py bdist_wheel --universal > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/wheel_build_done
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
rm /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
cd /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake && python3 setup.py sdist > /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist.log
touch /c/Users/Administrator/Desktop/Git/nimi-python/bin/nifake/log/sdist_build_done
