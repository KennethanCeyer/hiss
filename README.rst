|pypi| |ghit.me| |License: MIT| |Join the chat at
https://gitter.im/KennethanCeyer/PIGNOSE|

What is the hiss?
-----------------

``hiss`` is simple cli tool to control the database schema. If you care
a stable enterprise service, You need to know hiss cli.

If you designed the schema of development environment database, and you
want to move it to a production server.

It would be difficult and unstable. hiss can help to migrate for
deployment and also help to ETL for another database engine.

Installation
------------

hiss can be installed ``pypi``.

.. code:: bash

    $ pip install hiss-cli

Features (Plan)
---------------

-  Supporting common databases (MySQL, MSSQL, PostgreSQL, MariaDB,
   Oracle)
-  Controlling revision history of changes the schema.
-  Commit, Rollback, Push, Reset, Tag, List, Show (The simple command
   designs based on ``Git``.
-  ETL to another database and analyze (To another common databases or
   distribute engines: Athena, Presto, Impala, Druid, Hadoop system, or
   JSON, XML, CSV)

Design (Plan)
-------------

.. code:: bash

    $ hiss init
    $ hiss remote add origin database.endpoint.com:3306

    > connecting... done.
    > database `MySQL`, v5.7.11
    > Type username: {username}
    > Type password: {password}

    $ hiss show databases
    > couting databses: 32.
    > databse_1_schema
    > databse_2_schema
    > databse_3_schema
    > more...

    $ hiss checkout database_1_schema
    > switched to database `database_1_schema`.

    $ hiss show tables
    > counting tables: 160.
    > information_schema
    > table_1_sample
    > table_2_sample
    > table_3_sample

    $ hiss set tables table_1_sample
    > now your current table is `table_1_sample`.

    $ hiss add column new_column int(64) pk auto_increment default 0 not null -m 'column comment'
    > add column `new_column`, done.

    $ hiss status
    > counting changes: 1, done.
    > add column 'new_column' int(64) primary auto_increment default 0 not null
    > : column comment
    > end

    $ hiss commit -m 'add new column for testing'.
    > 1 changes are committed, 1 add(+), 0 remove(-), 0 modified(=).

    $ hiss reset HEAD^ --hard
    > reset... done.
    > : first commit message.

    $ hiss tag -a v1.0 -m 'marking for first commition.'
    > done.

Notice
------

This repository is still progress under development.

If you want to use the demo version, Please send a message via gitter
(Check the above badge).

Thank you.

TODO
----

- [] Continous Integration & Continous Deployment
- [] Add UnitTest
- [] Add commands: init, show, checkout
- [] Integration with MySQL
- [] Branding: LOGO

.. |pypi| image:: https://badge.fury.io/py/hiss-cli.svg
    :target: https://badge.fury.io/py/hiss-cli
.. |ghit.me| image:: https://ghit.me/badge.svg?repo=KennethanCeyer/hiss
   :target: https://ghit.me/repo/KennethanCeyer/hiss
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
.. |Join the chat at https://gitter.im/KennethanCeyer/PIGNOSE| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/KennethanCeyer/PIGNOSE?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
