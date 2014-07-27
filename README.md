textclock
=========

A flask/backbone application that renders a text-based clock.

Once upon a time, I saw [QLOCKTWO's wallclock](http://www.amazon.com/dp/B006IZXP1M/?tag=047-20) and
wondered if I could make it myself.  

Here's my attempt.  While I was at it, might as well try out backbone.js.

Requirements
------------
* [python 2.7](https://www.python.org/download/releases/2.7/)
* [fabric](http://docs.fabfile.org/en/1.6/installation.html)
* [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation)

Install
-------
`cd` into the local directory and execute `fab setup`.

Execution
---------
`cd` into the local directory and execute `fab runserver`.

Your server should now be running on the local host on port 5000!

You can now go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to view the clock.