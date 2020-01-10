import subprocess
import sys

USER = "user022"
PASSWORD = "JZUkRMG7"
PORT=" - p 3637"
HOST="158.129.140.201"
# Ports are handled in ~/.ssh/config since we use OpenSSH

import subprocess
proc = subprocess.Popen(['ssh', 'user@host', 'cat > %s' % filename],
                        stdin=subprocess.PIPE)
proc.communicate(file_contents)
if proc.retcode != 0:
    ...