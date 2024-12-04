import json
import pytest
from unittest.mock import mock_open, patch
from task_manager.dao import TaskDAO

# Пример данных для теста
mock_data = [
    {
        "id": 1,
        "title": "Изучить основы FastAPI",
        "description": "Пройти документацию по FastAPI и создать простой проект",
        "category": "Обучение",
        "due_date": "2024-11-30",
        "priority": "Высокий",
        "status": "Не выполнена"
    }
]

# Тест для метода all_task_json
def test_all_task_json(mocker):
    mocker.patch("builtins.open", mock_open())
    
    result = TaskDAO.all_task_json()
    
    assert result is not None
    open.assert_called_once_with("data_task.json", "r", encoding="utf-8")

def test_all_task_json_empty(mocker):
    # Тест, если файл не существует или пуст
    mocker.patch("builtins.open", mock_open(read_data=""))
    
    result = TaskDAO.all_task_json()
    
    assert result == []

# Тест для метода find_task_by_id_json
def test_find_task_by_id_json(mocker):
    mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_data)))
    
    result = TaskDAO.find_task_by_id_json(1)
    
    assert result["id"] == 1
    assert result["title"] == "Изучить основы FastAPI"

def test_find_task_by_id_json_not_found(mocker):
    mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_data)))
    
    result = TaskDAO.find_task_by_id_json(999)
    
    assert result == {}

# Тест для метода add_task_json
def test_add_task_json(mocker):
    mocker.patch("builtins.open", mock_open())

    new_task = {
        "id": 2,
        "title": "Изучить Django",
        "description": "Создать простой проект на Django",
        "category": "Обучение",
        "due_date": "2024-12-15",
        "priority": "Средний",
        "status": "Не выполнена"
    }

    result = TaskDAO.add_task_json(mock_data + [new_task])

    assert result is True
    open.assert_called_once_with("data_task.json", "w", encoding="utf-8")


def test_del_task_id_json(mocker):
    mocker.patch("builtins.open", mock_open())
    
    updated_data = [task for task in mock_data if task["id"] != 1]
    
    result = TaskDAO.del_task_id_json(updated_data)
    
    assert result is True
    open.assert_called_once_with("data_task.json", "w", encoding="utf-8")

