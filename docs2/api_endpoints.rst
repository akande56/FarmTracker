API endpoints
=============


-----


Registration
------------

- /api-farmer/registration/ (POST)
    - username
    - email
    - password1
    - password2
    - farm name
    - farm address

    Returns Token key


- /api-inspector/registration/ (POST)
    - username
    - email
    - password1
    - password2

    Returns Token key



Loging/logout/rest password/change password...
------------------------------------------------    

- /rest-auth/login/ (POST)

    - username
    - email
    - password

    Returns Token key


- /rest-auth/logout/ (POST)

    .. note:: ``ACCOUNT_LOGOUT_ON_GET = True`` to allow logout using GET - this is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout

- /rest-auth/password/reset/ (POST)

    - email

- /rest-auth/password/reset/confirm/ (POST)

    - uid
    - token
    - new_password1
    - new_password2

    .. note:: uid and token are sent in email after calling /rest-auth/password/reset/

- /rest-auth/password/change/ (POST)

    - new_password1
    - new_password2
    - old_password

    .. note:: ``OLD_PASSWORD_FIELD_ENABLED = True`` to use old_password.
    .. note:: ``LOGOUT_ON_PASSWORD_CHANGE = False`` to keep the user logged in after password change

- /rest-auth/user/ (GET, PUT, PATCH)

    - username
    - first_name
    - last_name

    Returns pk, username, email, first_name, last_name


