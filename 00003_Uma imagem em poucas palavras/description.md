Com `pandas` podemos fazer diferentes tipos de gráficos com poucas linhas de código. No exemplo anterior...

```python
emprego.plot.line(x="year")
```

....vemos como, utilizando os dados da nossa tabela `emprego`, fazemos um gráfico de linhas no qual nosso eixo x (também chamado de _abscissas_ ou _eixo horizontal_) é o `year`. Além disso, nosso eixo y (_ordenadas_ ou _eixo vertical_) inclui implicitamente as outras colunas numéricas como _series_, em nosso caso, `employment_rate_female` e `employment_rate_male`. Podemos dizer a mesma coisa mais explicitamente assim:

```python
emprego.plot.line(x="year", y=["employment_rate_female", "employment_rate_male"])
```

> Mas `pandas` não permite apenas fazer gráficos de linhas. Tente alterar os exemplos anteriores de `plot.line` para `plot.bar` em seu caderno e execute-os novamente. O que acontece?
