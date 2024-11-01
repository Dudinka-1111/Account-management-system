class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # Уровень доступа для обычного сотрудника

    # Get методы для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Set методы для изменения значений атрибутов
    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администратора

    # Метод для добавления пользователя в систему
    def add_user(self, user_list,user):
        user_list.append(user)
        print(f'Пользователь {user.get_name()} успешно добавлен в список.')

    # Метод для удаления пользователя из системы
    def remove_user(self, user_list,user):
        user_list.remove(user)
        print(f'Пользователь {user.get_name()} успешно удален из списка.')

    # Метод для отображения списка пользователей
    def display_users(self, user_list):
        for user in user_list:
            print(f'ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')

#Пример использования
users = []
admin = Admin('1', 'Ben')
user1 = User('2', 'Codi')
user2 = User('3', 'Tom')

print(user1.get_name())

# Изменение имени пользователя и проверка
user1.set_name('Pol')
print(f"Имя пользователя после изменения: {user1.get_name()}")

# Администратор добавляет пользователей
admin.add_user(users, user1)
admin.add_user(users, user2)

# Отобразить список пользователей
print("\nСписок пользователей:")
admin.display_users(users)

# Администратор удаляет пользователей
admin.remove_user(users, user1)

# Отобразить список пользователей
print("\nСписок пользователей:")
admin.display_users(users)
