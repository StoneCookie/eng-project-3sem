from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Наименование роли", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name")
        verbose_name = "Роли"
        verbose_name_plural = "Роли"

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField("ФИО пользователя", max_length=255)
    mail = models.CharField("E-mail", max_length=60)
    login = models.CharField("Логин", max_length=60)
    password = models.CharField("Пароль", max_length=60)
    id_role = models.ForeignKey(
        Role, verbose_name="ID Роли", on_delete=models.CASCADE)

    def __str__(self):
        return self.fio

    class Meta:
        ordering = ("id", "fio", "mail", "login", "password", "id_role")
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Сфера деятельности", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name")
        verbose_name = "Сфера деятельности"
        verbose_name_plural = "Сфера деятельности"

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Тип работы", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name")
        verbose_name = "Тип работы"
        verbose_name_plural = "Тип работы"

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название компании", max_length=255)
    description = models.CharField("Описание", max_length=255)
    mail = models.CharField("E-mail", max_length=60)
    phone = models.CharField("Номер телефона", max_length=11)
    fio = models.CharField("ФИО представителя", max_length=255)
    login = models.CharField("Логин", max_length=60)
    password = models.CharField("Пароль", max_length=60)
    id_role = models.ForeignKey(
        Role, verbose_name="ID Роли", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name", "description", "mail", "phone",
                    "fio", "login", "password", "id_role")
        verbose_name = "Компания"
        verbose_name_plural = "Компания"

class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название вакансии", max_length=255)
    description = models.CharField("Описание", max_length=255)
    requirements = models.CharField("Требования", max_length=255)
    conditions = models.CharField("Условия", max_length=255)
    responsibilities = models.CharField("Обязанности", max_length=255)
    id_category = models.ForeignKey(
        Category, verbose_name="ID сферы деятельности", on_delete=models.CASCADE)
    id_work = models.ForeignKey(
        Work, verbose_name="ID типа работы", on_delete=models.CASCADE)
    id_company = models.ForeignKey(
        Company, verbose_name="ID компании", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name", "description", "requirements", "conditions",
                    "responsibilities", "id_category", "id_work", "id_company")
        verbose_name = "Работа"
        verbose_name_plural = "Работа"

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название мероприятия", max_length=100)
    date = models.DateTimeField("Дата проведения мероприятия", max_length=15)
    id_company = models.ForeignKey(
        Company, verbose_name="ID компании", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name", "date", "id_company")
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название курса", max_length=255)
    description = models.CharField("Описание", max_length=255)
    duration = models.CharField("Длительность", max_length=255)
    id_category = models.ForeignKey(
        Category, verbose_name="ID сферы деятельности", on_delete=models.CASCADE)
    id_company = models.ForeignKey(
        Company, verbose_name="ID компании", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name", "description", "duration",
                    "id_category", "id_company")
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

STATUS_CHOICES = (
    ('ч', 'Черновик'),
    ('о', 'Опубликована'),
    ('а', 'Архив'),
)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Заголовок новости", max_length=255)
    description = models.CharField("Описание", max_length=255)
    date = models.DateTimeField("Дата создания", max_length=15)
    status = models.CharField("Статус", max_length=1,
                              choices=STATUS_CHOICES, default='ч')
    id_category = models.ForeignKey(
        Category, verbose_name="ID сферы деятельности", on_delete=models.CASCADE)
    id_company = models.ForeignKey(
        Company, verbose_name="ID компании", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id", "name", "description", "date",
                    "id_category", "id_company", "status")
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        Users, verbose_name="ID пользователя", on_delete=models.CASCADE, null=True, blank=True)
    id_course = models.ForeignKey(
        Course, verbose_name="ID курса", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ("id", "id_user", "id_course")
        verbose_name = "Запись на курс"
        verbose_name_plural = "Запись на курс"
