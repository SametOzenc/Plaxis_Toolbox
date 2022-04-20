from plxscripting.easy import *
s_i, g_i = new_server()

def main():
    for phase in g_i.Phases[1:]:
        if phase.DeformCalcType == phase.DeformCalcType.consolidation or phase.DeformCalcType == phase.DeformCalcType.plastic or phase.DeformCalcType == phase.DeformCalcType.safety:
            if phase.Deform.UseUpdatedMesh == True:
                phase.Deform.UseUpdatedWaterPressures = True

main()