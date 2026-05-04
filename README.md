# Portal JM Backend

Backend of an editorial blog developed for a client in the educational and religious sector. Engineered with Django, Django REST Framework (DRF), and PostgreSQL.

## 🚀 Technologies

- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **PostgreSQL**

## 📦 Features

- **Accounts Management:** Custom user authentication and management.
- **Blog System:** Complete editorial functionalities including articles, categories, and tags.
- **Media Handling:** Video and image management (banners, covers, carousels).
- **Comments System:** Generic comments system for the blog content.

## 🛠️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd portaljm-back
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add the necessary environment variables (e.g., Database credentials, Django Secret Key, Debug status).

5. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure

- `portaljm/` - Main Django project configuration settings.
- `accounts/` - User authentication and account management app.
- `blog/` - Main blog application handling articles, questions, comments, and carousels.
- `common/` - Shared utilities and common models.
- `media/` - Directory for user-uploaded files (images, banners, videos).
