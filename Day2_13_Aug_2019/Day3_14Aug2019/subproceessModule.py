#!/usr/bin/python
"""
	Purpose: Demo for subprocess
"""

import subprocess
import os

commsn_to_execute = "ping google.com"

p =subprocess.Popen(commsn_to_execute,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)

out,err = p.communicate()

print(f'''
        out:{out.decode('utf-8')}
        err:{err.decode('utf-8')}
        ''')