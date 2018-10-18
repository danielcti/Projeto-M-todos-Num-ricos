# Projeto de Metodos Numericos - IF816EC

Todas as aplicações dos Métodos Numéricos feitos por Daniel Cavalcanti (dpc2@cin.ufpe.br) utilizando Python.

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

Caso se queira plotar os gráficos o arquivo de entrada se iniciará com a palavra plot, nesse caso para cada gráfico que for gerado é necessário fechar ele para continuar a execução do programa.
<br />
Caso não seja necessário plotar os gráficos escreva a letra n na primeira linha. <br />
As próximas linhas serão os métodos desejados com seus respectivos parâmetros. Lembrando que precisa estar em função de 'y' e 't' e estar nos padrões da Sympy. ```ex: 1-t+4**y```<br />
E para indicar que as entradas acabaram deve ter um /// na ultima linha.


### Escolhendo o Método que será utilizado
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
### Exemplo do arquivo de entrada
```
plot
euler 0 0 0.1 20 1-t+4*y
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
adam_bashforth_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
///
```
As saídas serão salvas no arquivo output.txt, para o input.txt acima o output.txt gerado será assim:

### Exemplo do arquivo de saída
```
Metodo de Euler
y(0.00000) = 0.00000000
h = 0.10000
0 0.00000
1 0.10000000
2 0.23000000
3 0.40200000
4 0.63280000
5 0.94592000

Metodo Adams Bashforth
y(0.00) = 0.00000
h = 0.10
0 0.00000
1 0.10000
2 0.23000
3 0.40200
4 0.63280
5 1.00007

Metodo Adams Bashforth por Runge Kutta
y(0.00) = 0.00000
h = 0.10
0 0.00000
1 0.11720
2 0.27974
3 0.50991
4 0.84097
5 1.32252

///
```