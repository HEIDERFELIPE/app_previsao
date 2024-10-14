 Previsão de Custos Iniciais de Franquias com Regressão Linear

Este projeto utiliza a biblioteca Streamlit para criar uma aplicação web simples que permite a visualização e a previsão de custos iniciais de franquias. A previsão é realizada através de um modelo de regressão linear, treinado com dados históricos de franquias.

Funcionalidades:

Carregamento de Dados: Os dados são carregados a partir do arquivo CSV 'slr12.csv', onde cada linha representa uma franquia e as colunas correspondem à frequência anual e ao custo inicial.
Visualização de Dados: Os primeiros 10 registros do DataFrame são exibidos em uma tabela para uma rápida análise dos dados.
Gráfico de Dispersão: Um gráfico de dispersão mostra a relação entre a frequência anual e o custo inicial das franquias, com a linha de regressão sobreposta para visualizar a tendência.
Previsão: O modelo de regressão linear é utilizado para prever o custo inicial de uma franquia com base em sua frequência anual.
Tecnologias Utilizadas:

Streamlit: Biblioteca Python para criar aplicações web interativas.
Pandas: Biblioteca para manipulação e análise de dados.
Scikit-learn: Biblioteca para aprendizado de máquina, utilizada para implementar a regressão linear.
Matplotlib: Biblioteca para criação de gráficos.
Como Utilizar:

Clone o repositório: Clone este repositório para sua máquina local.
Instale as dependências: Execute pip install -r requirements.txt para instalar as bibliotecas necessárias.
Execute a aplicação: Execute o script Python principal para iniciar a aplicação Streamlit.
Observações:

A precisão da previsão depende da qualidade e quantidade dos dados utilizados para treinar o modelo.
Este é um exemplo simples de aplicação de aprendizado de máquina e pode ser expandido para incluir mais features e modelos mais complexos.
Exemplo de Uso:

Para utilizar a aplicação, o usuário pode inserir novos dados de frequência anual e o modelo fornecerá uma estimativa do custo inicial da franquia.

Potencialidades:

Tomada de Decisão: A aplicação pode auxiliar empreendedores a tomar decisões mais informadas sobre o investimento em franquias.
Análise de Mercado: A análise dos dados e dos resultados da previsão pode fornecer insights sobre o mercado de franquias.
Limitações:

Modelo Simples: O modelo de regressão linear é um modelo simples e pode não capturar todas as complexidades do mercado de franquias.
Dados Limitados: A precisão da previsão pode ser limitada pela quantidade e qualidade dos dados disponíveis.
Próximos Passos:

Melhoria do Modelo: Explorar outros modelos de aprendizado de máquina para obter melhores resultados.
Inclusão de Mais Features: Adicionar mais features aos dados, como setor, localização, etc., para melhorar a precisão da previsão.
Interface do Usuário: Melhorar a interface do usuário para facilitar a interação.
Contribuições:

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões para melhorar o projeto, por favor, abra um issue ou faça um pull request.

Agradecimentos:

Agradeço à comunidade open-source pelo desenvolvimento das bibliotecas utilizadas neste projeto.
