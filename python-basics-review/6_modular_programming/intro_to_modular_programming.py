# MODULES

# It is impractical to use the Python interpreter only in interctive mode as all your commands get lost when you close the interactive mode.
# Most times you want to save and aceess commands you have typed
# When you want to create a longer program, Python gives you the option to save commands and definitions in a file and pass that to the interpreter
# This process is known as creating a SCRIPT
# Then when the SCRIPT gets too long it is a good programming process to split the commands and definitions into multiple files for better organization and maintenance
# One may also want to use function definitions provided in one script in another script
# Python provides a means to support all of this
# Python provides a means to put all commands and function definitions in a .py file and then use it in the interactive mode or in a script
# Such a .py file is called a module. The module name is the name of the file before .py extension
# Simply put a .py file that stores commands and definitions called a module
# Within a module, it's name is available and accessible as the value of the __name__ variable (in string form) when it is imported
# You can import definitions from one module to another
# One can import a module using the import statement
# Example:

import example

# Once a module is imported, the module's name is added to the current namespace.
# The names of functions and definitions in the module can be accessed via this module name and are not added to the current namespace themselves
# We can now use the functions defined in example

result= example.add(4,5)
print(result)

result=example.subtract(15, 3)
print(result)

# if you want to use a function repeatedly, you can assign it to a local name
addr= example.add
print((addr(3,9)))

print(__name__) # prints name of current module that we are in
print(example.__name__) # prints name of example module

# A module can contain executable statements as well as function definitions
# The goal of having the executable statements is to initialize the module
# These statements are executed the first time the module's name is mentioned in the import statement
# They are also run if the file is executed as a script.

# Every module has it's own PRIVATE NAMESPACE
# This namespace is treated as the global namespace by all the functions in the module
# Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.
# On the other hand, you can acess a module’s global variables with the same notation used to refer to its functions, modname.itemname.
print(example.var1, example.var2)

# Moduless can also have other modules imported within them
# This is done via the import statement as previously discussed
# It is convention to place all import statements at the top of a module
# When another module is imported within a module, the imported module's name is added to the current module's global namespace
# We can use the from keyword alongside import to import names or functions alone from the module
# This does not introduce the module name from which the imports are taken in the local namespace
# Example
from example import var1, add

a=add(21,3)
print(a)
print(var1)
# There is a version of import using for that imports all names from a particular module
# That is:
from example import *

# This imports all names except those beginning with an underscore (_). 
# Python programmers usually do not use this feature since it introduces an unknown set of names into the interpreter
# These names may conflict with previously defined names
# In general using * in an import statement is frowned upon as it reduces the readability of code 

# If the module name is followed by as, then the name following as is bound directly to the imported module.
# You can refer to and access the module using this name within the current module
# Example:

import example as batman

result=batman.add(3,4)
print(result)

# You can use the as and from keywords in conjunction with each other
# Example
from example import var1 as robin
print(robin)

# Note that you can also run a module in the command line
# The code will be executed in the same manner as if the module was imported
# Except the value of __name__ variable is set to '__main__' instead of the name of the module
# Syntax for running a module in command line
# python3 module_name.py <arguments>
# arguments mentioned above are optional and can be accessed in sys.argv using the sys module (refer to section 2.intro_to_python_interpreter)
# This means you can add a line of the form if __name=="__main" to the module so that it can be run as a script or imported as a module
# Refer the example module for this example

# THE MODULE SEARCH PATH
# When a module is imported in a Python file, the Python interpreter first checks if there is a built in module with the same name
# Built-in module names can be viewed after importing the sys module at the sys.builtin_module_names
# This returns a tuple containing all the built in module names

import sys
print(sys.builtin_module_names)

# If the module name does not belong to the list of built in module names, then the Python interpreter searches for the file with name of the imported module in a list of directories given by the sys.path name
# This sys.path variable is a list of directories
print(sys.path)

# The sys.path variable is initialized from the following locations:
# 1. The directory containing the input script (current directorywhen no file is specified)
# 2. PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# 3. The installation-dependent default (by convention including a site-packages directory, handled by the site module).

# Python programs can modify the sys.path variable after initialization
# The directory containing the script that is currently being run is the first member of the sys.path list, ahead of the standard library path
# This means the current folder takes priority over standard python modules 
# (Note that standard python modules are different from built in python modules. The built in Python modules are a small subset of the Python Standard Library modules.)
# This may cause potential errors when you have files in your directory named the same as some standar python modules
# Then if you try to import the standard library module, you will import the files in your local directory instead
# So, avoid naming files the same as standard Python modules

# 'COMPILED' PYTHON FILES
# Caching is a technique used in computing to store results of expensive or frequently used operations so they can be quickly retrieved later without recomputing them.
# In order to speed up the loading of modules, Python caches the compiled version (bytecode) of each module in the __pycache__ directory under the name module.version.pyc
# Above, the version placeholder encodes the format of the compiled file (it generally contains the python version number) E.g  __pycache__/spam.cpython-33.pyc
# In the above example, spam is the name of a module, encoding is of type cpython version3.3
# This naming convention allows compiled modules from different releases and different versions of Python to coexist.
# Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. 
# This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.
# Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. 
# Second, it does not check the cache if there is no source module.

# PYTHON STANDARD MODULES
# Python comes with a library of standard modules
# These are all described in the Python Library Reference
# Some of these modules are built into the interpreter
# They are used in order to provide access to functionality that is necessary for things such as OS operations but not a core part of the language itself
# The set of such modules built into the interpreter also depends upon the platform. E.g the winreg module is only available in Windows
# An example of a module built into the Python interpreter in every case is the sys modules

# THE dir() FUNCTION
# dir() is a built in function used to list all names that a module defines
# It lists all names: those of functions, variables and modules
# It returns a sorted list of strings and takes a module name as the arguments
print(dir(sys))

# Without arguments, dir() lists the names you have defined currently
print(dir())

# dir() however does not list the names of all the builtin functions and variables
# These names however are defined in the builtins module
import builtins
print(dir(builtins))

# PACKAGES
# Packages provide a means of structuring Python's module namespace
# It uses dotted module names to classify submodules as a means of duing this
# Suppose A is a module, a submodule B of A is referred to as module A.B
# Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.
# A package in Python is essentially a directory that contains multiple python modules (.py files)
# For Python to treat a directory as a package, the directory must have a __init__.py file which can even be empty
# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable.
# The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.
# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

# Importing * from a package
# Saying import package.module.* should will import all submodules inside of module
# This may however take a long time if module has a lot of submodules
# It may also result in weird behaviour that should happen only if a particular submodule is imported explicitly
# To avoid this there exists a particular convention
# The package author is supposed to provide an explicit index of the package in the __init__.py file of the package
# The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered.
#  It is up to the package author to keep this list up-to-date when a new version of the package is released.
#  Package authors may also decide not to support it, if they don’t see a use for importing * from their package.
# E.g assume in __init__.py: __all__ = ["echo", "surround", "reverse"]
# Be aware that submodules might become shadowed by locally defined names.
# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package.
# This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements.
# Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.
# Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.