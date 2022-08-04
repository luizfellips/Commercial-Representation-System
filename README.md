# EXCEL AUTOMATIONS PROJECT

Construí este sistema para facilitar no preenchimento de planilhas de acordo com dados inseridos. Utilizei a biblioteca padrão de construção de GUIs do Python(Tkinter) e Pandas para análise e processamento da base de dados de planilhas em Excel.

### UTILIZANDO O PROGRAMA
- Insira o nome do arquivo a ser lido com sua respectiva extensão, .xlsx(o mesmo deve estar no mesmo formato dos arquivos na pasta _files, com suas 3 colunas respectivas, CÓDIGO, ESPECIFICAÇÃO e PREÇO)

- Insira a quantidade e o código do produto e aperte Enter ou o botão Adicionar, que a busca será realizada instantaneamente e o produto será mostrado no sistema.

- Você pode deletar um ou vários arquivos ao mesmo tempo, eles serão removidos do sistema antes de salvar.

- Por fim insira o nome do arquivo para ser salvo, com sua respectiva extensão(.xlsx) e aperte SALVAR, o arquivo ficará salvo na pasta saved_files.

- O código dos arquivos deve ser inserido da seguinte maneira: 
Se possuir apenas números: Digite apenas o número, sem nenhuma pontuação.
Se possuir letras e números: Digite da forma que está na tabela, mesmo se houver pontuações.


### COMO FUNCIONA
```
O programa lê o nome do arquivo inserido e o transforma em um DataFrame, que facilita sua manipulação e resgate de dados.
O DataFrame fica disponível enquanto o programa não é fechado ou até outro arquivo ser lido.
Todo código inserido será pesquisado por toda a base de informações do DataFrame, onde será resgatado sua especificação e preço.
Estes serão apresentados na visualização em árvore, no qual poderão ser selecionados e deletados se desejar.
Essas informações ainda não estão sendo preenchidas na planilha, seu armazenamento é feito em listas e tuplas e totalmente temporário.
No fim você insere o nome do arquivo para salvar, e clica no botão SALVAR, onde cada produto será inserido numa planilha
com suas respectivas colunas imediatamente e o arquivo ficará disponibilizado na pasta saved_files.
```
### Funcionalidades a serem adicionadas
- Criação de um arquivo temporário que guardará as informações sendo inseridas, em caso de fechamento acidental do aplicativo.
- 
