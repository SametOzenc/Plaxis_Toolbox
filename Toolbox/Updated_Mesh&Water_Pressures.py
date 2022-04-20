from plxscripting.easy import *
s_i, g_i = new_server()

def main():
    for phase in g_i.Phases[1:]:
        if not phase.DeformCalcType == phase.DeformCalcType.fullycoupledflowdeformation:
            phase.Deform.UseUpdatedMesh = True
            if phase.DeformCalcType != phase.DeformCalcType.dynamic and not phase.DeformCalcType == phase.DeformCalcType.dynamicwithconsolidation:
                phase.Deform.UseUpdatedWaterPressures = True
main()
