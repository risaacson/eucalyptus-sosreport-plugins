eucalyptus-sosreport-plugins
============================

r2.2 branch -> sosreport 2.2
r2.3 branch -> sosreport 2.3 & 3.0(?)
master branch -> r2.2 branch

eucalyptus-sosreport-plugins was formally a part of the doctor-euca project(https://github.com/eucalyptus/doctor-euca).

This project contains plugins for sosreport(https://github.com/sosreport/sosreport) that focus on the collection needs of Eucalyptus Clouds. Once these plugins have been added to a system with sosreport when run sosreport will pick up and execute them if applicable and place the output into the archive.

These plugins focus on these areas:
* Console - if the Eucalyptus Console is installed.
* Core - Logs and commands that exist on all eucalpyus installs.
* DB - Output from the database.
* Frontend - Executed on the frontend using the installed euca2ools.

You will want to make sure that when you execute sosreport that you have already sourced your eucarc file to get all of the correct output.

The original work for the project was done by Tom Ellis(https://github.com/tomellis).