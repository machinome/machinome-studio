============
Installation
============

Machinome Studio is installed from a clone of its repository into a Python
environment of its own, which also holds the framework and the browser
viewer. The studio runs the framework's ``machinome`` command from that
environment and reaches the viewer through it; it imports neither.

What you need
=============

* **Linux.** The studio is validated there and nowhere else.
* **Python 3.11 or later**, with ``venv``.
* **Node.js 22 or later, with npm.** The studio's browser surface is built
  from source, and the OpenSpec command-line tool the studio depends on is
  a Node program.
* **Git.** Every project is its own repository, and the agents commit.
* **OpenSCAD** on ``PATH``, for the framework's OpenSCAD backend and its
  snapshots.
* **An agent backend, logged in.** `Claude Code
  <https://claude.com/claude-code>`_, the ``claude`` command, or `OpenCode
  <https://opencode.ai/>`_, the ``opencode`` command. A project cannot open
  without one; the hub reports which it finds.

Set up
======

.. code-block:: console

   $ git clone git@github.com:machinome/machinome-studio.git
   $ cd machinome-studio
   $ scripts/setup

The script is idempotent; run it again after pulling a change. It:

* creates ``.venv/`` and installs ``machinome[viewer]`` and
  ``machinome-viewer[snapshot]`` into it, with the Chromium build the
  viewer's headless capture needs, which renders the hub's model previews;
* installs the OpenSpec command-line tool, ``@fission-ai/openspec``, with
  npm when ``openspec`` is not already on ``PATH``;
* builds the browser surface into ``floor/static/``;
* installs the studio itself, editable, into ``.venv/``.

The framework's own manual covers the CAD backends a model may use and how
to install them: `Installing Machinome
<https://machinome.readthedocs.io/en/latest/start/install.html>`_. The
studio needs the framework installed with its ``viewer`` extra and nothing
more of it.

Verify
======

.. code-block:: console

   $ source .venv/bin/activate
   $ machinome viewer
   $ openspec --version
   $ claude --version

``machinome viewer`` prints, as JSON, the viewer bundle the framework found
and the API it declares. The studio opens a project only with API
|required-viewer-api| or later, and says so when it refuses. The other two
commands confirm the prerequisite the hub checks and the backend it
reports.

Then start the hub: :doc:`opening-a-project`.

Rebuilding the browser surface
==============================

``floor/static/`` is generated, not tracked. After changing anything under
``floor/frontend/``, or after pulling a change that did, rebuild it:

.. code-block:: console

   $ npm --prefix floor/frontend run build

``scripts/setup`` does the same. A hub that serves a blank page has usually
been started before this build.
