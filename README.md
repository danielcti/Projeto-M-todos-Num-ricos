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

O arquivo txt que será lido tem que iniciar com 1, caso se deseje plotar os gráficos, ou 0, caso contrário.
A próxima linha contém um /// para indicar que o programa iniciará.
Com exceção dos Métodos Adams Bashforth, Adams Multon e Formula de Diferenciação Inversa as linhas serão da seguinte forma:

```
nome_do_metodo t0 Y(t0) h(o tamanho do passo) n(numero de iterações) dF(y,t)/dt(a própria função)
```
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
