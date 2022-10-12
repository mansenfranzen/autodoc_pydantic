![Autodoc Pydantic](https://raw.githubusercontent.com/mansenfranzen/autodoc_pydantic/main/docs/source/material/logo_black.svg)

[![PyPI version](https://img.shields.io/pypi/v/autodoc_pydantic?style=for-the-badge)](https://pypi.org/project/autodoc-pydantic/)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg?style=for-the-badge)

[![Master](https://img.shields.io/github/workflow/status/mansenfranzen/autodoc_pydantic/ci?style=for-the-badge)](https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/codecov/c/gh/mansenfranzen/autodoc_pydantic?style=for-the-badge)](https://app.codecov.io/gh/mansenfranzen/autodoc_pydantic)

[![Downloads](https://img.shields.io/pypi/dm/autodoc_pydantic?color=fe7d37&style=for-the-badge)](https://pypistats.org/packages/autodoc-pydantic)<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-29-orange.svg?style=for-the-badge)](#contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


You love [pydantic](https://pydantic-docs.helpmanual.io/) ❤ and you want to
document your models and configuration settings with [sphinx](https://www.sphinx-doc.org/en/master/)?

Perfect, let's go. But wait, sphinx' [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
does not integrate too well with pydantic models 😕.

Don't worry - just `pip install autodoc_pydantic` ☺.

## Features

- 💬 provides default values, alias and constraints for model fields
- 🔗 adds hyperlinks between validators and corresponding fields
- 📃 includes collapsable model json schema
- 🏄 natively integrates with autodoc and autosummary extensions
- 📎 defines explicit pydantic prefixes for models, settings, fields, validators and model config
- 📋 shows summary section for model configuration, fields and validators
- 👀 hides overloaded and redundant model class signature
- 📚 sorts fields, validators and model config within models by type
- 🍀 Supports `pydantic >= 1.5.0` and `sphinx >= 3.4.0`

### Comparison between autodoc sphinx and autodoc pydantic

[![Comparison](https://raw.githubusercontent.com/mansenfranzen/autodoc_pydantic/main/docs/source/material/example_comparison_v1.0.0.gif)](https://autodoc-pydantic.readthedocs.io/en/latest/examples.html#default-configuration)

To see those features in action, jump over to the [example documentation](https://autodoc-pydantic.readthedocs.io/en/stable/users/examples.html#default-configuration) to compare
the appearance of standard sphinx autodoc with *autodoc_pydantic*.

## Documentation

For more details, please visit the official [documentation](https://autodoc-pydantic.readthedocs.io/en/stable/):

- [Installation](https://autodoc-pydantic.readthedocs.io/en/stable/users/installation.html)
- [Configuration](https://autodoc-pydantic.readthedocs.io/en/stable/users/configuration.html)
- [Usage](https://autodoc-pydantic.readthedocs.io/en/stable/users/usage.html)
- [Examples](https://autodoc-pydantic.readthedocs.io/en/stable/users/examples.html)

## Acknowledgements

Thanks to great open source projects [sphinx](https://www.sphinx-doc.org/en/master/),
[pydantic](https://pydantic-docs.helpmanual.io/) and
[poetry](https://python-poetry.org/) (and so many more) ❤ in addition to the following contributors:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/mansenfranzen"><img src="https://avatars.githubusercontent.com/u/18086180?v=4?s=100" width="100px;" alt="Franz Wöllert"/><br /><sub><b>Franz Wöllert</b></sub></a><br /><a href="#maintenance-mansenfranzen" title="Maintenance">🚧</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Documentation">📖</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Tests">⚠️</a> <a href="#content-mansenfranzen" title="Content">🖋</a></td>
      <td align="center"><a href="https://github.com/TheBeardedBerserkr"><img src="https://avatars.githubusercontent.com/u/32272268?v=4?s=100" width="100px;" alt="TheBeardedBerserkr"/><br /><sub><b>TheBeardedBerserkr</b></sub></a><br /><a href="#ideas-TheBeardedBerserkr" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center"><a href="https://github.com/vlcinsky"><img src="https://avatars.githubusercontent.com/u/635911?v=4?s=100" width="100px;" alt="Jan Vlčinský"/><br /><sub><b>Jan Vlčinský</b></sub></a><br /><a href="#security-vlcinsky" title="Security">🛡️</a></td>
      <td align="center"><a href="https://github.com/antvig"><img src="https://avatars.githubusercontent.com/u/25105210?v=4?s=100" width="100px;" alt="antvig"/><br /><sub><b>antvig</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aantvig" title="Bug reports">🐛</a> <a href="#userTesting-antvig" title="User Testing">📓</a></td>
      <td align="center"><a href="https://roguh.com"><img src="https://avatars.githubusercontent.com/u/6373447?v=4?s=100" width="100px;" alt="Hugo O Rivera"/><br /><sub><b>Hugo O Rivera</b></sub></a><br /><a href="#ideas-roguh" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center"><a href="https://github.com/ybnd"><img src="https://avatars.githubusercontent.com/u/31547038?v=4?s=100" width="100px;" alt="yura bondarenko"/><br /><sub><b>yura bondarenko</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aybnd" title="Bug reports">🐛</a> <a href="#userTesting-ybnd" title="User Testing">📓</a></td>
      <td align="center"><a href="http://tahoward.github.io"><img src="https://avatars.githubusercontent.com/u/547570?v=4?s=100" width="100px;" alt="Trevor Howard"/><br /><sub><b>Trevor Howard</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Atahoward" title="Bug reports">🐛</a> <a href="#userTesting-tahoward" title="User Testing">📓</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/thomas-pedot"><img src="https://avatars.githubusercontent.com/u/86731212?v=4?s=100" width="100px;" alt="thomas-pedot"/><br /><sub><b>thomas-pedot</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Athomas-pedot" title="Bug reports">🐛</a> <a href="#userTesting-thomas-pedot" title="User Testing">📓</a></td>
      <td align="center"><a href="https://github.com/matutter"><img src="https://avatars.githubusercontent.com/u/2701379?v=4?s=100" width="100px;" alt="Mat Utter"/><br /><sub><b>Mat Utter</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Amatutter" title="Bug reports">🐛</a> <a href="#userTesting-matutter" title="User Testing">📓</a></td>
      <td align="center"><a href="https://github.com/davidchall"><img src="https://avatars.githubusercontent.com/u/1804856?v=4?s=100" width="100px;" alt="David C Hall"/><br /><sub><b>David C Hall</b></sub></a><br /><a href="#ideas-davidchall" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-davidchall" title="User Testing">📓</a></td>
      <td align="center"><a href="https://yoshanuikabundi.me"><img src="https://avatars.githubusercontent.com/u/28590748?v=4?s=100" width="100px;" alt="Josh A. Mitchell"/><br /><sub><b>Josh A. Mitchell</b></sub></a><br /><a href="#ideas-Yoshanuikabundi" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=Yoshanuikabundi" title="Tests">⚠️</a></td>
      <td align="center"><a href="https://github.com/goroderickgo"><img src="https://avatars.githubusercontent.com/u/17296713?v=4?s=100" width="100px;" alt="Roderick Go"/><br /><sub><b>Roderick Go</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=goroderickgo" title="Tests">⚠️</a></td>
      <td align="center"><a href="https://github.com/lilyminium"><img src="https://avatars.githubusercontent.com/u/31115101?v=4?s=100" width="100px;" alt="Lily Wang"/><br /><sub><b>Lily Wang</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=lilyminium" title="Documentation">📖</a> <a href="#content-lilyminium" title="Content">🖋</a></td>
      <td align="center"><a href="https://github.com/j-carson"><img src="https://avatars.githubusercontent.com/u/44308120?v=4?s=100" width="100px;" alt="j-carson"/><br /><sub><b>j-carson</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aj-carson" title="Bug reports">🐛</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=j-carson" title="Code">💻</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=j-carson" title="Tests">⚠️</a></td>
    </tr>
    <tr>
      <td align="center"><a href="http://imada.sdu.dk/~jlandersen/"><img src="https://avatars.githubusercontent.com/u/6465735?v=4?s=100" width="100px;" alt="Jakob Lykke Andersen"/><br /><sub><b>Jakob Lykke Andersen</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=jakobandersen" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/astrojuanlu"><img src="https://avatars.githubusercontent.com/u/316517?v=4?s=100" width="100px;" alt="Juan Luis Cano Rodríguez"/><br /><sub><b>Juan Luis Cano Rodríguez</b></sub></a><br /><a href="#content-astrojuanlu" title="Content">🖋</a></td>
      <td align="center"><a href="https://github.com/nchaly"><img src="https://avatars.githubusercontent.com/u/2665273?v=4?s=100" width="100px;" alt="Mikalai Chaly"/><br /><sub><b>Mikalai Chaly</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Anchaly" title="Bug reports">🐛</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=nchaly" title="Tests">⚠️</a></td>
      <td align="center"><a href="https://github.com/StigKorsnes"><img src="https://avatars.githubusercontent.com/u/10085536?v=4?s=100" width="100px;" alt="Stig Korsnes"/><br /><sub><b>Stig Korsnes</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3AStigKorsnes" title="Bug reports">🐛</a> <a href="#ideas-StigKorsnes" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center"><a href="https://github.com/iliakur"><img src="https://avatars.githubusercontent.com/u/899591?v=4?s=100" width="100px;" alt="Ilia Kurenkov"/><br /><sub><b>Ilia Kurenkov</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Ailiakur" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://orcid.org/my-orcid?orcid=0000-0002-5470-1676"><img src="https://avatars.githubusercontent.com/u/3826210?v=4?s=100" width="100px;" alt="Grzegorz Bokota"/><br /><sub><b>Grzegorz Bokota</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3ACzaki" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://github.com/jgunstone"><img src="https://avatars.githubusercontent.com/u/21370980?v=4?s=100" width="100px;" alt="jgunstone"/><br /><sub><b>jgunstone</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Ajgunstone" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/iwyrkore"><img src="https://avatars.githubusercontent.com/u/92745880?v=4?s=100" width="100px;" alt="iwyrkore"/><br /><sub><b>iwyrkore</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=iwyrkore" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/spacemanspiff2007"><img src="https://avatars.githubusercontent.com/u/10754716?v=4?s=100" width="100px;" alt="spacemanspiff2007"/><br /><sub><b>spacemanspiff2007</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aspacemanspiff2007" title="Bug reports">🐛</a> <a href="#ideas-spacemanspiff2007" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center"><a href="https://luke.hsiao.dev"><img src="https://avatars.githubusercontent.com/u/7573542?v=4?s=100" width="100px;" alt="Luke Hsiao"/><br /><sub><b>Luke Hsiao</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Alukehsiao" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://github.com/nickeldan"><img src="https://avatars.githubusercontent.com/u/21210592?v=4?s=100" width="100px;" alt="Daniel Walker"/><br /><sub><b>Daniel Walker</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Anickeldan" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://t.me/pipeknight"><img src="https://avatars.githubusercontent.com/u/34810566?v=4?s=100" width="100px;" alt="Evgeniy Lupashin"/><br /><sub><b>Evgeniy Lupashin</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3APipeKnight" title="Bug reports">🐛</a></td>
      <td align="center"><a href="http://janhendrikewers.uk/"><img src="https://avatars.githubusercontent.com/u/12383029?v=4?s=100" width="100px;" alt="Jan-Hendrik Ewers"/><br /><sub><b>Jan-Hendrik Ewers</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aiwishiwasaneagle" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Asneakers-the-rat" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center"><a href="http://charlie.machalow.com"><img src="https://avatars.githubusercontent.com/u/5749838?v=4?s=100" width="100px;" alt="Charles Machalow"/><br /><sub><b>Charles Machalow</b></sub></a><br /><a href="#question-csm10495" title="Answering Questions">💬</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
