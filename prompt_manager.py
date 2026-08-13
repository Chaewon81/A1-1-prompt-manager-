prompts = [
    {
        "title": "영어회화 선생님",
        "content": "너는 영어회화 전문 선생님이야.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "축구 포스터 생성",
        "content": "축구 경기 포스터를 만들어줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "AI 학습 코치",
        "content": "너는 초등학생 학습을 도와주는 코치야.",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")

while True:
    show_menu()

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        print("프롬프트 추가를 선택했습니다.")
    elif choice == "2":
        print("프롬프트 목록을 선택했습니다.")
    elif choice == "3":
        print("카테고리별 조회를 선택했습니다.")
    elif choice == "4":
        print("프롬프트 검색을 선택했습니다.")
    elif choice == "5":
        print("프롬프트 상세 보기를 선택했습니다.")
    elif choice == "6":
        print("즐겨찾기 관리를 선택했습니다.")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 번호입니다.")


