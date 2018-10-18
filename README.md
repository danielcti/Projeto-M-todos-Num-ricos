# Projeto de Metodos Numericos - IF816EC

Todas as aplicações dos Métodos Numéricos feitos por Daniel Cavalcanti (dpc2@cin.ufpe.br) utilizando Python

## Informações Gerais

Essas instruções irão ajudar em como compilar e executar o código presente neste repositório.

### Pré-requisitos

Para rodar este programa você deve estar em um ambiente Linux e com a biblioteca Simpy e MatplotLib instaladas em sua máquina. Caso você não tenha entre nos links abaixo.
```
https://docs.sympy.org/latest/install.html#installation
https://matplotlib.org/users/installing.html

```

### Executando o código

Assim, quando quiser executá-lo, com todas as dependências devidamente instaladas, você deve rodar o comando abaixo, na qual input.txt é um arquivo texto com as entradas desejadas.
```
$ python3 metodos.py < input.txt
```

## Como o programa funciona

O arquivo txt que será lido tem que iniciar com 1, caso se deseje plotar os gráficos, ou 0, caso contrário.<br />
A próxima linha contém um /// para indicar que o programa iniciará.<br />
As próximas linhas serão os métodos desejados com seus respectivos parâmetros.<br />
E para indicar que as entradas acabaram deve ter um /// na ultima linha.
<br /> <br />
Nos métodos de Euler, Euler Inverso, Euler Aprimorado e Runge Kutta as linhas serão assim:

```
nome_do_metodo t0 Y(t0) h(o tamanho do passo) n(número de iterações) (dF(y,t)/dt)
```
Nos métodos Adams Bashforth, Adams Multon e Formula de Diferenciação Inversa obtendo os valores iniciais por métodos anteriores as linhas serao assim:

```
nome_do_metodo t0 Y(t0) h(o tamanho do passo) n(número de iterações) (dF(y,t)/dt) grau
```
E nos métodos Adams Bashforth, Adams Multon e Formula de Diferenciação Inversa por lista de valores iniciais as linhas serão assim:

```
nome_do_metodo (grau-1 valores de y) t0 h(o tamanho do passo) n(número de iterações) (dF(y,t)/dt) grau
```
## Exemplo do arquivo de entrada
```
1
///
euler 0 0 0.1 20 1-t+4*y
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
adam_bashforth_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
///
```