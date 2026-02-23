class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(ind.get("name"), ind.get("age")) for ind in people]
    for pers in people:
        part = pers.get("wife")
        if part:
            Person.people[pers["name"]].wife = Person.people[part]
        part = pers.get("husband")
        if part:
            Person.people[pers["name"]].husband = Person.people[part]
    return result
