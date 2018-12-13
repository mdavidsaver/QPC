from iocbuilder import AutoSubstitution, Substitution, SetSimulation, ModuleBase
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *


class digitelQpc(AutoSubstitution, AutoProtocol):
    # Make sure unit is a 2 digit int
    def __init__(self, **args):
        if "unit" in args:
            args["unit"] = "%02d" % int(args["unit"])
            args["port"] = "%02d" % int(args["port"])
            args["punits"] = "%s" % args["punits"]
        self.__super.__init__(**args)

    # Substitution attributes
    TemplateFile = 'digitelQPCController.template'

    # AutoProtocol attributes
    ProtocolFiles = ['digitelQpc.proto']


class digitelQpcPump(ModuleBase):
    pass


class _digitelQpcIonpTemplate(AutoSubstitution):
    TemplateFile = 'digitelQpcIonp.template'


class digitelQpcIonp(_digitelQpcIonpTemplate, digitelQpcPump):
    __doc__ = _digitelQpcIonpTemplate.__doc__

    # Just pass the arguments straight through
    def __init__(self, QPC, 
    	SIZE=500, HV=3000, alh="None", text="$(device)",
    	**args):
        # args['controller'] = QPC.args['controller']
        args['SPLY'] = "%02d" % int(args['SPLY'])
        args['SPT'] = "%02d" % int(args['SPT'])
        args['SIZE'] = "%d" % int(SIZE)
        args['HV'] = "%d" % int(HV)
        args['port'] = QPC.args['port']
        args['unit'] = QPC.args['unit']
        args['spon'] = "%1.2G" % float(args['spon'])
        args['spoff'] = "%1.2G" % float(args['spoff'])
		
        self.__super.__init__(**args)

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        QPC	=Ident('digitelQPC object', digitelQpc),
        SPLY=Simple('Pump supply number', int),
        SPT	=Simple('Set point number for this pump', int),
        SIZE=Simple('Pump Size (L/S)', int),
        HV  =Simple('Target voltage', int),
        text=Simple('Text to display in the ion pump controller window', str),
        alh =Simple('alarm handler tag (Defaults to None)', str) ) + \
        _digitelQpcIonpTemplate.ArgInfo.filtered(without=["port", "unit", "SIZE", "HV", "text", "alh"])
