from task_manager.service import STask


def main():
    while True:
        print(
            "Меню\n"
            "1. Просмотр задач\n"
            "2. Добавление задачи\n"
            "3. Изменение задачи\n"
            "4. Удаление задачи\n"
            "5. Поиск задач\n"
            "0. Выход"
        )

        try:
            choice = int(input("Выберите действие: "))
            
            if choice == 0:
                break
            
            if choice == 1:
                print(
                    "1. Просмотр всех текущих задач\n"
                    "2. Просмотр задач по категориям"
                )
                sub_choice = int(input("Выберите действие: "))
                
                if sub_choice == 1:
                    print("Текущие задачи:")
                    print(STask.find_now_task())
                elif sub_choice == 2:
                    category = input("Введите категорию: ")
                    print(STask.find_task_by_category(category))
                else:
                    print("Неверный номер")

            elif choice == 2:
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                category = input("Введите категорию задачи: ")
                due_date = input("Введите срок выполнения (в формате YYYY-MM-DD): ")
                priority = input("Введите приоритет задачи (низкий, средний, высокий): ").lower()
                
                result = STask.add_task(title, description, category, due_date, priority)
                print(result)

            elif choice == 3:
                print(
                    "1. Редактирование существующей задачи\n"
                    "2. Отметка задачи как выполненной"
                )
                sub_choice = int(input("Выберите действие: "))
                
                if sub_choice == 1:
                    task_id = int(input("Введите ID задачи, которую хотите изменить: "))
                    new_title = input("Новое название задачи (или пропустите): ")
                    new_description = input("Новое описание задачи (или пропустите): ")
                    new_category = input("Новая категория задачи (или пропустите): ")
                    new_due_date = input("Новая дата выполнения задачи (или пропустите): ")
                    new_priority = input("Новый приоритет задачи (или пропустите): ")
                    
                    print(STask.edit_task(task_id, new_title, new_description, new_category, new_due_date, new_priority))
                elif sub_choice == 2:
                    task_id = int(input("Введите ID задачи, которую хотите отметить как выполненную: "))
                    print(STask.completed_task(task_id))
                else:
                    print("Неверный номер")

            elif choice == 4:
                task_id = int(input("Введите ID задачи, которую хотите удалить: "))
                STask.del_task(task_id)

            elif choice == 5:
                print("Поиск задач.")
                key = input("Введите ключевые слова (или оставьте пустым): ")
                category = input("Введите категорию (или оставьте пустым): ")
                status = input("Введите статус (или оставьте пустым): ")
                
                print(STask.search_task(key, category, status))
            else:
                print("Неверный номер")
        
        except ValueError:
            print("Неверный формат ввода! Пожалуйста, введите число.")


if __name__ == "__main__":
    print("Добро пожаловать в менеджер задач!")
    main()
