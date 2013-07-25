eucalyptus-sosreport-plugins
============================

About
-----
eucalyptus-sosreport-plugins was formally a part of the doctor-euca project(https://github.com/eucalyptus/doctor-euca).

This project contains plugins for sosreport(https://github.com/sosreport/sosreport) that focus on the collection needs of Eucalyptus Clouds. Once these plugins have been added to a system with sosreport when run sosreport will pick up and execute them if applicable and place the output into the archive.

These plugins focus on these areas:
* Console - if the Eucalyptus Console is installed.
* Core - Logs and commands that exist on all eucalpyus installs.
* DB - Output from the database.
* Frontend - Executed on the frontend using the installed euca2ools.

You will want to make sure that when you execute sosreport that you have already sourced your eucarc file to get all of the correct output.

The original work for the project was done by Tom Ellis(https://github.com/tomellis). The torch was picked up by Richard Isaacsn(https://github.com/risaacson) to drive and improve the project.

Versioning
----------
r2.2 branch -> sosreport 2.2 (CentOS uses this.)
r2.3 branch -> sosreport 2.3 & 3.0(?) (This is the future.)
master branch -> r2.2 branch

Troubleshooting
---------------
You are invited to point out any problems that might have happened while running the plugins. When submitting an issue please add the following so that we are able to best track down what the issue is.

If you don't know exactly what eucalyptus plugin failed please run the following and attach the output.

`sosreport --batch --only-plugins eucacore,eucadb,eucafrontend,eucaconsole -vv`

If you can identify a signle plugin that is having problems run only that plugin and pull the output.

`sosreport --batch --only-plugins PLUGIN -vv`

New Features
------------
If you can find anything that we are missing please open an issue on this repository, we will review the issue and add the new feature if it is reasonable.