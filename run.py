import os

testFilePrefix="testFile"
testCommitPrefix="TEST-"
testCommits=[
1,2,3,4,2,4,6,3,5,3,6,2,3,4,2,3,8,2,3,5,
2,8,3,8,3,4,2,1,5,5,5,9,2,5,9,2,9,1,8,5,

5,8,6,7,1,8,7,5,9,4,8,2,8,7,5,1,6,5,3,5,
2,8,3,8,3,4,2,1,5,5,5,9,2,5,9,2,9,1,8,5,

4,6,3,5,3,6,2,3,4,2,3,8,2,3,5,4,2,1,5,5,
5,9,2,5,9,2,4,6,5,2,8,1,2,6,8,2,5,8,6,6,

9,2,4,5,9,8,4,6,2,5,5,8,4,7,4,9,5,8,1,3,
5,8,6,7,1,8,7,5,9,4,8,2,8,7,5,1,6,5,3,5,

2,4,8,2,5,6,2,1,5,6,1,5,3,5,1,5,6,4,2,6,
9,2,4,5,9,8,4,6,2,5,5,8,4,7,4,9,5,8,1,3,

5,8,6,7,1,8,7,5,9,4,8,2,8,7,5,1,6,5,3,5,
2,8,3,8,3,4,2,1,5,5,5,9,2,5,9,2,9,1,8,5,
]
releaseBranch="release"
developBranch="develop"
ticketNameFileName="jiraRelease.txt"
commitHashFileName="commitHashes.txt"

#start program
os.system("cat startMessage")

#git init
os.system("git init")
os.system("git add .")
os.system("git commit -m 'init'")

#git init branch
os.system("git branch -M main")
os.system(f"git branch {releaseBranch}")
os.system(f"git branch {developBranch}")

#move to develop branch
os.system(f"git checkout {developBranch}")

#start commit
for i in range(len(testCommits)):
	count=testCommits[i]
	for j in range(count):
		os.system(f"ls -l > {testFilePrefix}_{i}_{j}")
		os.system("git add .")
		os.system(f"git commit -m '{testCommitPrefix}{i}({j+1}/{count})'")

#create searchTargetFile
targetCommitSum=0;
ticketNameFile=open(ticketNameFileName)
for i in range(len(testCommits)):
	if(random.random()>0.7): 
		ticketNameFile.write(f"{testCommitPrefix}{i}\n")
		targetCommitCount+=testCommits[i]
picks=ticketNameFile.readlines()
ticketNameFile.close()


#파일을 읽어서 git log --grep으로 검색하여 커밋 해시들을 파일에 저장.
grep = "git log --pretty=format:%H"
for pick in picks:
    pick=pick.strip()
    grep+=(f" --grep={pick}")
os.system(grep+"> "+commitHashFileName)

#커밋 해시를 담은 파일을 읽어오기
hashFile = open(commitFile)
hashs=hashFile.readlines()
hashFile.close()

#머지할 브랜치로 이동
os.system("git add .")
os.system("git commit -m 'create commitFile'")
os.system("git checkout "+releaseBranch)

#파일을 읽어서 git cherry-pick으로 커밋들을 머지.
cherry= ""
for hash in hashs:
    hash=hash.strip()
    cherry=hash+" "+cherry
cherry="git cherry-pick "+cherry
os.system("echo "+cherry)
os.system(cherry)








