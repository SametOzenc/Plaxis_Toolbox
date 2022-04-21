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
    Activates the Updated Mesh and Updated Water Pressures option in all phases except the Initial phase
    """
    for phase in g_i.Phases[1:]:
        if not phase.DeformCalcType == phase.DeformCalcType.fullycoupledflowdeformation: #There is no Uptaded Mesh option for Fully coupled flow-deformatio calculation type  
            phase.Deform.UseUpdatedMesh = True #Activates the Updated Mesh option
            if phase.DeformCalcType != phase.DeformCalcType.dynamic and not phase.DeformCalcType == phase.DeformCalcType.dynamicwithconsolidation: #There is no Updated Water Pressures option for dynamic and dynamic with consolidation calculation type  
                phase.Deform.UseUpdatedWaterPressures = True #Activates the Updated Mesh and Updated Water Pressures option
main()
