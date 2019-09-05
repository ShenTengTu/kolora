======
kolora
======

-----------------------------------------------------
"kolora teksto" is Esperanto, meaning "colored text."
-----------------------------------------------------
Use method chain to make colored text in terminal.

.. image:: https://github.com/ShenTengTu/kolora/raw/master/img/Kolora_logo.png


Description
===========
example :

.. code-block:: python

    from kolora import Kolora

    txt = Kolora()\
        ('"kolora teksto"', fg='Maroon', bg="#d7af00")\
        (' is Esperanto, meaning ', reset=True)\
        ('"colored text."', fg='Silver', bg="#005fff").text

    print(txt)

.. image:: https://github.com/ShenTengTu/kolora/raw/master/img/example.png


Install
-------
Current package is testing version, the distribution is uploaded to Test PyPI.
.. code-block::

    pip install -i https://test.pypi.org/simple/ kolora


Testing
-------
Use the command as below:

.. code-block::

    python -m test

