# SALES CLI

A simple python CLI to manage clients in a file.

___
## Instalation

1. __Create a new virtual environment__
``` 
$ sudo pip3 install virtualenv
$ virtualenv --python=python3 venv
```
2. __Activate the new virtual environment__
``` 
$ source venv/bin/activate
```
3. __Install Click__
``` 
(venv)> $ pip install Click
```
4. __Install sales cli__

``` 
$ cd sales
$ pip install --editable .
```
To verify the installation type:  
``` $sales ```  
and you will recieve a response like this:  
``` 
Usage: sales [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clients  Manages the clients lifecycle

```
    