# ProjName: Git cherry-pick Test


### why
회사에서 CI/CD 관리를 하게 되었다. 지라 티켓을 커밋 메시지로 하여 푸시하고, 지라 티켓의 일부분만 골라서 머지할 수 있는 방법이 없을까 고민해 보게 되었다.
    
    
### Stack
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    
    
### Summary
0. 깃을 초기화하고, main,release,develop 세 개의 브랜치 생성한다.
1. develop 브랜치에서 수 백개의 커밋을 쌓는다.
2. 커밋을 70% 확률로 선택하여 커밋 메시지를 저장한다. (지라 티켓 번호 부분)
3. 2번에서 저장한 파일을 읽어, git log --grep으로 커밋 해시들을 얻고, 파일로 저장한다.
4. 3번에서 저장한 파일을 읽어 git cherry-pick으로 커밋들을 머지한다.
