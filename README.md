# WEB SCRAPING
Projeto de Exemplo com MVVM e CRUDs
Este projeto de exemplo demonstra o uso do padrão de arquitetura MVVM (Model-View-ViewModel) para desenvolvimento de um aplicativo. O projeto possui implementações de CRUDs (Create, Read, Update, Delete) para operações de banco de dados, com foco especial em operações relacionadas a voos de companhias aéreas.

# Estrutura do Projeto
database_operations.py: Este módulo contém a lógica para interação com o banco de dados, incluindo operações de criação, leitura, atualização e exclusão de registros de voos.

webdriver_setup.py: Este módulo oferece uma função para configurar o driver do navegador Chrome, permitindo a inicialização e configuração do navegador para posterior raspagem de dados de sites de companhias aéreas.

CVC.py e Decolar.py: Esses arquivos contêm as implementações específicas para os sites CVC e Decolar, incluindo a extração de dados de voos e a inserção desses dados no banco de dados por meio da interface fornecida pelo módulo database_operations.

# README.md: Este arquivo fornece uma descrição geral do projeto, incluindo detalhes sobre a estrutura do projeto, arquivos incluídos e instruções básicas para uso e contribuição.

# Objetivo
O objetivo principal deste projeto é demonstrar uma implementação prática e básica do padrão MVVM juntamente com operações CRUD, com foco na coleta de dados de voos de companhias aéreas de sites como CVC e Decolar. O projeto serve como um guia para desenvolvedores interessados em compreender a implementação básica do padrão MVVM e operações CRUD em Python.