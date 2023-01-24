# how to create pypi using flit. 
It requires four main description in project.toml file.
* build-system.
* meta-data.
* package dependency.
* scipts( if any).
* project-url 




build system section, which say the build in requirements.



____
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"
____


# metadata 
metadata which say the description of the file. 


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

the version is automatically read by flit in the __init__.py file and the description is also read using doc string in the __init__.py file which has """ example description """


## dependency 
package dependency required.

    dependencies = [
        "requests >=2.6",
        "configparser; python_version == '2.7'",
    ]

## shell script 
    [project.scripts]
    numpy_numeric = "numpy_numeric.example:run"
    numpy_numeric_test = "numpy_numeric.test.test_run:run"

    The example.py is that script that contatin the function and run that are executable. 


## project urls
[project.urls]
Documentation = "https://github.com/hypowergravity/test_pypi"
Source = "https://github.com/hypowergravity/test_pypi"



Once all the inputs are given in the project.toml file, flit build command can be used to build the package.
if flit is not installed, 
~~~
pip install flit
~~~

~~~bash 
flit build 
~~~


#Install using command line 
pip install dist/numpy_numeric-0.1.0.tar.gz


to uninstall.
pip uninstall numpy_numeric 
#
