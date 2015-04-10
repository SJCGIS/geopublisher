.. :changelog:

History
-------

0.1.1 (2015-03-25)
---------------------

* Fixed
  * Added two missing directories. Because Git doesn't support adding empty directories, I've added 'stub' files to the directories so they get picked up correctly. Without these directories, most of the tests were failing.
  * When the tests failed, the zf object couldn't be properly referenced in the finally blocks. I've switched to the contextlib / with syntax which avoids this issue and has other advantages.

0.1.0 (2015-03-23)
---------------------

* First release
