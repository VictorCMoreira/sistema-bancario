# Sistema de Conta Bancária

## Sobre

Um sistema de conta bancária que implementa três operações: depósito, saque e extrato.

## Saque

#### Regras

- O sistema permite apenas três saques;
- O valor do saque não pode ser negativo;
- O limite máximo para cada saque é de R$ 500,00;
- O saque não é permitido em caso de saldo insuficiente
  Para todas as três exceções o sistema emite uma mensagem informando que não foi possível realizar a operação.

## Depósito

#### Regra

- O valor do depósito não pode ser negativo

## Extrato

- Lista todos os saques e depósitos realizados
- Exibe, no final, o saldo atual da Conta
- Os valores são exibidos no formato R$ xxxx.xx
