class TaskModel:
    """Класс для представления задачи."""

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        category: str,
        due_date: str,
        priority: str
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = "Не выполнена"

    def get_dict(self) -> dict:
        """Возвращает данные задачи в виде словаря."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @staticmethod
    def get_str(task: dict) -> str:
        """Возвращает строковое представление задачи."""
        return (
            f"Задача №{task['id']},\n"
            f"Название: {task['title']},\n"
            f"Описание: {task['description']},\n"
            f"Категория: {task['category']}, Приоритет: {task['priority']},\n"
            f"Срок выполнения: {task['due_date']}, Статус: {task['status']}"
        )
