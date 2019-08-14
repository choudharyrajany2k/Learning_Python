#!/usr/bin/python
"""
	Purpose: List All python files
"""

import os

_currentWorkingDirectory = os.getcwd()
_changeDirectory = os.chdir(_currentWorkingDirectory)

print(list(os.walk(r'C:\Users')))
