from plxscripting.easy import *
s_i, g_i = new_server()  

def main():
    for i in g_i.Phases[1:]:
        g_i.delete(i)

main()