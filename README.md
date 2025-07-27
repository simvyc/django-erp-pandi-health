# django-erp-pandi-health

**Django based ERP Pandi for patients medical records**

:rocket: **Setup Notes**

After cloning the project and installing dependencies:

:small_blue_diamond: Run migrations to set up the database:

<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>

:small_blue_diamond: Create a superuser to access the admin panel:

<pre><code>python manage.py createsuperuser</code></pre>

**User Roles:**

- :health_worker: Doctors are added by the superuser through the admin panel.

- :raising_hand: Patients can register themselves using the registration form.

Once users are created, users can login through the login form.
