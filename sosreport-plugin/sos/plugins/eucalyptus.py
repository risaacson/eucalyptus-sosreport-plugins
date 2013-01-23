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

class eucalyptus(sos.plugintools.PluginBase):
    """Eucalyptus Cloud related information
    """
    def checkenabled(self):
        if self.isInstalled("eucalyptus"):
            return True
        return False

    def setup(self):
        # Eucalyptus logs
        self.addCopySpec("/etc/eucalyptus/")
        self.addCopySpec("/var/log/eucalyptus/")
	# Generic Eucalyptus Networking (not included in other plugins)
        self.collectExtOutput("/sbin/arp -a")

        # Useful output from euca2ools commands
        clc_commands = ['euca-describe-services -E -A',
                        'euca-describe-availability-zones verbose',
                        'euca-describe-instances verbose',
                        'euca-describe-volumes verbose',
                        'euca-describe-snapshots verbose',
                        'euca-describe-keypairs verbose',
                        'euca-describe-groups verbose',
                        'euca-describe-properties',
                        'euare-accountlist',
                        'euare-getldapsyncstatus']

        try:
            # Only run euca2ools commands if cloud creds are present in environment
            os.environ["EC2_URL"] and os.environ["EC2_ACCESS_KEY"] and os.environ["EC2_SECRET_KEY"]
            for cmd in clc_commands:
                 # Shorten default timeout, 2mins per command
                 self.collectExtOutput(cmd, timeout = 120)
        except KeyError:
                print "Eucalyptus Credentials not in environment, skipping euca commands."
        return
