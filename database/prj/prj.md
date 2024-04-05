# django에서 데이터 사이언스 패키지 사용하기
- numpy: 빠르게 배열 연산
- pandas: 조작 및 분석
- matplotlib: 시각화(그래프)

- 문제 정의 - 데이터 수집(API,캐글) - 데이터 전처리(pandas) - 데이터 분석 - 결과 해석 및 공유(matplotlib )

- BytesIO

- 공식문서 살펴보기
  - 버전 맞춰서 키워드 검색
  - content 먼저
- django 오픈소스 분석
  - 브랜치에서 버전 찾아서 (4.2)
  - __init__.py 폴더 자체를 모듈처럼 사용할 수 있게 해주는 파일
    - 
  - 폴더에서 파일을 import(init으로 하면 폴더만  import). 폴더 내에 파일의 메서드를 import