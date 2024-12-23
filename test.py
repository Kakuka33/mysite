# ファイル名
file_name = "todo.txt"

# タスクを追加する関数
def add_task(file_name):
    print("タスクを追加するよ！")
    task = input("追加したいタスクを入力してね （終了するにはqを入力！）：")
    if task == "q":
        print("タスク追加キャンセルしたんやで")
    else:
        with open(file_name, "a") as f:
                f.write(task + "\n")
        print("タスクを追加したよ！")

# タスクを表示する関数
def show_coontents(file_name):
    print("タスク一覧を表示するよ！")
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            tasks = f.readlines()
            if tasks:
                for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")
    except FileNotFoundError:
            print("タスクまだ無いっぽいからどんどん追加しよ！")

# タスクを削除する関数
def delete_task(file_name):
    print("タスク一覧を表示するから削除したいものを選んでね！")
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            tasks = f.readlines()
            if tasks:
                for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")
    except FileNotFoundError:
            print("タスクまだ無いっぽいからどんどん追加しよ！")
    try:
        delete_task = int(input("削除したいタスクの番号を入力してね: "))
        if delete_task <0 or delete_task > len(tasks):
            print("そのタスクはないんだぜ！")

        deleted_task = tasks.pop(delete_task-1)
        print(f"{deleted_task.strip()}を削除したよ！")
        with open(file_name, "w", encoding='utf-8') as f:
            for task in tasks:
                    f.writelines(task)
    except ValueError:
            print("ちゃんと数字で入力してね！")



print("タスク管理アプリへようこそ！✨")

while True:
    print("\n [メニュー]")
    print("1: タスクを追加する")
    print("2: タスクを一覧表示する")
    print("3: タスクを削除する")
    print("q: 終了する")
    choice = input("選択肢を入力してね: ").strip()

    if choice == "1":
        add_task(file_name)

    elif choice == "2":
        show_coontents(file_name)    
    
    elif choice == "3":
        delete_task(file_name)
        
    elif choice.lower() == "q":
        print("お疲れ様ー、アプリを終了するよ！")
        break
    else:
        print("1か2かqで答えてちょ。")
    
