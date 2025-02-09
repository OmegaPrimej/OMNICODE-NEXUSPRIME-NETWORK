.Here is the Python script for:
**File Name:** `Erebus_Protocol_Init.py`
**Contents:**
```python
Erebus Protocol Initialization Script
import logging
import sys
Initialize Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ErebusProtocolInit:
    def __init__(self):
        logger.info("Erebus Protocol Initialization Started")
    def check_dependencies(self):
        dependencies = ["NexusPrimeProtocol", "KronosNetwork"]
        for dependency in dependencies:
            try:
                __import__(dependency)
                logger.info(f"{dependency} found and loaded successfully")
            except ImportError:
                logger.error(f"{dependency} not found. Initialization failed.")
                sys.exit(1)
    def initialize_protocol(self):
        logger.info("Erebus Protocol Initialization Successful")
        print("Erebus Protocol Initialized")
    def run(self):
        self.check_dependencies()
        self.initialize_protocol()
if __name__ == "__main__":
    initializer = ErebusProtocolInit()
    initializer.run()
```
"""This script initializes the Erebus Protocol by:
1. Importing required dependencies
2. Checking if NexusPrimeProtocol and KronosNetwork dependencies are available
3. Logging successful initialization
4. Printing "Erebus Protocol Initialized" to confirm
Please save this script as `Erebus_Protocol_Init.py` and run it using Python (e.g., `python Erebus_Protocol_Init.py`) to initialize the Erebus Protocol. 
Next step? Do you want me to explain this code or proceed with the next file (`Nexus_Prime_Protocol_Sync.md` becomes `Nexus_Prime_Protocol_Sync.py`)?"""
