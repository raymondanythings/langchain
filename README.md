- LCEL : https://python.langchain.com/docs/expression_language/why

## RAG

### Retriveval

- langchain의 모듈
- 여러종류의 소스 데이터를 document loader를 통해 불러와 분할한다 ( Transform )
- 변환된 데이터를 임베딩한다 ( 임베딩 : 컴퓨터가 이해할 수 있는 숫자로 변환하는 작업 )
- 임베딩 과정은 많은 비용이 필요하기 때문에, 다양한 cache store를 활용할 수 있다.
-
