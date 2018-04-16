## Watchlist v2

### Project description

This is an update of my previous watchlist project. It allows users to find movies and write reviews for those movies.

##### NB Please note the project is still in development

### Set-up instructions

1. You will need to have Python3.6 installed in your machine together with venv and pip.
2. Set up the virtual environment and activate it

```bash
$ python3.6 -m venv virtual
$ source virtual/bin/activate

```
3. Install all the necessary modules

```bash
$ pip install -r requirements.txt
```

4. Get an API key from [TMDB](https://www.themoviedb.org/)

5. Create an Instance folder at your project root.
```bash
$ mkdir instance
```
6. Create a config.py file  inside the instance folder
```bash
$ touch instance/config.py
```
7.  Paste in the API key inside the new config.py file
```python
  MOVIE_API_KEY='Your API KEY HERE'
```
6. Run the application

```bash
$ python3.6 run.py
```

### Branches

Each branch  tackles a specific part in the application development

0. Master: The primary branch with all the content.
1. 01-Templates: Introduction to templates and template variables.
2. 02-Dynamic-routes : Creating a dynamic view function.
3. 03-Configurations: Set up the projects configuration file.
4. 04-Control-Flows: Added control flows in our template files.
5. 05-Storing-API-Keys: Store API key in instance folder
6. 06-Movie Model: Movie model and test class
7. 07-API-call: Make API call
8. 08-For-Loops-Macros:Looping through items using Macros
9. 09-Base-Template: Add base template and extend to template files
10. 10-Adding-Bootstrap: Added Bootstrap extension and structured the page
11. 11.Adding-CSS : Added css file and styled the page
### License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.
