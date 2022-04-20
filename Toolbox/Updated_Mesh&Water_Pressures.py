from plxscripting.easy import *
s_i, g_i = new_server('localhost', 10000, password="ek1g7@W4@Gev?@Q?")

def main():
    for phase in g_i.Phases[1:]:
        if not phase.DeformCalcType == phase.DeformCalcType.fullycoupledflowdeformation:
            phase.Deform.UseUpdatedMesh = True
            if not phase.DeformCalcType == phase.DeformCalcType.dynamic or not phase.DeformCalcType == phase.DeformCalcType.dynamicwithconsolidation:
                phase.Deform.UseUpdatedWaterPressures = True

main()