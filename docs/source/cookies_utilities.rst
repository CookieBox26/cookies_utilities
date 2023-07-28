Documentation
=============

Functions
*********

cookies_utilities.get_dates
---------------------------

.. autofunction:: cookies_utilities.get_dates

**Example**

An example of incrementing by one day.

.. code-block:: python

   import cookies_utilities as cu
   dates = cu.get_dates(
       start='2016/07/01', end='2016/07/03', format='%Y/%m/%d',
       delta={'days': 1}, format_out='%Y-%m-%d')
   print(dates)

.. code-block:: console

   ['2016-07-01', '2016-07-02', '2016-07-03']

An example of incrementing by 20 minutes.

.. code-block:: python

   import cookies_utilities as cu
   dates = cu.get_dates(
       start='2016-07-01 02:00:00', end='2016-07-01 03:00:00',
       format='%Y-%m-%d %H:%M:%S',
       delta={'minutes': 20})
   print(dates)

.. code-block:: console

   ['2016-07-01 02:00:00', '2016-07-01 02:20:00', '2016-07-01 02:40:00', '2016-07-01 03:00:00']

An example of retrieving as a generator iterator.

.. code-block:: python

   import cookies_utilities as cu
   dates = cu.get_dates(
       start='2016/07/01', end='2016/07/03', format='%Y/%m/%d',
       delta={'days': 1}, geniter=True)
   print(type(dates))
   for date in dates:
       print(date)

.. code-block:: console

   <class 'generator'>
   2016/07/01
   2016/07/02
   2016/07/03

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
