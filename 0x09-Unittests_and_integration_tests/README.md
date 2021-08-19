0x09. Unittests and Integration Tests

- The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

- Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

- Integration tests will test interactions between every part of your code.

- Execute your tests with

$ python -m unittest path/to/test_file.py

General:
- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures
