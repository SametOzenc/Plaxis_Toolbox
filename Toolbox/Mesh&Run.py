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
    Mesh medium element distribution and calculate
    """
    g_i.gotomesh()
    g_i.mesh()
    g_i.gotostages()
    g_i.calculate()

main()
