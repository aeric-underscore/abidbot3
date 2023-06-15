


class AbidBot: 
    # The AbidBot class (new to abidbot3) serves as a way to organize all the parameters floating around in Abid Bot for the python scripts
    #   so that python functions can take an instance of AbidBot as an argument to access all the parameters; 
    
    def __init__(self, params, params_fields, params_gw):
        # the arguments of __init__() are bash files (strings of absolute paths) that live in abidbot/params/
        #   each of these files defines and exports bash variables
        #   then the bash variables are each assigned a "property" in AbidBot
        #
        # UPDATING ABIDBOT:
        #   if there is some change you want to make that requires a new parameter
        #       (such as a new type of Visit plot with its associated boolean flag and xml file)
        #   then add the bash parameters to the appropriate params file
        #       or create a new params file and add it as an argument to __init__()
        #       and to add it as an argument to all the python files
        #   then add respective lines in __init__() as well as in __str__()
        
