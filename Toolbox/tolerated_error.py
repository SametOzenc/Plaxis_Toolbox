from easygui import *
from plxscripting.easy import *

title = "Tolerated Error"
button = "Create Model"

s_i, g_i = new_server()


def user_input():
    msg = "Enter the information below:"
    title = "Plaxis Toolbox / Tolerated Error "
    field_names = ["Tolerated Error (Default = 0.01)"]
    field_values = []  # we start with blanks for the values
    field_values = multenterbox(msg, title, field_names)

    # make sure that none of the fields was left blank
    while True:
        if field_values is None:
            break
        errmsg = ""
        for i in range(len(field_names)):
            if field_values[i].strip() == "":
                errmsg = errmsg + \
                    ('"%s" is a required field.\n\n' % field_names[i])
        if errmsg == "":
            break  # no problems found
        field_values = multenterbox(errmsg, title, field_names, field_values)

    return field_values


def main():
    Tolerated_Error = float(user_input()[0])
    g_i.gotostages()
    for phase in g_i.Phases[1:]:
        phase.Deform.UseDefaultIterationParams = False
        phase.Deform.ToleratedError = Tolerated_Error


main()
