from .solution import Employee


def _employees_from_lists(rows: list[list[int | list[int]]]) -> list[Employee]:
    employees: list[Employee] = []
    for row in rows:
        emp_id = row[0]
        importance = row[1]
        subs = row[2]
        assert isinstance(emp_id, int)
        assert isinstance(importance, int)
        assert isinstance(subs, list)
        employees.append(Employee(emp_id, importance, subs))
    return employees


def run_get_importance(solution_class: type, employees: list[list[int | list[int]]], id: int):
    emp_objects = _employees_from_lists(employees)
    implementation = solution_class()
    return implementation.get_importance(emp_objects, id)


def assert_get_importance(result: int, expected: int) -> bool:
    assert result == expected
    return True
