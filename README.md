
# 🗂️ 나만의 프롬프트 관리 프로그램

AI 프롬프트를 체계적으로 저장하고 관리하는 Python 콘솔 프로그램입니다.  
텍스트 생성, 이미지 생성, 페르소나 등 다양한 카테고리로 프롬프트를 분류하고,  
키워드 검색과 즐겨찾기 기능으로 필요한 프롬프트를 빠르게 찾을 수 있습니다.

---

## 🚀 실행 방법

### 요구 사항
- Python 3.10 이상

### 실행

```bash
python main.py
```

---

## 📋 기능 목록

| 번호 | 기능 | 설명 |
|------|------|------|
| 1 | 프롬프트 추가 | 제목, 내용, 카테고리를 입력하여 새 프롬프트 등록 |
| 2 | 프롬프트 목록 | 저장된 모든 프롬프트를 번호, 제목, 카테고리, 즐겨찾기(⭐) 와 함께 출력 |
| 3 | 카테고리별 조회 | 카테고리를 선택하여 해당 카테고리의 프롬프트만 필터링 |
| 4 | 프롬프트 검색 | 키워드로 제목 또는 내용에서 프롬프트 검색 |
| 5 | 상세 보기 | 번호를 입력하여 프롬프트 전체 내용 확인 |
| 6 | 즐겨찾기 관리 | 즐겨찾기 추가/해제 및 즐겨찾기 목록 모아보기 |
| 0 | 종료 | 프로그램 종료 |

---

## 🗂️ 프롬프트 카테고리

| 카테고리 | 설명 |
|----------|------|
| 텍스트 생성 | 블로그 글, 카피라이팅, 요약 등 텍스트 작성용 프롬프트 |
| 이미지 생성 | Midjourney, DALL·E 등 이미지 생성 AI용 프롬프트 |
| 영상 생성 | Sora, Runway 등 영상 생성 AI용 프롬프트 |
| 페르소나 | 특정 역할이나 캐릭터를 부여하는 프롬프트 |
| 자동화 | 반복 작업 자동화를 위한 프롬프트 |
| 기타 | 위 카테고리에 속하지 않는 프롬프트 |

---

## 📁 프로젝트 구조

```
prompt-manager/
├── main.py        # 메인 실행 파일
├── .gitignore     # Git 제외 파일 설정
└── README.md      # 프로젝트 설명 파일
```

---

## 🛠️ 개발 환경

- **에디터**: Visual Studio Code 1.133.0
- **언어**: Python 3.14.6
- **버전 관리**: Git 2.55.0
- **OS**: Windows 11

---

## 📝 Git 커밋 이력

```
* 6b767ee (HEAD -> main) Update README
* 9396ec2 Add favorite management
* d0cf65e Add prompt detail view
* 1fa6185 Add prompt search
* 5fa4a9f Add category search
* a969c0b (feature/add-prompt) Add prompt creation
* 49ef975 Add prompt list
* 82060c5 Update gitignore
* bbf94f4 Add main menu
* 0e8e809 Add initial prompt data
* cdc8812 Initial project setup
```

---

## 👤 개발자 정보

- GitHub: [https://github.com/Chaewon81/A1-1-prompt-manager-]

---

### ✅ 스크린샷 1 - 개발 환경 설정


![실행화면](E:\코디세이\코디세이 과제\AI 활용\1\images\개발 환경 설정)

---

### ✅ 스크린샷 2 - 프로그램 실행 결과

![실행화면](E:\코디세이\코디세이 과제\AI 활용\1\images\프로그램 실행 결과)

---

### ✅ 스크린샷 3 - git log 결과

![실행화면](E:\코디세이\코디세이 과제\AI 활용\1\images\git log 결과)


