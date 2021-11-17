# http-forms-and-cows

Not everything in computing has bindings for Python (as much as I would like that to be true), so it's important to learn how to work with the host system and pass details back and forth.

The goal for this project is to build a very simple django server (so simple that it's only two views, one form, and one model) that passes user input to the operating system, runs a command, retrieves the output, and sends it back to the client. We use the model to back up a copy of what people submit to the page, and have a second endpoint at /history where it lists the last ten things that were sent through the form.

[Cowsay](https://en.wikipedia.org/wiki/Cowsay) is a utility that has been around for a very long time, but is essentially just a toy. If you don't have it already, then you can install it simply by running:

- OSX: `brew install cowsay` Note: If you're running Big Sur, follow these [instructions](http://macappstore.org/cowsay/)
- Ubuntu / Debian: `sudo apt install cowsay`

Sample usage: `cowsay "Hello, world!"`

WINDOWS USERS ONLY:

Install cowsay by installing it through NPM: `npm install -g cowsay`. When using Python's `subprocess` module, you will *most likely* need to pass `shell=True` as well. This is because Windows does not look at the PATH without passing that flag.
