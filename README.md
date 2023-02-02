# docsify-django

> A small proof-of-concept illustrating how to integrate markdown-driven documentation (in this case, [docsify](https://docsify.js.org)) with your [Django](https://djangoproject.com) project, so that only your authenticated users can access the docs.

## Why this?

- Given that
  - You have a Django project, and you have user documentation already written in markdown (thanks to its simple syntax, we can write the docs quickly. In addition, your documentation is in version control, as opposed to being in a database.).
  - You don't want the documentation to be public. Only logged-in users should be able to access the documentation.
  - Having a separate documentation site is out of the question, you want to use the already existing auth mechanism within your Django project.
- In my case, I wanted to use [MkDocs](http://www.mkdocs.org/) with the shiny [Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/). However, MkDocs **builds** a static site, and adding access control to this generated site is a complex process. I tried to follow [this tutorial](https://www.hacksoft.io/blog/integrating-a-password-protected-mkdocs-in-django), written for Django 1.1x, but a lot has changed in the Django ecosystem since then, so I couldn't make it work with Django 4.x (I'm pretty sure it's not impossible to make it work 😉, I just gave up after trying various things!).
- So I started looking for a solution that doesn't involve building a site, that is, generating html files and other static content. This is where [docsify](https://docsify.js.org) comes in. There are probably other solutions, but I picked docsify because I was already familiar with it, having used it some time back.
- Docsify is pretty sweet, because it doesn't **build** a site (unless you tell it to do so), it just automagically renders your markdown files in a template. So what we are doing here is that we are using Django to render the template, which has all the fancy docsify stuff. It's still a bit of hack, because I had to create a Django view for each markdown file :frowning: which can be a nightmare if your docs are gigantic. There's therefore need to explore better solutions. For now, this works fine! If you have any suggestions / ideas, please [give me a shout](https://twitter.com/engineervix/)!

## Try it out on your machine

- clone the repo and `cd` into the cloned directory.
- set up a fresh virtual environment using your preferred way of managing python virtual environments.
- install dependencies (`Django` and `crispy-bulma`)

  ```bash
  pip install -r requirements.txt
  ```

- migrate

  ```bash
  ./manage.py migrate
  ```

- create a superuser

  ```bash
  ./manage.py createsuperuser
  ```

- run the development server

  ```bash
  ./manage.py runserver
  ```

- go to <http://127.0.0.1:8000> in your browser. The docs are accessible at <http://127.0.0.1:8000/docs>. You'll be asked to login in order to access the docs.

## References

- [Integrating a password-protected MkDocs in Django](https://www.hacksoft.io/blog/integrating-a-password-protected-mkdocs-in-django)
- [This stackoverflow answer](https://stackoverflow.com/a/58901221), under the post *Basic flask implementation of Docsify documentation*.

## Image credits

- Photo 1 by <a href="https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sigmund</a> on <a href="https://unsplash.com/photos/TlFw-WoI8_w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo 2 by <a href="https://unsplash.com/@hngstrm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Henry & Co.</a> on <a href="https://unsplash.com/photos/pjJdOE2XBRU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Photo 3 by <a href="https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sigmund</a> on <a href="https://unsplash.com/photos/QuusekRfTI8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
