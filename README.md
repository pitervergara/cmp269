# Interfaces Web
* ### Jupyter: https://localhost:8888 (senha cmp269)
* ### Solr: http://localhost:8986


---

# Como rodar

* Instale os requisitos (veja seção **Requisitos** abaixo)
* Clone esse repo: `git clone https://github.com/pitervergara/cmp269.git`
* Entre no folder: `cd cmp269`
* Inicialize os containers: `docker-compose up -d`
* Acesse os Jupyter (a **senha** é: _cmp269_) : https://localhost:8888
* Execute os notebooks em ordem (01, 02, 03)
Obs.: O notebook _01 - Install libs.ipynb_ instala pacotes python e depende de acesso à internet para isso. Variáveis _http_proxy_ e _https_proxy_ que estiverem definidas no console onde os containers foram inicializados serão propagadas para o container. Se for necessário, é possível definir essas variáveis manualmente no arquivo _docker-compose.yml_ ou diretamente na célula do notebook antes do comando `pip install` executado por ela.

## Requisitos
* [Instale o docker](https://www.docker.com/community-edition#/download)
* [Instale o docker-compose](https://docs.docker.com/compose/install/#install-compose)

