# SportsHub

SportsHub is a web application built with Django that provides real-time football scores and allows users to sign up, log in, and access a dashboard. The application integrates with an external API to fetch scheduled events and display football match information.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Football Scores**: Football (Soccer) scores from previous tournaments (did not know I had to pay for current APIs to use).
- **Dashboard**: A user-specific dashboard page (once implemented).
- **Error Handling**: Error messages displayed if scores fail to load.

## Technologies

- Django 3.x
- Python 3.x
- HTML, CSS (Bootstrap used for styling)
- External API for football scores (SportAPI)
- SQLite (default database for development)

## Setup

### Prerequisites

Ensure you have Python 3.x installed. You can check this by running:

```bash
python --version
