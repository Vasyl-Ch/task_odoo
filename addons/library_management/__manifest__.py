{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Manage library books and rentals",
    "author": "Vasyl Cherkes",
    "category": "Services",
    "depends": ["base", "contacts"],  # Залежності від базових модулів Odoo
    "data": [
        "security/ir.model.access.csv",  # Права доступу до моделей
        "views/book_views.xml",          # Відображення для книг
        "views/rent_views.xml",          # Відображення для оренд
        "wizard/rent_wizard_views.xml"   # Відображення для майстра оренди
    ],
    "installable": True,  # Модуль можна встановлювати
    "application": True,  # Модуль є окремим додатком
}
