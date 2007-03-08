#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Last commit info:
----------------------------------
$LastChangedDate: 2007-03-01 18:18:33 +0100 (Do, 01 Mär 2007) $
$Rev: 876 $
$Author: JensDiemer $

Created by Jens Diemer

license:
    GNU General Public License v2 or above
    http://www.opensource.org/licenses/gpl-license.php
"""

import cgi

class LocalModuleResponse(object):
    """
    A local response object for all Modules/Plugins.
    """
    def __init__(self):      
        self._container = []
        
    def write(self, txt):
        if not isinstance(txt, basestring):
            txt = (
                "<p>"
                "[Error: response.write only with Strings! You write a %s]"
                "</p><p>%s</p>"
            ) % (cgi.escape(str(type(txt))), cgi.escape(repr(txt)))
        self._container.append(txt)
    
    def get(self):
        return ''.join(self._container)
