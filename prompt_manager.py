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

categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

def show_menu():   
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")

def add_prompt():

    print("===== 프롬프트 추가 =====")


    title = input("제목을 입력하세요: ")

    while title == "":
        print("제목은 비워둘 수 없습니다.")
        title = input("제목을 입력하세요: ")


    content = input("내용을 입력하세요: ")

    while content == "":
        print("내용은 비워둘 수 없습니다.")
        content = input("내용을 입력하세요: ")


    while True:
        print("카테고리를 선택하세요.")

        for i, category in enumerate(categories, start=1):
            print(i, category)

        print("7. 직접 입력")

        category_choice = input("카테고리 번호를 입력하세요: ")

        if category_choice == "7":
            category = input("새 카테고리를 입력하세요: ")

            if category != "":
                break

            print("카테고리는 비워둘 수 없습니다.")

        elif category_choice in ["1", "2", "3", "4", "5", "6"]:
            category_index = int(category_choice) - 1
            category = categories[category_index]
            break

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")
            

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_list():
    print("===== 프롬프트 목록 =====")

    for i, prompt in enumerate(prompts, start=1):
        print(i, prompt["title"], "[", prompt["category"], "]")

def show_by_category():
    print("===== 카테고리별 조회 =====")

    for i, category in enumerate(categories, start=1):
        print(i, category)

    choice = input("카테고리 번호를 입력하세요: ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        category_index = int(choice) - 1
        selected_category = categories[category_index]

        print(f"===== {selected_category} 프롬프트 =====")

        found = False

        for i, prompt in enumerate(prompts, start=1):
            if prompt["category"] == selected_category:
                print(i, prompt["title"])

                found = True

        if not found:
            print("해당 카테고리에 프롬프트가 없습니다.")

    else:
        print("잘못된 번호입니다.")

def search_prompt():
    print("===== 프롬프트 검색 =====")

    keyword = input("검색할 키워드를 입력하세요: ")

    if keyword == "":
        print("검색어를 비워둘 수 없습니다.")
        return

    found = False

    for i, prompt in enumerate(prompts, start=1):
        if keyword in prompt["title"] or keyword in prompt["content"]:
            print(
                i,
                prompt["title"],
                "[", prompt["category"], "]"
            )
            found = True

    if not found:
        print("검색 결과가 없습니다.")

def show_detail():
    print("===== 프롬프트 상세 보기 =====")

    choice = input("프롬프트 번호를 입력하세요: ")

    if not choice.isdigit():
        print("잘못된 번호입니다.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]

    print("제목:", prompt["title"])
    print("카테고리:", prompt["category"])

    if prompt["favorite"]:
        print("즐겨찾기: ⭐")
    else:
        print("즐겨찾기: ☆")

    print("내용:", prompt["content"])

while True:
    show_menu()

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "3":
        show_by_category()
    elif choice == "4":
        search_prompt()
    elif choice == "5":
        show_detail()
    elif choice == "6":
        print("즐겨찾기 관리를 선택했습니다.")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 번호입니다.")
