# C5LML Game Forum

## Description

Link to the git repo: https://github.com/TrevorChLiu/C5-LML.git

C5LML is a community platform where gamers can explore game rankings, detailed profiles, and engage in interactive discussions to share strategies and enhance their gaming experience.

## Branch

This is a Trunk-Based Development, so most of the development happens at the main branch. (In fact, we used feature branch workflow at first and that is why here was a branch which is deleted later called `user-and-core`)

## Dependencies

Install Django5, Django-Boostrap5, and Pillow before you go:
> pip install django\
> pip install django-bootstrap5\
> pip install pillow

## Usage

To open the website, type:
> python manage.py runserver

and visit http://127.0.0.1:8000 in your browser.

## Development

Please store all templates/static files you use in the global `templates` or `static` folders.

All the colors infomation are stored in `C5-LML/static/css/colors.css`, you can use it directly.