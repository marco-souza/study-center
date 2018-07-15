# Python Developer's Toolbox

Lista de ferramentas e dicas sobre todo o ambiente python de desenvolvimento.

## Gerenciando Pacotes em Python

- `pip` - Instalado por padrão da versão 3.4+
- `pip install {pkg_name}` - Instalar pacote
- `pip search {pkg_name}` - Pesquisa pacote na [Cheese Shop](https://pypi.org/)
- `pip freeze >> requirements.txt` - "Congela" a versão dos pacotes atuais usados no ambiente aplicação
- `pip install -r requirements.txt` - Instala dependências para rodar seu projeto

## Isolamento de ambientes de desenvolvimento

### Virtualenv e VirtualenvWrapper

Necessário para manter sua máquina organizada e seus projetos atualizados, sem conflito entre versões.

Instalação `virtualenv`:

- `pip install virtualenv`
- [PP]: criar pasta em `$HOME/.virtualenvs/` para organizar seu ambientes de desenvolvimento

Utilização:

- `virtualenv ~/.virtualenvs/project_name` - cria um **novo ambiente** chamado `project_name` na sua pasta de ambientes 😖 (could be better)

- `source ~/.virtualenvs/project_name/bin/activate` - ativa o ambiente `project_name` 😖 (could be better)

- `deactivate` - desativa o ambiente `project_name`

Para facilitar a interação com os ambientes, foi criado um utilitário chamado `virtualenvwrapper`.

Utilização:

- `workon meu_projeto` - ativa o ambiente `meu_projeto`
- `mkvirtualenv meu_projeto` - cria o ambiente `meu_projeto` e o ativa imediatamente na sia pasta `~/.virtualenvs/` 😎 Nice
- `cd ~/dev/meu_projeto && setvirtualenvproject` - define `~/dev/meu_projeto` como sua pasta de projeto, assim, quando for usado `workon meu_projeto`, você irá para a pasta do projeto 🤩 What a charm!
- `mkproject meu_projeto` - cria o **projeto** e **ambiente** `meu_projeto` e o ativa imediatamente, indo para a pasta correspondente. O projeto será criado dentro da pasta padrão de projetos (definita no setup) 🤩 What a charm!

Instação:

- `pip install virtualenvwrapper` - instala `virtualenvwrapper`
- Adicionar os seguints comandos no seu `~/.profile`:

```bash
...
export PROJECT_HOME="$HOME/dev" # define sua pasta padrão de projetos
source /usr/local/bin/virtualenvwrapper.sh # carrega virtualenvwrapper

```
