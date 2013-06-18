eucalyptus-sosreport-plugins
============================

eucalyptus-sosreport-plugins was formally a part of the doctor-euca project(https://github.com/eucalyptus/doctor-euca).

This project contains plugins for sosreport that focus on the collection needs of Eucalyptus Clouds.

These plugins are compatable with recent versions of sosreport after version 2.3. While attempts at getting it into the distribution repositories has stalled we will work towards hosting pre-built packages on the Eucalyptus download servers.

If you do not have sosreport with a version after 2.3 you can download the source(https://github.com/sosreport/sosreport.git), compile, and install the RPM.

git clone https://github.com/sosreport/sosreport.git; cd ~/sosreport; make clean rpm; yum remove -y sos; yum install -y dist-build/noarch/sos-2.3-1.el6.noarch.rpm

The original work for the project was done by Tom Ellis.
