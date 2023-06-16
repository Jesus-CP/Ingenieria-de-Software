# Ingenieria-de-Software
# Con Django # 

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# En PostgreSQL #

INSERT INTO auth_group VALUES(0, 'Default');
INSERT INTO auth_group VALUES(1, 'Administrador');
INSERT INTO registration_profile VALUES(0, 'No', 'No', 1, 1);