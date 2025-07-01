# Pawsy - Animal Shelter Management System

Pawsy is a comprehensive web application designed to help animal shelters manage their animals, adoption processes, and volunteers. The system provides both a user-friendly web interface and a RESTful API for integration with other systems.

## Features

- **Animal Management**: Track detailed information about shelter animals including breed, size, gender, vaccination status, and more
- **Adoption Process**: Manage adoption requests from potential pet parents
- **Volunteer Management**: Keep track of shelter volunteers and their status
- **Admin Dashboard**: Powerful admin interface for shelter staff to manage all aspects of the system
- **RESTful API**: Integrate with other systems or build custom frontends using the comprehensive API

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates, HTML, CSS
- **Database**: SQLite (default), compatible with PostgreSQL, MySQL
- **Media Storage**: Local file system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Denos-PB/pawsy.git
   cd pawsy
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

### Web Interface

- **Home Page**: Browse featured animals available for adoption
- **Animals Page**: View all animals currently available for adoption
- **Animal Detail Page**: See detailed information about a specific animal and submit adoption requests
- **Volunteers Page**: View information about shelter volunteers

### Admin Interface

Access the admin interface at http://127.0.0.1:8000/admin/ to:
- Manage animals (add, edit, delete)
- Process adoption requests
- Manage volunteers
- Configure system settings

### API Endpoints

- `/api/animals/` - List and manage animals
- `/api/adoption-requests/` - View and create adoption requests
- `/api/volunteers/` - List and manage volunteers

## Project Structure

```
Pawsy/
├── Pawsy/              # Project settings
├── main/               # Main application
│   ├── models.py       # Data models
│   ├── views.py        # Views and API endpoints
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin interface configuration
│   └── serializer.py   # API serializers
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded media
└── venv/               # Virtual environment
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
