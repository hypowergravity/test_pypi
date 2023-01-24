# how to create pypi package using flit. 
It requires the following main parameters in pyproject.toml file.
* build-system.
* meta-data.
* package dependency.
* scripts( if any).
* project-url 

# source 
The src folder has an example script under numpy_numeric/example.py which computes arithmetic operations using numpy.
The numpy_numeric also has a test folder and test_run.py test file which runs test using [unittest](https://docs.python.org/3/library/unittest.html).


1. build system section, which provides the flit as a requirement for installation.

____
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"
____

# metadata 
2. metadata which provides the description of the file and other details of the project. 


    [project]
    name = "numpy_numeric" # this is the package name
    authors = [
        {name = "sriram raghavan", email = "hypowergravity@gmail.com"},
    ]
    readme = "Readme.md"
    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.7"
    dynamic = ["version", "description"]
___

if the version is written in the __init__.py file, then the version automatically gets read by flit through the  aforementioned *dynamic* parameter.

 The doc string in the __init__.py which denotes the "description" of the tool is also read by description keyword in   *dynamic* parameter. Exaple of doc string is: """ some example description """

3. Dependency section denotes the requisites that are required for tool functionalities. 

## dependency 
package dependency required.

    dependencies = [
        "requests >=2.6",
        "configparser; python_version == '2.7'",
    ]


4. If the script has to run using command line, this option can be given. 

## shell script 
    [project.scripts]
    numpy_numeric = "numpy_numeric.example:run"
    numpy_numeric_test = "numpy_numeric.test.test_run:run"

    The example.py is that script that contains the function and run that are executable. 

5. Project url which provides documentation of the tool.
## project urls
>
    [project.urls]
    Documentation = "https://github.com/hypowergravity/test_pypi"
    Source = "https://github.com/hypowergravity/test_pypi"


6. Building the package using flit
Once all the inputs are given in the project.toml file, flit build command can be used to build the package.
if flit is not installed, 
~~~
pip install flit
~~~

~~~bash 
flit build 
~~~

* local installation of the package
# Install using command line 
~~~bash
pip install dist/numpy_numeric-0.1.0.tar.gz
~~~

* uninstallation of the local installed package. 
# Uninstalling the package can be done with the package name
~~~bash
pip uninstall numpy_numeric 
~~~
