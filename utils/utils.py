#CONSTANTS
import inspect

ADMINURL = "https://www.phptravels.net/admin"
EMAIL = "admin@phptravels.com"
PASSWORD = "demoadmin"

def whoami():
    return inspect.stack()[1][3]