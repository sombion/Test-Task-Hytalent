from datetime import datetime
from task_manager.dao import TaskDAO
from task_manager.models import TaskModel


class STask:

    @staticmethod
    def add_task(title: str, description: str, category: str, due_date: str, priority: str) -> str:
        data = TaskDAO.all_task_json()

        task_id = int(data[-1]["id"]) + 1 if data else 1

        if not title:
            return "Название задачи не может быть пустым."
        if not description:
            return "Описание задачи не может быть пустым."
        if not category:
            return "Категория задачи не может быть пустой."
        if not due_date:
            return "Срок выполнения не может быть пустым."

        try:
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
            if due_date_obj < datetime.now():
                return "Дата не может быть в прошлом."
        except ValueError:
            return "Неверный формат даты. Используйте формат 'YYYY-MM-DD'."

        if priority not in ['низкий', 'средний', 'высокий']:
            return "Приоритет должен быть одним из: 'низкий', 'средний', 'высокий'."

        task = TaskModel(task_id, title, description, category, due_date, priority)
        data.append(task.get_dict())

        if TaskDAO.add_task_json(data):
            return f"Задача '{title}' успешно добавлена."
        return "Ошибка добавления задачи."

    @staticmethod
    def find_now_task() -> str:
        tasks = [task for task in TaskDAO.all_task_json() if task["status"] == "Не выполнена"]

        if not tasks:
            return "Задач нет."

        return "\n\n".join(TaskModel.get_str(task) for task in tasks)

    @staticmethod
    def find_task_by_category(category: str) -> str:
        tasks = [task for task in TaskDAO.all_task_json() if task["category"] == category]

        if not tasks:
            return "Задач в этой категории нет."

        return "\n\n".join(TaskModel.get_str(task) for task in tasks)

    @staticmethod
    def edit_task(
        task_id: int,
        title: str | None = None,
        description: str | None = None,
        category: str | None = None,
        due_date: str | None = None,
        priority: str | None = None
    ) -> str:
        tasks = TaskDAO.all_task_json()
        task_found = False

        for task in tasks:
            if task["id"] == task_id:
                task_found = True
                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                if category:
                    task["category"] = category
                if due_date:
                    try:
                        due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
                        if due_date_obj < datetime.now():
                            return "Дата не может быть в прошлом."
                    except ValueError:
                        return "Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
                    task["due_date"] = due_date
                if priority:
                    if priority not in ['низкий', 'средний', 'высокий']:
                        return "Приоритет должен быть одним из: 'низкий', 'средний', 'высокий'."
                    task["priority"] = priority

        if not task_found:
            return f"Задача с ID {task_id} не найдена."

        TaskDAO.add_task_json(tasks)
        return f"Задача с ID {task_id} успешно обновлена."

    @staticmethod
    def completed_task(task_id: int) -> str:
        tasks = TaskDAO.all_task_json()

        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "выполнена":
                    return f"Задача с ID {task_id} уже выполнена."
                task["status"] = "выполнена"
                TaskDAO.add_task_json(tasks)
                return f"Задача с ID {task_id} успешно выполнена."

        return f"Задача с ID {task_id} не найдена."

    @staticmethod
    def search_task(key: str = "", category: str = "", status: str = "") -> str:
        if not key and not category and not status:
            return "Вы не указали ни один из параметров для поиска."

        tasks = TaskDAO.all_task_json()
        matching_tasks = [
            task for task in tasks
            if (not key or key.lower() in task.get("title", "").lower() or key.lower() in task.get("description", "").lower()) and
               (not category or task.get("category") == category) and
               (not status or task.get("status") == status)
        ]

        if not matching_tasks:
            return "Подходящих задач не найдено."

        return "\n\n".join(TaskModel.get_str(task) for task in matching_tasks)

    @staticmethod
    def del_task(task_id: int) -> str:
        if not TaskDAO.find_task_by_id_json(task_id):
            return "Задача с указанным ID не найдена."

        tasks = TaskDAO.all_task_json()
        updated_tasks = [task for task in tasks if int(task['id']) != task_id]

        if TaskDAO.del_task_id_json(updated_tasks):
            return f"Задача с ID {task_id} успешно удалена."
        return "Ошибка при удалении задачи."
