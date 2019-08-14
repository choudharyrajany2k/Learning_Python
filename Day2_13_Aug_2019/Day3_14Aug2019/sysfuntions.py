#!/usr/bin/python
"""
	Purpose: Demo sys

"""
import sys
from pprint import pprint
sys.stdout.write('test')
# print(f"sys.copyright {sys.copyright}")

pprint(f"sys.copyright {sys.path}")

pprint(f"executing file {__file__}")

# print(f"sys.copyright {sys.builtin_function_names}")
# print(f"sys.copyright {sys.copyright}")
# print(f"sys.copyright {sys.copyright}")
# print(f"sys.copyright {sys.copyright}")

print(f"sys.platform {sys.platform}")