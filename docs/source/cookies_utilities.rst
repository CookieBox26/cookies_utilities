Documentation
=============

Functions
*********

cookies_utilities.get_dates
---------------------------

.. autofunction:: cookies_utilities.get_dates

**Example**

.. code-block:: python

   import cookies_utilities as cu
   dates = cu.get_dates(
       start='2016-07-01 02:00:00',
       end='2016-07-02 01:00:00',
       format='%Y-%m-%d %H:%M:%S',
       delta={'hours': 1})
   # ['2016-07-01 02:00:00', '2016-07-01 03:00:00', ..., '2016-07-02 01:00:00']

Classes
*******

cookies_utilities.Stopwatch
---------------------------

.. autoclass:: cookies_utilities.Stopwatch
   :members:
   :undoc-members:

..   :show-inheritance:

**Example**

.. code-block:: python

   import cookies_utilities as cu
   sw = cu.Stopwatch()
   sw.press('train start')
   # train
   sw.press('train end')
   # test
   sw.press('test end')
   sw.show()

.. code-block:: console

   time1(train start-train end): 2.000s
   time2(train end-test end): 1.000s
   total: 3.000s
