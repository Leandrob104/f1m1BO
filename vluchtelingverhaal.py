import sys
import time
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7./100)

slowprint("de dag begint zoals elke andere dag")
slowprint("opeens hoor je buiten een alarm")
slowprint("")
