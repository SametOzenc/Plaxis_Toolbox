# BOILERPLATE for PLAXIS #
# To be used when running via Expert > Run python tool
from plxscripting.easy import *

s_i, g_i = new_server()

# To be used when running via SciTE
# localhostport_i = 10000
# password = 'YOUR_PASSWORD'
# s_i, g_i = new_server('localhost', localhostport_i, password=password)
# END OF BOILERPLATE ##


def main():
    """
    Deletes all phases except the Initial Phase
    """
    g_i.gotostages()
    for i in g_i.Phases[1:]:
        g_i.delete(i)


main()
