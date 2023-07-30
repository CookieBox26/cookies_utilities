Documentation
=============

Functions
*********

cookies_utilities.copy_datetime
-------------------------------

.. autofunction:: cookies_utilities.copy_datetime

**Example**

.. code-block:: python

   import cookies_utilities as cu
   import datetime

   dt = datetime.datetime.strptime('2016-07-01 02:15:00', '%Y-%m-%d %H:%M:%S')
   dt_copy = cu.copy_datetime(dt, {'minute': 0})  # --> 2016-07-01 02:00:00

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

cookies_utilities.convert_time_to_feature
-----------------------------------------

.. autofunction:: cookies_utilities.convert_time_to_feature

.. code-block:: python

   import cookies_utilities as cu

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='day', ceiling='hour')
   #  --> 0.125  ( 3:00 am is 12.5% of the day )

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='year', ceiling='day')
   #  --> 0.002732  ( 1.0 / 366.0 )

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='month', ceiling='day')
   #  --> 0.032258  ( 1.0 / 31.0 )

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='week', ceiling='hour')
   #  --> 0.017857  ( 0.125 / 7.0 )

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='hour', ceiling='minute')
   #  --> 0.666667  ( 40.0 / 60.0 )

   feature_value = cu.convert_time_to_feature(
       dt='2023-01-02 03:40:50', format='%Y-%m-%d %H:%M:%S',
       period='minute')
   #  --> 0.833333  ( 50.0 / 60.0 )

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

   time1 (train start - train end): 2.000s
   time2 (train end - test end): 1.000s
   total: 3.000s
