## 분산 버전 관리시스템
- 변화를 기록하고 추적하는 것
- 각 버전은 이전 버전으로부터의 **변경사항**을 기록.
- 원본과 변경사항 파일 따로 생성 ->마지막 파일과 이전 변경사항만 남기기.

## 과정
- 중앙집중식: 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드,관리 힘듦, 중앙 서버에 문제시 큰일남
- 분산식: 버전을 여러 개의 복제된 저장소에 저장 밎 관리. 동시에 푸시할 경우 따로 깃이 알려줌
## 역할
- 코드의 버전관리
- 코드의 변경이력을 기록하고 혐업을 원활하게 하는 도구

## git의 영역
- work directory(wr직업중인 폴더)폴더 자체. init 으로 관리 선언
- staging area(변경사항 계속해서 기록)git add러 변경사항 기록,repository(변동사항들만 기록한 레포지터리
  ) commit으로 수정

## 레포지터리
-  버전이력과 파일들이 영구적으로 저장되는 영역
-  .git 폴더햣 ㅣㅐㅎ
-  git init\
-   git statius
-    git add startcamp02
-  git commit -m "20240111"
-  git config --global user.email "you@example.com"
-   git config --global user.name "Your Name"
- 그 전으로 돌아가기 위해 16진수 난수를 만들어 놓음
- $ git log

- 뭐 커밋하기 전에 클린한지 확인
``
 git status
On branch master
nothing to commit, working tree clean
``

- 커밋은 쉴때마다 add commit 하는 게 낫다. 나중엔 기능 완성할때마다.
ㅇㅇ

- 방금 커밋한 거 수정하는 법 `git commit --ammend`
`insert` `Esc``:wq`

-  git log --oneline

- 실제 작업물(working drictory), 버전을 기록_변경사항을 기록_묶어놓기(staging area)

- 지금까지 한 건 git을 local에 저장한 거.이걸 gitlab의 원격저장소에 저장. \

-  커밋하다가 집가기전에 푸시. 깃허브는 개인적으로 사용
-  깃랩 뉴프로젝트 = 뉴 리포지터리. 깃허브는 개인 저장소. 깃랩은 싸피 공용. URL에 속해있는 그룹 선택가능. user로 선택
-  README 체크해제.
-  git push origin master 입력 시 다시 로그인 요청 오는 이유. 브라우저랑 CLI에서 요청보내는 것은 별개. 브라우저에서 요청 <-> 내 컴퓨터에서 요청.
- CLI에서 드래그만 해도 복사가 됨

- 원격저장소 주소 복사 - git clone 주소. 별명말고 주소로 부르는 이유: 저장을 시켰던 컴퓨터의ㅏ .git 파일안에 별명 저장되어있기떄문에 주소로 불러옴. 이 때 받아온 URL이 자동으로 origin으로 저장
- clone 은 최초로 내려받을 때. 그 다음부터는 git remote -v
- 깃헙은 따로 연결. origin도 rename
- git add -> git commit -> git push -> 다른 컴퓨터로 이동 -> git pull gitlab master -> add commit push 반복
-  .git이 있는 서로 다른 폴더에 옮겨넣기 안됨.
-  아예 덮어씌워버리면 괜찮은거 아닌가? 
-  원격저장소도 해당 폴더의 .git에 저장됨
-  merge 시 Esc :wq
-  원격저장소 갱신 시 먼저 pull을 받아야 push가 가능.
-  서로 다른 파일일 경우 merge 시 크게 문제 없음. 한 파일에 담긴 데이터가 서로 다를 경우, 에디터 내에서 수정가능할 수도 있음
-  git으로 관리되는 폴더내부의 파일이더라도 복사 붙여넣기 가능
-  이름은 같지만 파일 내 내용이 다른 파일을 pull할 경우 commit하지 않은 상황에서는 충돌이 발생하지 않음. 애초에 pull도 안되는 듯.아닌가. 뭐 하여튼.