from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from ...models import Employee, Subdivision
import random

NUM_USERS = 50000
NUM_SUBDIVISIONS = 25

SUBDIVISION = [
    "Главный офис",
    "Склад",
    "Столовая",
    "Администрация",
    "Коммерческие службы",
    "Технические службы",
    "Отдел снабжения",
    "Отдел продаж",
    "Отдел рекламы",
    "Сектор закупок по РФ",
    "Сектор зарубежных закупок",
    "Отдел главного конструктора",
    "Отдел главного технолога",
    "Юридический отдел",
    "Сектор договорной работы",
    "Служба логистики",
    "Отдел логистики",
    "Сектор грузоперевохок",
    "Склад 1",
    "Склад 2",
    "Склад 3",
    "Площадь сбыта",
    "Площадь списания",
    "Отдел главного механика",
    "Продоволствие"

]


class Provider(faker.providers.BaseProvider):
    """ Provide self data for subdivision items """

    def subdivision_category(self):
        return self.random_element(SUBDIVISION)


class Command(BaseCommand):
    """ Command creates subdivisions and employees """
    help = "Generates test data"

    def handle(self, *args, **options):
        faker = Faker('ru_RU')
        self.stdout.write("Deleting old data...")
        models = [Employee, Subdivision]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        faker.add_provider(Provider)

        for _ in range(NUM_SUBDIVISIONS):
            d = faker.unique.subdivision_category()
            Subdivision.objects.create(name=d)

        for _ in range(50):
            c_id = Subdivision.objects.values_list("id", flat=True)
            с_name = random.choice(SUBDIVISION)
            parent = random.choice(c_id)
            Subdivision.objects.create(
                name=с_name,
                parent_id=parent,
            )

        check_subdivision = Subdivision.objects.all().count()
        self.stdout.write(
            self.style.SUCCESS(f'Number of subdivisions: {check_subdivision}'))

        for _ in range(NUM_USERS):
            u_name = faker.name()
            u_position = faker.job()
            u_salary = round(random.randint(90000, 120000) / 1000) * 1000
            u_hiring = faker.date()
            c_id = Subdivision.objects.values_list("id", flat=True)
            u_subdivision = random.choice(c_id)
            Employee.objects.create(
                full_name=u_name,
                position=u_position,
                salary=u_salary,
                hiring=u_hiring,
                subdivision_id=u_subdivision
            )

        check_users = Employee.objects.all().count()
        self.stdout.write(
            self.style.SUCCESS(f'Number of workers: {check_users}'))
