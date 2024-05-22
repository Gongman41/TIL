
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 웹 페이지의 URL
url = 'https://pedia.watcha.com/ko-KR/users/DgwxAeQYNxrMj/contents/movies/ratings'

# HTML을 가져옴
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

all_a_tags = soup.find_all('a')

# 모든 <a> 태그의 title 속성 값 가져오기
titles = [a['title'] for a in all_a_tags if 'title' in a.attrs]

# 결과 출력
for title in titles:
    print(title)


# import requests
# import json

# API_KEY = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZjA4ZjI1ZDJhOTljOTAwNGU5MGViNDg0NTNiYjJlNCIsInN1YiI6IjY2M2Q2NWMxNjM2NzllZjlhMGQ5ZTNjZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._ZVCz0YUwuPuoio-DtTn2384JSPeWPywopvxnwtJB_I"

# def get_movie_datas(movie_titles):
#     movie_data = []
#     people_data = []
#     people_set = set()  # 중복 방지를 위해 ID를 저장할 집합

#     headers = {
#         "accept": "application/json",
#         "Authorization": API_KEY,
#     }

#     for movie_title in movie_titles:
#         params = {
#             'query': movie_title,
#             'language': 'ko-KR'
#         }
#         url = f'https://api.themoviedb.org/3/search/movie'

#         response = requests.get(url, headers=headers, params=params)
#         movies = response.json()

#         for movie in movies.get('results', []):
#             movie_id = movie['id']
            
#             # Get credits data
#             credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
#             credits_response = requests.get(credits_url, headers=headers)
#             credits = credits_response.json()

#             # Process cast data
#             cast = sorted(credits.get('cast', []), key=lambda x: x['popularity'], reverse=True)[:5]
#             cast_ids = [c['id'] for c in cast]
#             for c in cast:
#                 if c['id'] not in people_set:
#                     people_set.add(c['id'])
#                     people_data.append({
#                         'id': c['id'],
#                         'name': c['name'],
#                         'poster_path': c.get('profile_path'),
#                         'character': c.get('character'),
#                     })

#             # Process crew data
#             crew = [c for c in credits.get('crew', []) if 'producer' in c.get('job', '').lower()]
#             top_crew = sorted(crew, key=lambda x: x['popularity'], reverse=True)[:5]
#             crew_ids = [c['id'] for c in top_crew]
#             for c in top_crew:
#                 if c['id'] not in people_set:
#                     people_set.add(c['id'])
#                     people_data.append({
#                         'id': c['id'],
#                         'name': c['name'],
#                         'poster_path': c.get('profile_path'),
#                         'job': c.get('job'),
#                     })

#             movie_info = {
#                 "model": "movies.movie",  # 모델 경로 지정
#                 "pk": movie_id,
#                 "fields": {
#                     'title': movie.get('title'),
#                     'release_date': movie.get('release_date'),
#                     'popularity': movie.get('popularity'),
#                     'vote_count': movie.get('vote_count'),
#                     'vote_average': movie.get('vote_average'),
#                     'overview': movie.get('overview'),
#                     'poster_path': movie.get('poster_path'),
#                     'genres': movie.get('genre_ids'),
#                     'cast': cast_ids,
#                     'crew': crew_ids
#                 }
#             }

#             movie_data.append(movie_info)

#     with open("movie_data.json", "w", encoding="utf-8") as movie_file:
#         json.dump(movie_data, movie_file, indent=2, ensure_ascii=False)

#     with open("people_data.json", "w", encoding="utf-8") as people_file:
#         json.dump(people_data, people_file, indent=2, ensure_ascii=False)

