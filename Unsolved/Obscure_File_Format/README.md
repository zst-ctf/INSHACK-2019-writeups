# Obscure File Format
Reverse

## Challenge 

Someone left a strange script and some files on a server.

Will you help me understand what it did to a server ?

## Solution

obscure-file-format $ file a
a: data
obscure-file-format $ file k
k: data
obscure-file-format $ file l
l: Python script text executable, ASCII text, with very long lines


pip3 install cryptography

---


	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 1, in <module>
	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 1, in <module>
	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 1, in <module>
	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 1, in <module>
	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 1, in <module>
	  File "l_modified.py", line 8, in hijacked_exec
	    exec_bak(x)
	  File "<string>", line 231, in <module>
	  File "<string>", line 241, in _c1f55bb831d144058e27ac1a85645c87
	NameError: name '_0aa77fc2a6db4be4b58865ae4d13913a' is not defined

---

	obscure-file-format $ python3 l_later.py 
	usage: l_later.py [-h] d o
	l_later.py: error: the following arguments are required: d, o
	obscure-file-format $ python3 l_later.py -h
	usage: l_later.py [-h] d o

	positional arguments:
	  d
	  o

	optional arguments:
	  -h, --help  show this help message and exit
	obscure-file-format $ python3 l_later.py a k
	Traceback (most recent call last):
	  File "l_later.py", line 355, in <module>
	    _46a7c5c324234b988db190a6f5011912()
	  File "l_later.py", line 352, in _46a7c5c324234b988db190a6f5011912
	    _1cf3273eea5e4642b24446463c8edb23.mkdir(parents=_33186cdf76944c1d8b235829cede199b, exist_ok=_33186cdf76944c1d8b235829cede199b)
	  File "/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/pathlib.py", line 1230, in mkdir
	    self._accessor.mkdir(self, mode)
	FileExistsError: [Errno 17] File exists: 'k'
	obscure-file-format $ python3 l_later.py a 1
	obscure-file-format $ python3 l_later.py k 1
	obscure-file-format $ python3 l_later.py "hi" 1

Takes input flag as a string and then outputs 2 files: `archive`, `keystore`.



## Flag

	??