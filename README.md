# Projeto Django Girls

## Objetivo do projeto
    Treinamento em django rest framework

## Passos iniciais
    - clonar repositório 
    - criar ambiente virtual 
    - acessar ambiente virtual
    - ir para a pasta raíz do projeto
    - rodar o comando : pip install -r requirements.txt

## Rodando o projeto
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
    
    O projeto estará funcionando no endereço:
    http://127.0.0.1:8000/

## Rodando testes
    - na raiz do projeto rode :
        coverage run manage.py test

## Criando uma aplicação
    - python3 manage.py startapp <nome_aplicação>
     -criar model 
     -criar serializer 
     -criar admin
     -criar o services
    - no arquivo settings da pasta projects colocar o nome da aplicação no "INSTALLED_APPS"
    
## Observações especiais
    -Error: That port is already in use.
        Usar o comando " sudo lsof -t -i tcp:8000 | xargs kill -9" para resolver.