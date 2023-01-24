# how to create pypi using flit. 
It requires two main description. 



build system section, which say the build in requirements.



____
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"
____


# metadata 
metadata which say the description of the file. 


    [project]
    name = "astcheck"
    authors = [
        {name = "Thomas Kluyver", email = "thomas@kluyver.me.uk"},
    ]
    readme = "README.rst"
    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.5"
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
    numpy_numeric = "src.master:main"

The master.py is that script that contatin the function and main is the executable function. 


## project urls
[project.urls]
Documentation = "https://github.com/hypowergravity/test_pypi"
Source = "https://github.com/hypowergravity/test_pypi"



Once all the inputs are given in the project.toml file, flit build command can be used to build the package.
~~~bash 
flit build 
~~~
