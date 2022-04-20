from plxscripting.easy import *
s_i, g_i = new_server()

def main():
    g_i.gotomesh()
    g_i.mesh()
    g_i.gotostages()
    g_i.calculate()

main()
