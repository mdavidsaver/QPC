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
    def __init__(self, QPC, **args):
        # args['controller'] = QPC.args['controller']
        args['SPLY'] = "%02d" % args['SPLY']
        args['SPT'] = "%02d" % args['SPT']
        args['SIZE'] = "%d" % args['SIZE']
        args['HV'] = "%d" % args['HV']
        args['port'] = QPC.args['port']
        args['unit'] = QPC.args['unit']
        args['spon'] = "%1.2G" % args['spon']
        args['spoff'] = "%1.2G" % args['spoff']

        self.__super.__init__(**args)

        # __init__ arguments
        ArgInfo = makeArgInfo(__init__,
            QPC = Ident ('digitelQPC object', QPC)) + \
            _digitelQpcIonpTemplate.ArgInfo.filtered(without = ['port', 'unit'])


class digitelQpcIonpGroup(AutoSubstitution):
    TemplateFile = 'digitelQpcIonpGroup.template'


class dummyIonp(AutoSubstitution):
    TemplateFile = 'dummyIonp.template'