# movie_titles = [
#     "노인을 위한 나라는 없다", "우리도 사랑일까", "안티크라이스트", "늑대아이", "빅 피쉬", "업", "레볼루셔너리 로드", "마더", "조디악", "바스터즈: 거친 녀석들",
#     "퍼스널 쇼퍼", "반지의 제왕 왕의 귀환", "피아니스트", "그랜드 부다페스트 호텔", "지구 최후의 밤", "폭스캐처", "로제타", "파이트 클럽", "덩케르크", "자마",
#     "멜랑콜리아", "데어 윌 비 블러드", "양들의 침묵", "보이후드", "컨택트", "릴리 슈슈의 모든 것", "비포 선셋", "버닝", "킬 빌 - 1부", "킬 빌 - 2부",
#     "월-E", "황해", "미스트", "인어공주", "사랑니", "브로크백 마운틴", "블루 재스민", "셰임", "비포 미드나잇", "사랑을 카피하다",
#     "만추", "씨민과 나데르의 별거", "파수꾼", "더 폴: 오디어스와 환상의 문", "킬러들의 도시", "유전", "인 디 에어", "스토리텔링", "공기인형", "시저는 죽어야 한다",
#     "생선 쿠스쿠스", "밤의 해변에서 혼자", "행복", "한여름의 판타지아", "닉슨", "미드소마", "언브레이커블", "엑스맨: 데이즈 오브 퓨처 패스트", "그녀", "타짜", "블루 발렌타인",
#     "캐빈 인 더 우즈", "색, 계", "아름다운 직업", "빅 쇼트", "우리들", "조지아", "클라커즈", "더 포스트", "포드 V 페라리", "프랑스", "나의 성생활: 나는 어떻게 싸웠는가","여고괴담 두번째 이야기", "자객 섭은낭", "러브 액츄얼리", "비몽", "사랑도 통역이 되나요?", "자유의 언덕", "휴고", "세 번째 살인", "환상의 그대", "폭스파이어", "모스트 원티드 맨", "미쓰 홍당무", "박치기", "삼거리극장", "경계도시2", "퐁네프의 연인들", "그을린 사랑", "파고", "뜨거운 녀석들", "아무도 머물지 않았다",
#     "스파이 브릿지", "디센트", "더 랍스터", "스카우트", "추격자", "어톤먼트", "스테이트 오브 플레이", "어벤져스: 인피니티 워", "맨 온 와이어", "씨 인사이드", "당신얼굴 앞에서", "레디 플레이어 원", "남한산성",
#     "스캔들 - 조선남녀상열지사", "그녀를 믿지 마세요", "판타스틱 플래닛", "여자는 남자의 미래다", "베오울프", "광해", "왕이 된 남자", "찰리와 초콜릿 공장", "월레스와 그로밋: 거대 토끼의 저주", "누구의 딸도 아닌 해원", "미스 리틀 선샤인", "아티스트", "오아시스", "목소리의 형태", "나", "다니엘 블레이크", "시라노; 연애조작단", "인트로덕션", "베를린", "남영동1985", "사이비", "스타워즈: 깨어난 포스", "인크레더블 2", "보리밭을 흔드는 바람", "제이슨 본", "브로드웨이를 쏴라", "미나리", "레버넌트: 죽음에서 돌아온 자", "스타트렉 다크니스", "데쓰 프루프",
#     "내 아내의 모든 것", "더 그레이", "웨이 백", "스플라이스", "블랙북", "해프닝", "극한직업",
#     "볼트", "유령신부", "악마는 프라다를 입는다", "우아한 세계", "스위니 토드", "레미제라블", "인디아나 존스: 크리스탈 해골의 왕국", "실미도", "괴물의 아이", "캐리비안의 해적: 세상의 끝에서", "패션 오브 크라이스트", "어메이징 스파이더맨", "어벤져스: 에이지 오브 울트론", "완벽한 타인", "터미네이터 3: 라이즈 오브 더 머신", "토끼 울타리", "쇼걸",
#     "투모로우", "체실 비치에서",
#     "퀵", "스파이더맨 3", "서핑업", "동창생", "아웃레이지", "모범시민", "스피드 레이서", "마이 블루베리 나이츠", "즐거운 인생", "매트릭스 3 - 레볼루션", "토르: 천둥의 신", "도가니", "늑대소년", "명량", "미녀는 괴로워", "7번방의 선물", "화려한 휴가", "트랜스포머: 패자의 역습", "트랜스포머 3", "지.아이.조: 전쟁의 서막", "그림 형제: 마르바덴 숲의 전설", "투 가이즈", "마음이…", "10억", "26년", "오스트레일리아", "황진이", "R2B: 리턴 투 베이스", "오! 마이 보스!",
#     "D-WAR", "둠", "투사부일체", "가문의 위기", "가문의 부활", "한반도", "쏜다", "오싹한 연애", "티스(영화)", "연평해전", "수어사이드 스쿼드", "싱크홀", "국가부도의 날", "300", "라스트 갓파더", "배틀쉽", "여고괴담 5 - 동반자살", "데스 센텐스", "브레이킹 던 part2", "나탈리", "7광구", "파괴자들", "누가 그녀와 잤을까?"

# ]
# get_movie_datas(movie_titles)