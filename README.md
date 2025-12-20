# Aurora Hospital Backend

This repository contains the Django backend for the Aurora Hospital website.

## Quick Setup (Windows)

- Clone the repo:

```powershell
git clone <repository-url>
cd Aurora-Hospital-Backend
```

- Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Install dependencies:

```powershell
pip install -r requirements.txt
```

- Configure environment (update `core/settings.py` or use environment variables):

  - DATABASE settings (Postgres, SQLite, etc.)
  - `DEBUG`, `ALLOWED_HOSTS`, secret key, and any storage credentials

- Apply migrations:

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

- (Optional) Create a superuser:

```powershell
python manage.py createsuperuser
```

## Media & Static

- During development, media files are served by Django. Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in `core/settings.py`.
- To collect static files for production:

```powershell
python manage.py collectstatic
```

## Data Seed Orientation (order matters)

Run the seeds in the following order to populate navigation, departments and doctors data:

1. Seed navigation (menus and menu contents):

```powershell
python manage.py seed_nav_data
```

2. Seed departments:

```powershell
python manage.py seed_departments
```

3. Seed doctors:

```powershell
python manage.py seed_doctors
```

## Run server

```powershell
python manage.py runserver
```

## Troubleshooting

- If migrations fail, inspect the error message and run `python manage.py makemigrations` then `migrate`.
- If a seeder command errors due to missing models or fields, ensure you are on the correct branch and migrations are applied.

## Contact / Contributing

- For questions or contributions, open an issue or pull request against this repository.

# Aurora_Hospital_Website
