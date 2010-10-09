.. Personal Server Specifications documentation master file, created by
   sphinx-quickstart on Mon Jul  5 12:58:22 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Personal Server Specifications!
==========================================================

Contents:

.. toctree::
   :maxdepth: 2

Objectives
==========

The Personal Server is a system hosted in the user's home. Its purpose
is to manage and to visualize multi-media contents from the user.

The Personal Server is to your data what your house is to you, the
mean to keep it, to protect it, but also to allow friends and family
to access it.

The objective of this document is to specify how Personal Server
software components fit together.

This document is a followup of the `Drumbeat
<http://www.drumbeat.org/>`_ meeting about Self Hosting that took
place in Paris at `La Cantine <http://www.lacantine.org/>`_ in July
2010. See the meeting notes at
http://www.drumbeat.org/content/summary-self-hosting-session-drumbeat-paris-2010.

Functionalities
===============

The following functionalities are requested for a Personal Server:

- multi-users,
- distribution of content to the local network,
- network data client,
- easy access to the data from the Internet for its users,
- host web applications to visualize and manage content for its users
  and for their network (friends, familly...) in a componentized way.

The following functionnalities are optional:

- Internet of Things,
- visualize content on the television.

Multi-Users
-----------

There are 2 kinds of users on the Personal Server:

1. users local to the system, who can access it from inside or outside
the home network, e.g. from a remote Internet place.
2. remote users accessing the server from the Internet with adequate
permissions granted by a local user.

The Personal Server allows multiple users to store their data
independently. Each user has his own space in the filesystem.

Distribution of content to the local network
--------------------------------------------

The Personal Server implements the following services for local data access:

- DLNA media server,
- DAAP server,
- Samba server.

Network data client
-------------------

The Personal Server acts as:

- NFS client,
- Samba client,
- UPnP Media Player.

Access to the data from the Internet
------------------------------------

- files are available from the Internet via WebDAV using https.

Web applications
----------------

Web applications need to be packaged in a special way to offer a good
user experience. The applications must follow these points:

- during installation they must register themselves,
- be compatible with the SSO.

The SSO must be able to handle OpenID users and local users.

Internet of things
------------------

The Personal Server has optionaly an email address and an XMPP
address. This allows to communicate with the Personal Server to send
orders or to request informations.

The protocol and security must be studied further. To be completed.

Visualize content on the TV
---------------------------

The content available on the system is viewed on the TV as a special
tv user on the system. So all content content must be accessible to
this user to have it viewed on the TV.

System organization
===================

Authentication
--------------

The authentification is centralized in a SQL database for easy
integration with web services and local services (via `PAM
<http://www.kernel.org/pub/linux/libs/pam/>`_).

Console
-------

A web console to manage services and users is available to local
administrators.

Users
-----

The first user created on the system has the administrator rights and
can give them to other users.

2 users are setup on the system:

1. tv to access data on the television.
2. guest to access data without login from the web.

File system
-----------

Each user has in his own storage area with the following areas:

1. Images to store photos and images.
2. Videos to store video files.
3. Music to store music files.

Access from Internet 
--------------------

The Personal Server tries automatically to redirect http and https
ports from the router to its own local address using the `Internet
Device Gateway Protocol
<http://en.wikipedia.org/wiki/Internet_Gateway_Device_Protocol>`_.

If it fails, it warns the user to setup the redirection on his router
manualy in the administration console.
