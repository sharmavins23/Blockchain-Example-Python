# Blockchain Example (Python)

This project is a simple flask server application designed to teach the basics
of blockchain development. By following along with this project, you will learn
the basics of RESTful applications, servers, package management, and distributed
ledgers.

This project is an extremely over-simplified version of an actual Blockchain
application, so a lot of the functions and methodology are not representative of
real world applications. For instance, the proof-of-work algorithm is
essentially a random generation of hashes. Another example of this project being
a poor representation of real-world Blockchain applications is the way the chain
is stored, which could be improved using a linked list or creating new block
objects.

A block is stored as a JSON object as the current moment; This could be redone
as a pythonic object, and could return a JSON object in its string
representation.

The original code for this project was adapted from Penn State's independent
study program labelled Computer Science 297 - Blockchain Deep Dive. This course
is offered at Penn State's University Park main campus by Penn State's own
[Distributed Ledger Society](https://www.blockchainpsu.com/). The implementation
of this code, however, and my changes/improvements on the initial versions are
my own.

# Program Stack

This project runs on Python 3.8.3, but should work on most versions of Python3.
You also need to have PIP to install the various packages. Some of the key
packages used:

-   **Flask** - Used to create a RESTful server that can communicate with other
    servers;
-   **Requests** - Used to create HTTP requests to neighboring nodes.

# Project Recommendations

When each function was created in this project, it was committed separately. As
such, it's recommended that you look through the individual commits and rework
through changes. All code is documented fairly well, and should explain a lot
about the project.

When you get to the point where you've created the project once or twice, you
can either improve the project or adapt it to your language of choice. Most
programming languages can handle RESTful server creation or RESTful client
creation. Alternatively, another project idea is to create client applications
that interface with this Python implementation of a Blockchain node server.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
