from contextlib import contextmanager


class Resource:
    def __init__(self, **kwargs):
        self._opened = False

    def open(self):
        self._opened = True
        print("Открываем ресурс")

    def action(self, **kwargs):
        print("Чё то мы делаем")
        print(f"Значения словаря: {kwargs}")

    def close(self):
        self._opened = False
        print("Закрываем ресурс")

    def __del__(self):
        if self._opened == True:
            print("У вас ресурс не закрыт")
            self.close(self)


@contextmanager
def open_resource(**kwargs):
    resource = False
    try:
        resource = Resource()
        resource.open()
        # resource.action()
        yield resource
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if resource:
            resource.close()


if __name__ == "__main__":
    with open_resource(a=1, b=2, c=3) as rs:
        rs.action(a=1, b=2, c=3)
