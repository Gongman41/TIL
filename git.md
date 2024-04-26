git branch : 브랜치 목록 확인
git branch -r : 원격 저장소의 브랜치 목록 확인
git branch <브랜치 이름> : 새로운 브랜치 생성
git branch -d <브랜치 이름> : 병합된 브랜치만 삭제ㅐ가능
git branch -D <브랜치 이름> : 강제삭제 ( 병합되지않은 브랜치도 삭제가능)

작업환경 변경 - HEAD 변경
git switch <다른 브랜치 이름> : 다른 브랜치로 이동
git switch -c <브랜치 이름> : 브랜치를 새로 생성과 동시에 이동
git switch -c <브랜치 이름> <커밋 id> : 특정 커밋 기준으로 브랜치 생성과 동시에 이동
스위치하기전 working directory 파일이 모두 버전관리가 되고 있는지 확인
  - add commit 하고 이동.

가상환경과 브랜치 확인
$ git log --all --graph

git branch merge b
현재 브랜치를 b에 병합
해도 지금 브랜치는 일단 감.
덮어쓰기 복붙 

3-way Merge
각 브랜치의 커밋 두개와 공통조상 커밋 하나를 사용하여 병합
Fast-Foward(빨리감기)
머지 과정 없이 단순히 브랜치의 포인터가 이동
master에 변동사항이 없을때.

Merge Conflict
같은 파일의 같은 부분을 수정한 경우
그냥 지우고 저장하면 끝
db gitignore 걸어 놓고 fixture 사용

수정사항 생기면 
git restore README.md 
하면 가장 최근에 commit한 시점으로 다시 돌아감. add하기 전 진행

add 하고 난 다음에 파일 상태 되돌리는 법.
git rm -- cached trash.txt
 - 최초 커밋조차 없었을 떄
git restore --staged trash.txt

직전 커밋 수정
git commit --amend