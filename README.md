================
= DBNormalizer =
================

--------------------------------------------------------------------------------------------------------------------------------
                                                DBNormalizer Description & Features
--------------------------------------------------------------------------------------------------------------------------------
Design Support Desktop Tool to enhance a Relational Database according to the normalization theory. The present Database 
Normalizer tool provides guidelines to reach the three normal forms and if possible the Boyce-Code normal form in a database, 
always ensuring lossless-join decomposition. This tool also provides candidate keys, attribute closure, and DDL statements 
to create the new relations in Postgresql 9.3.


This tool offers the following features:

- Import of database schemes (metadata) from a database instance; if not database connection is available, relational 
  schemes may be prompted manually.  
- Specification and editing of functional dependencies (FDs).
- Testing if a given set of FDs is satisfied in a database table (only if a database connection is available).
- Computation of a minimal cover.
- Determination of the attribute closure for a given attribute set
- Calculation of all candidate keys
- Normal Form (NF) testing from 1NF up to BCNF; FDs violating any NF will be reported to the user.

Generation of a normalization proposal: synthesis of relations in 3NF is always guaranteed; BCNF synthesis may be possible. 
Normalization includes computation of:

- The new relations
- Functional dependencies for the new relations
- All candidate keys for the new relations
- Normal forms of the new relations (3NF or BCNF)
- If a database connection is established, a SQL script for database transformation is created. This script includes:
    - DDL statements to create the new tables
    - Import and export of FDs and database schemes as XML files (not implememted in the GUI)
    - Import of FDs, automatically retrieved from a database
  
--------------------------------------------------------------------------------------------------------------------------------
                                                    DBNormalizer  Requirements & Installation
--------------------------------------------------------------------------------------------------------------------------------

*Requirements:

  Python 3.4
  PostgreSQL 9.3
  Packages:
  Itertools
  sqlalchemy
  tkinter

The program is divided into 3 modules. We followed the model view controller pattern:

1. Model: All the functions, classes and methods used to perform the decomposition, sql statements, get functional dependencies, read metadata from DBs, etc.
2. Controller: All the logic in the program, i.e. the flow. This acts as an interface between the view & the model. 
3. View: Here is the GUI code.


*Installation

In the terminal/CMD go to the Project folder and execute __main__.py. If you have OSX it will be necessary to execute it as
 python3 __main__.py.

