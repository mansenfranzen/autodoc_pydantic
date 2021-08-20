![Autodoc Pydantic](https://raw.githubusercontent.com/mansenfranzen/autodoc_pydantic/main/docs/source/material/logo_black.svg)

[![PyPI version](https://badge.fury.io/py/autodoc-pydantic.svg)](https://badge.fury.io/py/autodoc-pydantic)
![Master](https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/30a083d784f245a98a0d5e6857708cc8)](https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mansenfranzen/autodoc_pydantic&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/30a083d784f245a98a0d5e6857708cc8)](https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&utm_medium=referral&utm_content=mansenfranzen/autodoc_pydantic&utm_campaign=Badge_Coverage)
[![Documentation Status](https://readthedocs.org/projects/autodoc-pydantic/badge/?version=stable)](https://autodoc-pydantic.readthedocs.io/en/stable/?badge=stable) <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-11-orange.svg?style=flat-square)](#contributors-)
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

To see those features in action, jump over to the [example documentation](https://autodoc-pydantic.readthedocs.io/en/latest/examples.html#default-configuration) to compare
the appearance of standard sphinx autodoc with *autodoc_pydantic*.

## Documentation

For more details, please visit the official [documentation](https://autodoc-pydantic.readthedocs.io/en/latest/):

- [Installation](https://autodoc-pydantic.readthedocs.io/en/latest/installation.html)
- [Configuration](https://autodoc-pydantic.readthedocs.io/en/latest/configuration.html)
- [Usage](https://autodoc-pydantic.readthedocs.io/en/latest/usage.html)
- [Examples](https://autodoc-pydantic.readthedocs.io/en/latest/examples.html)

## Acknowledgements

Thanks to great open source projects [sphinx](https://www.sphinx-doc.org/en/master/),
[pydantic](https://pydantic-docs.helpmanual.io/) and
[poetry](https://python-poetry.org/) (and so many more) ❤ in addition to the following contributors:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/mansenfranzen"><img src="https://avatars.githubusercontent.com/u/18086180?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Franz Wöllert</b></sub></a><br /><a href="#maintenance-mansenfranzen" title="Maintenance">🚧</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Documentation">📖</a> <a href="https://github.com/mansenfranzen/autodoc_pydantic/commits?author=mansenfranzen" title="Tests">⚠️</a> <a href="#content-mansenfranzen" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/TheBeardedBerserkr"><img src="https://avatars.githubusercontent.com/u/32272268?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TheBeardedBerserkr</b></sub></a><br /><a href="#ideas-TheBeardedBerserkr" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/vlcinsky"><img src="https://avatars.githubusercontent.com/u/635911?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jan Vlčinský</b></sub></a><br /><a href="#security-vlcinsky" title="Security">🛡️</a></td>
    <td align="center"><a href="https://github.com/antvig"><img src="https://avatars.githubusercontent.com/u/25105210?v=4?s=100" width="100px;" alt=""/><br /><sub><b>antvig</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aantvig" title="Bug reports">🐛</a> <a href="#userTesting-antvig" title="User Testing">📓</a></td>
    <td align="center"><a href="https://roguh.com"><img src="https://avatars.githubusercontent.com/u/6373447?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hugo O Rivera</b></sub></a><br /><a href="#ideas-roguh" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/ybnd"><img src="https://avatars.githubusercontent.com/u/31547038?v=4?s=100" width="100px;" alt=""/><br /><sub><b>yura bondarenko</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Aybnd" title="Bug reports">🐛</a> <a href="#userTesting-ybnd" title="User Testing">📓</a></td>
    <td align="center"><a href="http://tahoward.github.io"><img src="https://avatars.githubusercontent.com/u/547570?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Trevor Howard</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Atahoward" title="Bug reports">🐛</a> <a href="#userTesting-tahoward" title="User Testing">📓</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/thomas-pedot"><img src="https://avatars.githubusercontent.com/u/86731212?v=4?s=100" width="100px;" alt=""/><br /><sub><b>thomas-pedot</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Athomas-pedot" title="Bug reports">🐛</a> <a href="#userTesting-thomas-pedot" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/matutter"><img src="https://avatars.githubusercontent.com/u/2701379?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mat Utter</b></sub></a><br /><a href="https://github.com/mansenfranzen/autodoc_pydantic/issues?q=author%3Amatutter" title="Bug reports">🐛</a> <a href="#userTesting-matutter" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/davidchall"><img src="https://avatars.githubusercontent.com/u/1804856?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David C Hall</b></sub></a><br /><a href="#ideas-davidchall" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-davidchall" title="User Testing">📓</a></td>
    <td align="center"><a href="https://yoshanuikabundi.me"><img src="https://avatars.githubusercontent.com/u/28590748?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Josh A. Mitchell</b></sub></a><br /><a href="#ideas-Yoshanuikabundi" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
