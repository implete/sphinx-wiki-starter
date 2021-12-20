# Sphinx Wiki starter

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- start index -->
## Introduction

[Sphinx][] based template for building documentation or start a digital garden. Supports Markdown. 

### Requirements

* [Python][]
* [Sphinx][]
* [MyST Parser][myst-parser]
* [Furo][]
* [Sphinx Inline Tabs][sphinx-inline-tabs]
* [Markdown][] or [reStructuredText][] syntax knlowledge

## Getting Started

To work locally with this project, you'll have to follow the steps below.

### Prerequisites

1. [Install Python][python-install]
2. [Install Sphinx][sphinx-install]
3. [Install MyST Parser][myst-parser-install]
4. [Install Furo][furo-install]
4. [Install Sphinx Inline Tabs][sphinx-inline-tabs-install]

### Installation

1. Clone the repo
   ```shell
   git clone https://github.com/implete/sphinx-wiki-starter.git
   ```

2. Build the site
   ```shell
   make html
   ```

[python]: https://docs.python-guide.org/
[sphinx]: https://github.com/sphinx-doc/sphinx
[myst-parser]: https://github.com/executablebooks/MyST-Parser  
[furo]: https://github.com/pradyunsg/furo
[sphinx-inline-tabs]: https://github.com/pradyunsg/sphinx-inline-tabs
[markdown]: https://wikiless.org/wiki/Markdown?lang=en
[restructuredtext]: https://wikiless.org/wiki/ReStructuredText?lang=en
[python-install]: https://docs.python-guide.org/starting/installation/
[sphinx-install]: https://www.sphinx-doc.org/en/master/usage/installation.html
[myst-parser-install]: https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html#install-the-myst-parser
[furo-install]: https://pradyunsg.me/furo/quickstart/#quickstart
[sphinx-inline-tabs-install]: https://github.com/pradyunsg/sphinx-inline-tabs#installation
<!-- end index -->
