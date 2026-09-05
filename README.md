# Scholarship Eligibility Evaluator

Projeto desenvolvido para a disciplina de **Fundamentos de Testes de Software**, com o objetivo de aplicar testes automatizados e análise de mutação em uma aplicação simples de avaliação de bolsas de estudo.

O sistema avalia um candidato considerando:

- idade;
- GPA;
- frequência;
- conclusão das disciplinas obrigatórias;
- histórico disciplinar.

A suíte de testes foi desenvolvida com **pytest** e sua qualidade foi avaliada utilizando **mutmut**.

---

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem utilizada no projeto |
| pytest | Execução dos testes automatizados |
| mutmut | Análise de mutação |
| WSL / Ubuntu | Ambiente utilizado para executar o mutmut |

---

## Como executar os testes
1. Criar o ambiente virtual

No Ubuntu/WSL:

```
python3 -m venv .venv 
```

2. Ativar o ambiente

```
source .venv/bin/activate
```

3. Instalar as dependências

```
pip install -r requeriments.txt
```

4. Executar os testes

O comando principal para executar a suíte é:

```
python -m pytest
```

## Análise de mutação
A análise de mutação é realizada utilizando o mutmut.

Para executar:

```
mutmut run
```


Após a execução, os resultados podem ser consultados com:

```
mutmut results
```

e
```
mutmut browse
```


Para visualizar um mutante específico:

```
mutmut show NOME_DO_MUTANTE
```


Por exemplo:

```
mutmut show ScholarshipEligibilityEvaluator.x__validate_inputs__mutmut_2
```


Configuração do mutmut

O projeto utiliza o arquivo setup.cfg para indicar ao mutmut qual arquivo deve ser analisado.

O source_paths aponta para o arquivo que contém a implementação do sistema.

## Execução no Windows
O mutmut não possui suporte nativo para Windows. Por isso, a análise de mutação deve ser executada através do WSL/Ubuntu.

O código pode ser desenvolvido normalmente no VS Code no Windows e executado no ambiente Ubuntu.

```
cd ~/aps-fund-testes
source .venv/bin/activate
```

## Resultados 

A suíte final possui 30 testes automatizados, todos passando.

Na análise de mutação final foram gerados 84 mutantes, sem sobreviventes.

### Score de mutação de 100%.

A evolução da suíte e a análise dos mutantes são apresentadas com mais detalhes no relatório do projeto na pasta 'docs'.