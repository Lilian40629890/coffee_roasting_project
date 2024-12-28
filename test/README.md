# Test

## How to Run Test
- Run tests for new data: `python test/new_data/test_new_data_management.py`
- Run tests for old data: `python test/old_data/test_old_data_management.py`

## GitHub Actions Workflow
To automate and validate the test process, I have configured GitHub Actions workflow. 
   - for new data: `.github/workflows/python-test_new_data_management.yml`
   - for old data: `.github/workflows/python-test_old_data_management.yml`

## Test Script Overview
- **test_main.py**: Validates the correctness of data extraction and transformation logic., and verifies that data is successfully imported into the MySQL database.
- **python-app_new_data_management.yml**: Automates the testing process by setting up the Python environment, installing dependencies, and running tests on every push or pull request. It ensures that the testing_new_data.py script functions correctly and verifies the integration with MySQL by running tests as part of the CI pipeline.

## Differences Between Test and Production Scripts
To facilitate testing without requiring access to the actual NAS system or MySQL database, the test scripts include the following modifications:
1. NAS System Simulation:
- Instead of connecting to a real NAS, test scripts use mock functions to simulate data retrieval.
- Mocked paths and sample data are used to represent files stored on the NAS.
2. MySQL Database Simulation:
- Test scripts do not connect to a real database but use simulated connections.
- Data upload functions print outputs to verify the process instead of executing actual database queries.
