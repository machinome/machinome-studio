==============
Project status
==============

Machinome Studio |release| is experimental and unpublished. It is on no
package index; it is installed from a clone of its repository, as
:doc:`../installation` describes, and its version will move when there is
something to release. Its profiles, its prompts and the disciplines its
agents follow are being exercised on real projects and revised as those
projects teach. ``CHANGELOG.md`` at the root of the repository says what
the current source gives a maker.

What it runs against
====================

Machinome |machinome-version|, installed with its ``viewer`` extra, whose
browser viewer must declare API |required-viewer-api| or later; the studio
checks the installed viewer once when it starts and refuses to open a
project without one. Where the framework and the viewer are published, and
in which versions, is stated in their own manuals; the studio pins neither
beyond that requirement.

Linux is the only validated platform. The agent backends are Claude Code,
OpenCode and qualified Codex, chosen per agent by the project. Codex is
limited to |codex-version| on Linux x86_64, with the models and reasoning
levels in :doc:`../reference/project-configuration`. Other versions and
tool-affecting configurations are refused.

Limits
======

* Setting up needs Python, Node.js, Git, OpenSCAD, Playwright's Chromium
  and a logged-in backend, and is still hand work; ``scripts/setup`` does
  what it can.
* The ``fordesmac`` librarian is out of service until the studio gives it
  a bounded research surface.
* A session keeps nothing: the project's repository is the record, and the
  agents commit but never push. Codex's separate authentication persists,
  but its ended project conversations do not.
* Tool scoping does not OS-sandbox code executed by project builds or
  tests. Codex cannot honor required signed commits. Its native refresh
  path and login persistence were exercised, not multi-day expiry behavior.
* The Build area's envelope fit is a bounding-box comparison, not a
  printability judgement. The studio does not slice and does not assess
  strength, tolerance or safety; nor does the framework.

Direction
=========

Delivering the studio to a maker in the browser, beside a web assistant
and on that maker's existing subscription, is being explored in separate
prototypes. No delivery architecture has been chosen, and nothing in the
studio depends on those prototypes. Packaging the studio as a plugin for
Claude Code, Codex and other assistants is intended and not done; today the
studio runs from its checkout. Publishing the studio is its author's
decision and never a side effect of a green build.
