# Rabble

A Reddit/Twitter-style social platform built with Django and Django REST Framework. Users can follow each other, join communities, post and comment within topic-based sub-communities ("subrabbles"), and message each other directly.

## Features

- **Auth & profiles** — custom user model with profile pictures, following/follower relationships
- **Communities & sub-communities** — `Communities` group multiple `Subrabbles` (topic-specific boards), each with their own membership and invite system
- **Posts, comments, replies** — nested discussion threads scoped to a subrabble
- **Direct messaging** — `Conversations` with multiple members and a message log
- **REST API** — full CRUD over posts and comments via Django REST Framework (see [src/API.md](src/API.md))
- **Server-rendered UI** — Django templates for browsing feeds, posts, and profiles alongside the API

## Tech stack

Django 5.1 · Django REST Framework · SQLite (dev) · pytest / pytest-django + factory_boy for tests · Gunicorn + WhiteNoise for deployment

## Project structure

```
src/
  rabble/          # core app: models, views, forms, templates, tests
  api/              # DRF serializers, views, and API routes
  cs220hw/          # Django project settings/urls
  static/           # CSS/JS
  templates/        # server-rendered pages
```

Data model highlights (`src/rabble/models.py`): `User`, `Following`, `Communities`, `Subrabbles`, `Posts`, `Comments`, `Replies`, `Conversations`, `ConversationMessages`, `CommunityInvites`.

## Running locally

```bash
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver
```

## Tests

```bash
cd src
pytest
```
