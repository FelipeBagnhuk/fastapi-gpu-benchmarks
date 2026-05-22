# GPU Benchmark API 

Uma API REST desenvolvida em Python com FastAPI para fornecer a média de quadros por segundo (FPS) de placas de vídeo (GPUs) em diferentes resoluções (1080p, 1440p e 4K), utilizando como base de conhecimento os dados consolidados do Tom's Hardware.

## Objetivo do Projeto
O objetivo é centralizar dados de performance que hoje estão dispersos em artigos e tabelas extensas, permitindo que desenvolvedores ou entusiastas consultem rapidamente o potencial de entrega de uma GPU de forma estruturada.

## Arquitetura e Conceitos Aplicados
Para garantir que o projeto seja escalável e fácil de manter, a API foi desenhada utilizando os seguintes pilares:

1. **Orientação a Objetos Avançada:** - Uso de classes abstratas para definir contratos de processamento de dados.
   - Encapsulamento das regras de cálculo de médias e métricas de desempenho.
2. **FastAPI & Uvicorn:** Para exposição dos endpoints de forma rápida, performática e com documentação automática (Swagger).
3. **Persistência de Dados:** Integração com Banco de Dados para armazenar o catálogo de GPUs e seus respectivos números de benchmark.
4. **Camada de Serviço Separada:** A lógica de negócio (cálculos de FPS, filtros de resolução) fica completamente isolada das rotas da API.

## Planejamento dos Endpoints (Rotas)

- `GET /gpus` -> Retorna a lista de todas as placas de vídeo cadastradas.
- `GET /gpus/{id}` -> Retorna os detalhes de uma placa específica.
- `GET /gpus/{id}/performance` -> Retorna a média de FPS daquela GPU filtrada por resolução (`1080p`, `1440p`, `4k`).
- `POST /gpus` -> (Admin) Para inserção de novos dados de benchmark coletados do Tom's Hardware.

## Como o Processamento de OO foi Pensado
A inteligência do projeto está na forma como as resoluções são tratadas. Cada resolução possui um comportamento de estresse diferente no hardware. O sistema utiliza polimorfismo para aplicar modificadores de performance ou validações específicas dependendo se a requisição pede dados em Full HD ou em 4K Nativo.
