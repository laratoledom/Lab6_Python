# Laboratório 6 de Python: Eleições 2022

Sexto projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
_______________________________________________________________________________________________________________________________________________________________________

"O Brasil adota o sistema eleitoral majoritário de dois turnos e o critério de maioria absoluta nas suas eleições. Para ser eleito no primeiro turno, o candidato precisa obter mais da metade dos votos válidos (excluídos os votos em branco e os votos nulos). Caso contrário, os dois candidatos mais votados no primeiro turno irão compor o segundo turno da eleição.

Você foi contratado pelo Tribunal Superior Eleitoral (TSE) para fazer um programa que indique se houve um vencedor no primeiro turno das eleições de 2022 ou se será necessário a realização de um segundo turno. No caso de haver um vencedor, você deve indicar quem foi o vencedor. Já no caso em que um segundo turno é necessário, você deve indicar os dois candidatos que participarão do segundo turno, seguindo a ordem de número de votos (o mais votado será impresso primeiro). A impressão deve seguir os modelos abaixo.

Quando existe vencedor no primeiro turno:<br>
- "~nome_candidato_vencedor ~ <b>foi o vencedor da eleição</b>"

Quando há a necessidade de segundo turno:
- "<b>Haverá segundo turno entre:</b><br>
~ nome_primeiro_colocado ~ <br>
~ nome_segundo_colocado ~"

Além disso, o seu programa deve imprimir o total de votos e o total de votos válidos, respectivamente, seguindo o modelo abaixo:

"<b>Total de votos:</b> ~ total de votos ~<br>
<b>Votos válidos:</b> ~ número de votos válidos ~"

O TSE fornecerá para o seu programa a seguinte entrada:<br>
•	Uma linha com a quantidade n de candidatos da eleição;<br>
•	Uma lista com o nome dos n candidatos, sendo um nome por linha;<br>
•	Uma lista com n+2 valores inteiros, um por linha, sendo que a i-ésima linha representa a quantidade de votos recebidos pelo i-ésimo candidato, seguindo a ordem de leitura da lista de nomes. Os últimos dois valores representam a quantidade de votos brancos e nulos, respectivamente.
Você pode assumir que todos os candidatos receberam uma quantidade distinta de votos."
_______________________________________________________________________________________________________________________________________________________________________
<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.
