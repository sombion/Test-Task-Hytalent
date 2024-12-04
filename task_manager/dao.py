import json
from task_manager.models import TaskModel


class TaskDAO:

    @staticmethod
    def all_task_json() -> list:
        """Возвращает список всех задач из файла."""
        try:
            with open("data_task.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("JSON должен содержать список!")
        except (FileNotFoundError, ValueError):
            data = []
        return data

    @staticmethod
    def find_task_by_id_json(task_id: int) -> dict:
        """Ищет задачу по ID."""
        tasks = TaskDAO.all_task_json()
        matching_tasks = [task for task in tasks if int(task["id"]) == task_id]
        return matching_tasks[0] if matching_tasks else {}

    @staticmethod
    def add_task_json(data: list) -> bool:
        """Сохраняет задачи в файл."""
        try:
            with open("data_task.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        except Exception as error:
            print(f"Ошибка сохранения данных: {error}")
            return False

    @staticmethod
    def del_task_id_json(updated_data: list) -> bool:
        """Удаляет задачу по ID, обновляя файл."""
        try:
            with open("data_task.json", "w", encoding="utf-8") as file:
                json.dump(updated_data, file, ensure_ascii=False, indent=4)
            return True
        except Exception as error:
            print(f"Ошибка удаления задачи: {error}")
            return False
