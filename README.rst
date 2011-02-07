Personnal server
================

This set of files is an implementation of the personal project
idea. For more information about the idea see the document
doc/specs/index.rst.

The implementation is done on top of existing deb packages using the
`adminkit <https://github.com/flepied/adminkit>`_ integration toolkit.

Getting started
---------------

To build a package, just use the following command: ::

 $ ./bin/create-pkg <pkg>

The resulting pserv-<pkg> will be available in the build directory.

The specific files for each package are located under the pkg
directory. The common files for all packages are located under the
skel directory.

For each package, we have the following at least:

* adminkit.conf.d/<number><pkg>.conf which will placed in
  /var/lib/adminkit/adminkit.conf.d.
* debian/changelog contains the changelog for the package.
* files and roles directories which contain the settings for adminkit.

Exisiting packages
------------------

The following packages exist:

* apache2
* base
* bind9
* dhcp3-server
* dovecot
* ejabberd
* exim4
* libpam-mysql
* miniupnpc
* openssh-server
* spamassassin
* tor

Global configuration
--------------------

The idea is to have generic packages built using the method described
above and to have only one file to modify in
/etc/adminkit/05variables.conf. This file contains the settings for
your home network like mac and ip adresses of your systems. Using only
one file eases the review and the modification of the settings for
your services. And in the future, it will allow to write a
configuration tool with a nice user interface.
