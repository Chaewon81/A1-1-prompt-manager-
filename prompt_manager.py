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
    """메인 메뉴를 출력합니다."""
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")


def get_non_empty_input(message):
    """빈 입력을 허용하지 않고 값을 입력받습니다."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("입력값을 비워둘 수 없습니다.")


def add_prompt():
    """새로운 프롬프트를 추가합니다."""
    print("===== 프롬프트 추가 =====")

    title = get_non_empty_input("제목을 입력하세요: ")

    # 동일한 제목의 프롬프트 중복 방지
    while any(prompt["title"] == title for prompt in prompts):
        print("이미 같은 제목의 프롬프트가 있습니다.")
        title = get_non_empty_input("다른 제목을 입력하세요: ")

    content = get_non_empty_input("내용을 입력하세요: ")

    while True:
        print("카테고리를 선택하세요.")

        for i, category in enumerate(categories, start=1):
            print(i, category)

        print("7. 직접 입력")

        category_choice = input("카테고리 번호를 입력하세요: ").strip()

        if category_choice == "7":
            category = get_non_empty_input("새 카테고리를 입력하세요: ")

            if category not in categories:
                categories.append(category)
                print(f"새 카테고리 '{category}'가 추가되었습니다.")
            else:
                print("이미 존재하는 카테고리를 사용합니다.")

            break

        elif category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
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
    """전체 프롬프트 목록을 출력합니다."""
    print("===== 프롬프트 목록 =====")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        favorite_mark = "⭐" if prompt["favorite"] else "☆"

        print(
            i,
            favorite_mark,
            prompt["title"],
            "[", prompt["category"], "]"
        )


def show_by_category():
    """선택한 카테고리의 프롬프트만 출력합니다."""
    print("===== 카테고리별 조회 =====")

    for i, category in enumerate(categories, start=1):
        print(i, category)

    choice = input("카테고리 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 번호입니다.")
        return

    category_index = int(choice) - 1

    if category_index < 0 or category_index >= len(categories):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[category_index]

    print(f"===== {selected_category} 프롬프트 =====")

    found = False

    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected_category:
            favorite_mark = "⭐" if prompt["favorite"] else "☆"

            print(
                i,
                favorite_mark,
                prompt["title"]
            )

            found = True

    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")


def search_prompt():
    """제목 또는 내용에 포함된 키워드로 프롬프트를 검색합니다."""
    print("===== 프롬프트 검색 =====")

    keyword = get_non_empty_input("검색할 키워드를 입력하세요: ")

    # 영문 대소문자를 구분하지 않도록 변환
    keyword = keyword.lower()

    found = False

    for i, prompt in enumerate(prompts, start=1):
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            favorite_mark = "⭐" if prompt["favorite"] else "☆"

            print(
                i,
                favorite_mark,
                prompt["title"],
                "[", prompt["category"], "]"
            )

            found = True

    if not found:
        print("검색 결과가 없습니다.")


def show_detail():
    """선택한 프롬프트의 상세 정보를 출력합니다."""
    print("===== 프롬프트 상세 보기 =====")

    choice = input("프롬프트 번호를 입력하세요: ").strip()

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


def toggle_favorite():
    """프롬프트의 즐겨찾기 상태를 추가하거나 해제합니다."""
    print("===== 즐겨찾기 추가/해제 =====")

    choice = input("프롬프트 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("잘못된 번호입니다.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompts[index]["favorite"] = not prompts[index]["favorite"]

    if prompts[index]["favorite"]:
        print("⭐ 즐겨찾기에 추가되었습니다.")
    else:
        print("☆ 즐겨찾기에서 해제되었습니다.")


def show_favorites():
    """즐겨찾기로 설정된 프롬프트만 출력합니다."""
    print("===== 즐겨찾기 목록 =====")

    found = False

    for i, prompt in enumerate(prompts, start=1):
        if prompt["favorite"]:
            print(
                i,
                "⭐",
                prompt["title"],
                "[", prompt["category"], "]"
            )

            found = True

    if not found:
        print("즐겨찾기한 프롬프트가 없습니다.")


def favorite_menu():
    """즐겨찾기 관련 메뉴를 관리합니다."""
    while True:
        print("===== 즐겨찾기 관리 =====")
        print("1. 즐겨찾기 추가/해제")
        print("2. 즐겨찾기 목록")
        print("0. 돌아가기")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            toggle_favorite()

        elif choice == "2":
            show_favorites()

        elif choice == "0":
            break

        else:
            print("잘못된 번호입니다.")


# 메인 프로그램
while True:
    show_menu()

    choice = input("메뉴를 선택하세요: ").strip()

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
        favorite_menu()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 번호입니다.")