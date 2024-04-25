![Autodoc Pydantic](https://raw.githubusercontent.com/mansenfranzen/autodoc_pydantic/main/docs/source/material/logo_black.svg)

[![PyPI - Version](https://img.shields.io/pypi/v/autodoc_pydantic?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/autodoc_pydantic/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/autodoc_pydantic?style=for-the-badge&logo=python&logoColor=white&color=blue)](https://pypistats.org/packages/autodoc-pydantic)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/mansenfranzen/autodoc_pydantic/tests-push-pr.yml?style=for-the-badge&logo=github)](https://github.com/mansenfranzen/autodoc_pydantic/actions)
[![Codecov](https://img.shields.io/codecov/c/gh/mansenfranzen/autodoc_pydantic?style=for-the-badge&logo=codecov)](https://app.codecov.io/gh/mansenfranzen/autodoc_pydantic)
[![Read the Docs (stable)](https://img.shields.io/readthedocs/autodoc_pydantic/stable?style=for-the-badge&logo=sphinx&label=Docs%20stable)](https://autodoc-pydantic.readthedocs.io/en/stable/)

[![GitHub License](https://img.shields.io/github/license/mansenfranzen/autodoc_pydantic?style=for-the-badge&color=orange&logo=semanticscholar&logoColor=white)](https://github.com/mansenfranzen/autodoc_pydantic/blob/main/LICENSE)
[![linting - ruff](https://img.shields.io/badge/Linting-orange?style=for-the-badge&logo=ruff&logoColor=white&label=ruff)](https://github.com/astral-sh/ruff)
[![types - Mypy](https://img.shields.io/badge/types-Mypy-orange.svg?style=for-the-badge&logo=python&logoColor=white)](https://github.com/python/mypy)<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-50-orange.svg?style=for-the-badge)](#contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


You love [pydantic](https://pydantic-docs.helpmanual.io/) ❤ and you want to
document your models and configuration settings with [sphinx](https://www.sphinx-doc.org/en/master/)?

Perfect, let's go. But wait, sphinx' [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
does not integrate too well with pydantic models 😕.

Don't worry - just `pip install autodoc_pydantic` ☺.

# 🌟 Features

- 💬 provides default values, alias and constraints for model fields
- 🔗 adds hyperlinks between validators and corresponding fields
- 📃 includes collapsable model json schema
- 🏄 natively integrates with autodoc and autosummary extensions
- 📎 defines explicit pydantic prefixes for models, settings, fields, validators and model config
- 📋 shows summary section for model configuration, fields and validators
- 👀 hides overloaded and redundant model class signature
- 🔱 visualizes entity-relationship-diagrams for class hierarchies
- 🔨 allows complete configurability on global and per-model level
- 🍀 supports `pydantic >= 1.5.0` and `sphinx >= 4.0.0`

# 📄 Documentation

| Section                         | Description                           |
|-----------------------------------------|-----------------------------------------|
| [📑 Landing Page](https://autodoc-pydantic.readthedocs.io/en/stable/)    | Guides and detailed information.        |
| [🛠️ Installation](https://autodoc-pydantic.readthedocs.io/en/stable/users/installation.html)      | Setup and installation procedures.      |
| [🔧 Configuration](https://autodoc-pydantic.readthedocs.io/en/stable/users/configuration.html)    | System or application settings.         |
| [💡 Usage](https://autodoc-pydantic.readthedocs.io/en/stable/users/usage.html)                     | How to use the application or tool.     |
| [🌐 Examples](https://autodoc-pydantic.readthedocs.io/en/stable/users/examples.html)              | Showcase and usage examples.                |
| [👨‍💻 Developer Guide](https://autodoc-pydantic.readthedocs.io/en/stable/developers/setup.html) | In-depth guide for developers.          |


# 🙏 Acknowledgements

Thanks to great open source projects [sphinx](https://www.sphinx-doc.org/en/master/),
[pydantic](https://pydantic-docs.helpmanual.io/) and
[poetry](https://python-poetry.org/) (and so many more) ❤ in addition to the following contributors:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mansenfranzen"><img src="https://avatars.githubusercontent.com/u/18086180?v=4?s=100" width="100px;" alt="Franz Wöllert"/><br /><sub><b>Franz Wöllert</b></sub></a><br /><a href="#maintenance-mansenfranzen" title="Maintenance">🚧</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Documentation">📖</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Tests">⚠️</a> <a href="#content-mansenfranzen" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yves-renier"><img src="https://avatars.githubusercontent.com/u/102358016?v=4?s=100" width="100px;" alt="Yves Renier"/><br /><sub><b>Yves Renier</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=yves-renier" title="Documentation">📖</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=yves-renier" title="Tests">⚠️</a> <a href="#content-yves-renier" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TheBeardedBerserkr"><img src="https://avatars.githubusercontent.com/u/32272268?v=4?s=100" width="100px;" alt="TheBeardedBerserkr"/><br /><sub><b>TheBeardedBerserkr</b></sub></a><br /><a href="#ideas-TheBeardedBerserkr" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vlcinsky"><img src="https://avatars.githubusercontent.com/u/635911?v=4?s=100" width="100px;" alt="Jan Vlčinský"/><br /><sub><b>Jan Vlčinský</b></sub></a><br /><a href="#security-vlcinsky" title="Security">🛡️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/antvig"><img src="https://avatars.githubusercontent.com/u/25105210?v=4?s=100" width="100px;" alt="antvig"/><br /><sub><b>antvig</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aantvig" title="Bug reports">🐛</a> <a href="#userTesting-antvig" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://roguh.com"><img src="https://avatars.githubusercontent.com/u/6373447?v=4?s=100" width="100px;" alt="Hugo O Rivera"/><br /><sub><b>Hugo O Rivera</b></sub></a><br /><a href="#ideas-roguh" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ybnd"><img src="https://avatars.githubusercontent.com/u/31547038?v=4?s=100" width="100px;" alt="yura bondarenko"/><br /><sub><b>yura bondarenko</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aybnd" title="Bug reports">🐛</a> <a href="#userTesting-ybnd" title="User Testing">📓</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://tahoward.github.io"><img src="https://avatars.githubusercontent.com/u/547570?v=4?s=100" width="100px;" alt="Trevor Howard"/><br /><sub><b>Trevor Howard</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Atahoward" title="Bug reports">🐛</a> <a href="#userTesting-tahoward" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thomas-pedot"><img src="https://avatars.githubusercontent.com/u/86731212?v=4?s=100" width="100px;" alt="thomas-pedot"/><br /><sub><b>thomas-pedot</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Athomas-pedot" title="Bug reports">🐛</a> <a href="#userTesting-thomas-pedot" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/matutter"><img src="https://avatars.githubusercontent.com/u/2701379?v=4?s=100" width="100px;" alt="Mat Utter"/><br /><sub><b>Mat Utter</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Amatutter" title="Bug reports">🐛</a> <a href="#userTesting-matutter" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/davidchall"><img src="https://avatars.githubusercontent.com/u/1804856?v=4?s=100" width="100px;" alt="David C Hall"/><br /><sub><b>David C Hall</b></sub></a><br /><a href="#ideas-davidchall" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-davidchall" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://yoshanuikabundi.me"><img src="https://avatars.githubusercontent.com/u/28590748?v=4?s=100" width="100px;" alt="Josh A. Mitchell"/><br /><sub><b>Josh A. Mitchell</b></sub></a><br /><a href="#ideas-Yoshanuikabundi" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=Yoshanuikabundi" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/goroderickgo"><img src="https://avatars.githubusercontent.com/u/17296713?v=4?s=100" width="100px;" alt="Roderick Go"/><br /><sub><b>Roderick Go</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=goroderickgo" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lilyminium"><img src="https://avatars.githubusercontent.com/u/31115101?v=4?s=100" width="100px;" alt="Lily Wang"/><br /><sub><b>Lily Wang</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=lilyminium" title="Documentation">📖</a> <a href="#content-lilyminium" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/j-carson"><img src="https://avatars.githubusercontent.com/u/44308120?v=4?s=100" width="100px;" alt="j-carson"/><br /><sub><b>j-carson</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aj-carson" title="Bug reports">🐛</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=j-carson" title="Code">💻</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=j-carson" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://imada.sdu.dk/~jlandersen/"><img src="https://avatars.githubusercontent.com/u/6465735?v=4?s=100" width="100px;" alt="Jakob Lykke Andersen"/><br /><sub><b>Jakob Lykke Andersen</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=jakobandersen" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/astrojuanlu"><img src="https://avatars.githubusercontent.com/u/316517?v=4?s=100" width="100px;" alt="Juan Luis Cano Rodríguez"/><br /><sub><b>Juan Luis Cano Rodríguez</b></sub></a><br /><a href="#content-astrojuanlu" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nchaly"><img src="https://avatars.githubusercontent.com/u/2665273?v=4?s=100" width="100px;" alt="Mikalai Chaly"/><br /><sub><b>Mikalai Chaly</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Anchaly" title="Bug reports">🐛</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=nchaly" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/StigKorsnes"><img src="https://avatars.githubusercontent.com/u/10085536?v=4?s=100" width="100px;" alt="Stig Korsnes"/><br /><sub><b>Stig Korsnes</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3AStigKorsnes" title="Bug reports">🐛</a> <a href="#ideas-StigKorsnes" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/iliakur"><img src="https://avatars.githubusercontent.com/u/899591?v=4?s=100" width="100px;" alt="Ilia Kurenkov"/><br /><sub><b>Ilia Kurenkov</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Ailiakur" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/my-orcid?orcid=0000-0002-5470-1676"><img src="https://avatars.githubusercontent.com/u/3826210?v=4?s=100" width="100px;" alt="Grzegorz Bokota"/><br /><sub><b>Grzegorz Bokota</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3ACzaki" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jgunstone"><img src="https://avatars.githubusercontent.com/u/21370980?v=4?s=100" width="100px;" alt="jgunstone"/><br /><sub><b>jgunstone</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Ajgunstone" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/iwyrkore"><img src="https://avatars.githubusercontent.com/u/92745880?v=4?s=100" width="100px;" alt="iwyrkore"/><br /><sub><b>iwyrkore</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=iwyrkore" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/spacemanspiff2007"><img src="https://avatars.githubusercontent.com/u/10754716?v=4?s=100" width="100px;" alt="spacemanspiff2007"/><br /><sub><b>spacemanspiff2007</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aspacemanspiff2007" title="Bug reports">🐛</a> <a href="#ideas-spacemanspiff2007" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://luke.hsiao.dev"><img src="https://avatars.githubusercontent.com/u/7573542?v=4?s=100" width="100px;" alt="Luke Hsiao"/><br /><sub><b>Luke Hsiao</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Alukehsiao" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nickeldan"><img src="https://avatars.githubusercontent.com/u/21210592?v=4?s=100" width="100px;" alt="Daniel Walker"/><br /><sub><b>Daniel Walker</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Anickeldan" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://t.me/pipeknight"><img src="https://avatars.githubusercontent.com/u/34810566?v=4?s=100" width="100px;" alt="Evgeniy Lupashin"/><br /><sub><b>Evgeniy Lupashin</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3APipeKnight" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://janhendrikewers.uk/"><img src="https://avatars.githubusercontent.com/u/12383029?v=4?s=100" width="100px;" alt="Jan-Hendrik Ewers"/><br /><sub><b>Jan-Hendrik Ewers</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aiwishiwasaneagle" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Asneakers-the-rat" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://charlie.machalow.com"><img src="https://avatars.githubusercontent.com/u/5749838?v=4?s=100" width="100px;" alt="Charles Machalow"/><br /><sub><b>Charles Machalow</b></sub></a><br /><a href="#question-csm10495" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkaraouzene"><img src="https://avatars.githubusercontent.com/u/20064077?v=4?s=100" width="100px;" alt="Thomas Karaouzene"/><br /><sub><b>Thomas Karaouzene</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Atkaraouzene" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/caseyzak24"><img src="https://avatars.githubusercontent.com/u/29411281?v=4?s=100" width="100px;" alt="caseyzak24"/><br /><sub><b>caseyzak24</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=caseyzak24" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/PriOliveira"><img src="https://avatars.githubusercontent.com/u/13801839?v=4?s=100" width="100px;" alt="Priscila Oliveira"/><br /><sub><b>Priscila Oliveira</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/pulls?q=is%3Apr+reviewed-by%3APriOliveira" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-PriOliveira" title="User Testing">📓</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/awoimbee"><img src="https://avatars.githubusercontent.com/u/22431493?v=4?s=100" width="100px;" alt="Arthur Woimbée"/><br /><sub><b>Arthur Woimbée</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/pulls?q=is%3Apr+reviewed-by%3Aawoimbee" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-awoimbee" title="User Testing">📓</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=awoimbee" title="Code">💻</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=awoimbee" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/effigies"><img src="https://avatars.githubusercontent.com/u/83442?v=4?s=100" width="100px;" alt="Chris Markiewicz"/><br /><sub><b>Chris Markiewicz</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aeffigies" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nagledb"><img src="https://avatars.githubusercontent.com/u/727435?v=4?s=100" width="100px;" alt="David B. Nagle"/><br /><sub><b>David B. Nagle</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Anagledb" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jerryjiahaha"><img src="https://avatars.githubusercontent.com/u/3163720?v=4?s=100" width="100px;" alt="JerryJia"/><br /><sub><b>JerryJia</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=jerryjiahaha" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/devmonkey22"><img src="https://avatars.githubusercontent.com/u/5084545?v=4?s=100" width="100px;" alt="Mike D"/><br /><sub><b>Mike D</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=devmonkey22" title="Code">💻</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Adevmonkey22" title="Bug reports">🐛</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=devmonkey22" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/daquinteroflex"><img src="https://avatars.githubusercontent.com/u/149674618?v=4?s=100" width="100px;" alt="Dario Quintero (Flexcompute)"/><br /><sub><b>Dario Quintero (Flexcompute)</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/pulls?q=is%3Apr+reviewed-by%3Adaquinteroflex" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rafa-guedes"><img src="https://avatars.githubusercontent.com/u/7799184?v=4?s=100" width="100px;" alt="Rafael Guedes"/><br /><sub><b>Rafael Guedes</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=rafa-guedes" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/caerulescens"><img src="https://avatars.githubusercontent.com/u/29284192?v=4?s=100" width="100px;" alt="Andrew Linzie"/><br /><sub><b>Andrew Linzie</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=caerulescens" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tasansal"><img src="https://avatars.githubusercontent.com/u/13684161?v=4?s=100" width="100px;" alt="Altay Sansal"/><br /><sub><b>Altay Sansal</b></sub></a><br /><a href="#ideas-tasansal" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.git-pull.com"><img src="https://avatars.githubusercontent.com/u/26336?v=4?s=100" width="100px;" alt="Tony Narlock"/><br /><sub><b>Tony Narlock</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=tony" title="Code">💻</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=tony" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://huxuan.org/"><img src="https://avatars.githubusercontent.com/u/726061?v=4?s=100" width="100px;" alt="Xuan (Sean) Hu"/><br /><sub><b>Xuan (Sean) Hu</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Ahuxuan" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Cielquan"><img src="https://avatars.githubusercontent.com/u/43916661?v=4?s=100" width="100px;" alt="Christian Riedel"/><br /><sub><b>Christian Riedel</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3ACielquan" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/morcef"><img src="https://avatars.githubusercontent.com/u/15701746?v=4?s=100" width="100px;" alt="morcef"/><br /><sub><b>morcef</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Amorcef" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/alejandro-yousef"><img src="https://avatars.githubusercontent.com/u/93203189?v=4?s=100" width="100px;" alt="alejandro-yousef"/><br /><sub><b>alejandro-yousef</b></sub></a><br /><a href="#ideas-alejandro-yousef" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/exs-dwoodward"><img src="https://avatars.githubusercontent.com/u/166007669?v=4?s=100" width="100px;" alt="exs-dwoodward"/><br /><sub><b>exs-dwoodward</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=exs-dwoodward" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Alwasser" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://galarzaa.com"><img src="https://avatars.githubusercontent.com/u/12865379?v=4?s=100" width="100px;" alt="Allan Galarza"/><br /><sub><b>Allan Galarza</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3AGalarzaa90" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
