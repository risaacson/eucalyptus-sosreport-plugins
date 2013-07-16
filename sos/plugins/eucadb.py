## Copyright (C) 2013 Eucalyptus Systems, Inc., Richard Isaacson <richard@eucalyptus.com>

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
import os

class eucadb(sos.plugintools.PluginBase):
    """Eucalyptus Cloud - PostgreSQL
    """

    def setup(self):
        if os.path.isfile('/usr/bin/pg_dump'):
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_auth", suggest_filename="eucalyptus_auth.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_cloud", suggest_filename="eucalyptus_cloud.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_config", suggest_filename="eucalyptus_config.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_dns", suggest_filename="eucalyptus_dns.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_faults", suggest_filename="eucalyptus_faults.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_general", suggest_filename="eucalyptus_general.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_records", suggest_filename="eucalyptus_records.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root --exclude-table=reporting_instance_usage_events eucalyptus_reporting", suggest_filename="eucalyptus_reporting.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_storage", suggest_filename="eucalyptus_storage.sql", timeout = 600)
            self.collectExtOutput("pg_dump -c -o -h /var/lib/eucalyptus/db/data -p 8777 -U root eucalyptus_walrus", suggest_filename="eucalyptus_walrus.sql", timeout = 600)
        return