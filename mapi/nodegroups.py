#!/usr/bin/env python
#

from log                                import center, cleave, cdebug
from nodegroup                          import Nodegroup
from error                              import MapiError
from power_types                        import PowerTypes

# Nodegroups
#
class Nodegroups(object):
    '''
    '''

    # __init__
    #
    def __init__(s, maas):
        center('Nodegroups.__init__')
        s.__maas = maas
        s.__nodegroups = None
        cleave('Nodegroups.__init__')

    # __len__
    #
    def __len__(s):
        return len(list(s.__iter__()))

    # __getitem__
    #
    def __getitem__(s, index):
        center('Nodegroups.__getitem__')
        s.__fetch_if_needed()
        retval = Nodegroup(s.__maas, s.__nodegroups[index])
        cleave('Nodegroups.__getitem__')
        return retval

    # __iter__
    #
    def __iter__(s):
        center('Nodegroups.__iter__')
        s.__fetch_if_needed()
        for group in s.__nodegroups:
            n = Nodegroup(s.__maas, group)
            yield n
        cleave('Nodegroups.__iter__')

    # __fetch_if_needed
    #
    def __fetch_if_needed(s):
        center('Nodegroups.__fetch_if_needed')
        if s.__nodegroups is None:
            response = s.__maas._get(u'/nodegroups/', op='list')
            if not response.ok:
                if type(response.data) == str:
                    cleave('Nodegroups.__fetch_if_needed')
                    raise MapiError(response.data)

            s.__nodegroups = response.data
            cdebug('    fetched')
        cleave('Nodegroups.__fetch_if_needed')

    # power_types
    #
    @property
    def power_types(s):
        center('Nodegroups.power_types')

        retval = PowerTypes(s.__maas)

        cleave('Nodegroups.power_types')
        return retval
