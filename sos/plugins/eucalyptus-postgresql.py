## Copyright (C) 2012-2013 Eucalyptus Systems, Inc., Tom Ellis <tellis@eucalyptus.com>

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools
import os, sys

class eucalyptus_postgresql(sos.plugintools.PluginBase):
    """Eucalyptus Cloud related information
    """
    def checkenabled(self):
        if self.isInstalled("eucalyptus-postgresql"):
            return True
        return False

    def setup(self):
        if os.path.isfile('/usr/bin/pg_dumpall'):
            self.collectExtOutput("pg_dumpall -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root", timeout = 600)
