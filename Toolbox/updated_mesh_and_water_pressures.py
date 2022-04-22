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
    Plaxis 2D Only
    Activates the Updated Mesh and Updated Water Pressures option in all phases except the Initial phase
    """
    g_i.gotostages()
    for phase in g_i.Phases[1:]:
        if not phase.DeformCalcType == phase.DeformCalcType.fullycoupledflowdeformation:
            phase.Deform.UseUpdatedMesh = True 
            if phase.DeformCalcType != phase.DeformCalcType.dynamic and not phase.DeformCalcType == phase.DeformCalcType.dynamicwithconsolidation:
                phase.Deform.UseUpdatedWaterPressures = True


main()
