# MFRC522-python Examples

The preferred way to run the examples is by creating a virtual environment and
installing MFRC522-python and all its dependencies in it.

```shell
# Clone git repository
git clone https://github.com/chme/MFRC522-python.git
cd MFRC522-python

# Create virtual env in the cloned repository
virtualenv -p python3 venv
# Activate the virtual env
source venv/bin/activate
# Install MFRC522-python
python3 setup.py install
# Install required dependencies
pip3 install -r requirements.txt

# Run example
python3 examples/firmware_check.py

# Deactivate virtual env
deactivate
```


## MFRC522
Python ports of some of the examples from https://github.com/miguelbalboa/rfid

- `firmware_check.py`
- `dump_info.py`
- `read_and_write.py`
- `minimal_interrupt.py`

## SimpleMFRC522

TODO