# eucalyptus-sosreport-plugins

Overview:
=========
[sosreport](https://github.com/sosreport/sosreport "sosreport/sosreport") is a tool used by many companies to gather the current state of a system into a portable archive primarily for use in troubleshooting. Eucalyptus CS members identified the potentials of sosreport and created a package with plugins that target Eucalyptus support needs. Everything is written in Python and is easy to modify to our needs.

This project contains plugins for sosreport that focus on the collection needs of Eucalyptus Clouds. Once these plugins have been added to a system with sosreport when run sosreport will pick up and execute them if applicable and place the output into the archive.

These plugins focus on these areas:
* Console - if the Eucalyptus Console is installed.
* Core - Logs and commands that exist on all eucalpyus installs.
* DB - Output from the database.
* Frontend - Executed on the frontend using the installed euca2ools.

History:
========
eucalyptus-sosreport-plugins was formally a part of [doctor-euca](https://github.com/eucalyptus/doctor-euca "eucalyptus/doctor-euca").

You will want to make sure that when you execute sosreport that you have already sourced your eucarc file to get all of the correct output.

The original work for the project was done by [Tom Ellis](https://github.com/tomellis). The torch was picked up by [Richard Isaacson](https://github.com/risaacson) to drive and improve the project.

Targeted Systems:
=================
The plugins package currently targets the version of sosreport that exists in the main CentOS 6.4 repository.

Installation:
=============
It is preferred to install eucalyptus-sosreport-plugins via the package but if not once sosreport is installed you are able to manually copy the files into the plugins directory.

Package Installation:
---------------------
Add the Eucalyptus Tools Repository. 

```shell
cd /etc/yum.repos.d
wget 'http://downloads.eucalyptus.com/software/tools/tools.repo'
```

Install the eucalyptus-sos-tools package which will install the sos package if it is not already installed.

```shell
yum install eucalyptus-sos-plugins
```

Manual Installation:
--------------------
To install eucalyptus-sosreport-plugins manually you will need to have git installed on the system along with sosreport compatible with r2.2.

```shell
git clone https://github.com/eucalyptus/eucalyptus-sosreport-plugins.git
cp eucalyptus-sosreport-plugins/sos/plugins/euca*.py /usr/lib/python2.6/site-packages/sos/plugins/euca*.py
```

Execution:
==========
Execution of sosreport is simple and straight forward. You will need to make sure that it is executed on each of the hosts that you want to collect data from. You will need to source your eucarc any time that you are executing sosreport with the eucalyptus-sosreport-plugins on a CLC host.

At the very least we want to make sure to use the `–batch` option so that interactive questions are no asked.

```shell
sosreport --batch
```

Execution could take severl moments. If it seems to be running long and it is not stuck on the databse the system plugin could be stuck. To skip the system plugin execute the following command.

```shell
sosreport --batch --skip-plugins=system
```

After you have executed sosreport you should move the resulting archive out of /tmp as you risk imparing the system if /tmp is too full. If /tmp is limited you can create the archive in an alternate location by executing.

```shell
sosreport --batch --tmp-dir SOMEDIRECTORY
```

Risks:
======
Systems evolve and applications are upgraded. Going forward we need to make sure that we keep in sync with the version of sosreport that is in the mainline repositories. sosreport r2.3 has a lot of syntax changes from r2.2. When the main repos switch to sosreport r2.3+ we will need to rework our plugins to match the newer framework.
Currently sosreport's github is at version 3.0 of the software.

Versioning:
===========
r2.2 branch -> sosreport 2.2 (CentOS 6.4 uses this.)

r2.3 branch -> sosreport 2.3 & 3.0(?) (This is the future.)

master branch -> r2.2 branch

Troubleshooting:
================
You are invited to point out any problems that might have happened while running the plugins. When submitting an issue please add the following so that we are able to best track down what the issue is.

If you don't know exactly what eucalyptus plugin failed please run the following and attach the output.

```shell
sosreport --batch --only-plugins eucacore,eucadb,eucafrontend,eucaconsole -vv
```

If you can identify a signle plugin that is having problems run only that plugin and pull the output.

```shell
sosreport --batch --only-plugins PLUGIN -vv
```

It can also be helpful to avoid creating an archive. If you use the '–build' flag to leave the directory structure intact. sosreport will print a message about where the directory structure is located.

```shell
sosreport --batch --build
```

Code Repositories:
==================
Official Repository: [eucalyptus/eucalyptus-sosreport-plugins](https://github.com/eucalyptus/eucalyptus-sosreport-plugins)

Original Repository: [risaacson/eucalyptus-sosreport-plugins](https://github.com/risaacson/eucalyptus-sosreport-plugins)

Issues/Improvement:
===================
We are completely open and transparent with eucalyptus-sosreport-plugins as the source resides in a public repository on github. Any issues or requests for improvement should be placed on the github issues page: [eucalyptus-sosreport-plugins/issues](https://github.com/eucalyptus/eucalyptus-sosreports/issues)

Contributing Code:
------------------
First off, thank you.
To submit any code you will need to clone the repository through github. Make any changes to the appropriate branch. Currently you would switch to the b2.2 branch and make your changes. Complete your submission by creating a pull request.
It is polite to send Richard Isaacson a note as a heads-up when work is done.