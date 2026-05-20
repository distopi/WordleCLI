# WordleCLI

Este projeto foi desenvolvido em Python com o objetivo de demonstrar a aplicação prática de conceitos de **Clean Code**, modularização, tratamento de erros e otimização de estruturas de dados para portfólio.

---

## 🚀 Funcionalidades

- **Leitura Dinâmica:** As palavras do jogo são carregadas a partir de um arquivo de texto externo (`words.txt`), permitindo atualizar o vocabulário facilmente sem mexer no código.
- **Validação Robusta de Inputs:** Tratamento inteligente para entradas inválidas (números, caracteres especiais, múltiplos caracteres ou letras já escolhidas) sem quebrar a execução do programa.
- **Gerenciamento Eficiente de Estados:** Uso de estruturas otimizadas para controle de tentativas e exibição do progresso em tempo real.
- **Interface Limpa no Terminal:** Feedback visual imediato com emojis e formatação organizada para uma melhor experiência do usuário (UX).
- **Resiliência:** Tratamento de exceção para ausência do arquivo de configuração, garantindo um encerramento seguro e informativo do software.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3.10+
- **Módulos Nativos:** `random`, `sys`
- **Estruturas de Dados Avançadas:** Uso de `set()` para validação de buscas em tempo constante.
- **Boas Práticas de Engenharia:**
  - *Guard Clauses:* Redução do aninhamento de blocos `if/else`, tornando o fluxo linear e legível.
  - *Type Hinting:* Tipagem explícita de argumentos e retornos para maior clareza e manutenibilidade.
  - *Block Isolation (`__main__`):* Estruturação profissional que impede a execução acidental do script quando importado como módulo.

---

## 📦 Como Executar o Projeto

### Pré-requisitos
Ter o Python 3 instalado na sua máquina.

### Passo a Passo

1. Clone este repositório:
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Prepare o banco de palavras:
   Crie um arquivo chamado words.txt no mesmo diretório do script e adicione as palavras que deseja sortear (uma por linha). Exemplo:

3. Execute o jogo:
   python main.py
