# class User:
#     def __init__(self, name, email):    # name и email строгие аргументы задаваемые __init__
#         self.name = name    # name и email атрибуты для всех экземпляров
#         self.email = email
# peter = User(name="Peter Robertson", email="peterrobertson@mail.com")    # аргументы задавать обязательно!
# julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")
#
# print(peter.name)
# print(julia.email)

# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id

events = [{"объект": -28, "отношение": "друг", "проживание": "петропавловск"},
    {"объект": 35, "отношение": "товарищ", "проживание": "новосибирск"},
    {"объект": 44, "отношение": "знакомый", "проживание": "новгород"}]
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))


class Event:
    def __init__(self, age=0, event_type="", session_id=""):
        self.age = age
        self.type = event_type
        self.session_id = session_id

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age

    def init_from_dict(self, event_dict):
        self.age = event_dict.get("объект")
        self.type = event_dict.get("отношение")
        self.session_id = event_dict.get("проживание")
for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.age)
    print(event_obj.type)
    print(event_obj.session_id)
    print('--------------------------------------------------------------------------------------------')