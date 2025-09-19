import os
import tempfile
import pytest
from logparse import parse_log
import logging

def test_parse_log_counts_correctly(caplog):
    """Tests if the log file is parsed and counts errors and warnings correctly."""
    
    log_content = """
    INFO: This is an informational message.
    WARNING: This is a warning message.
    ERROR: This is an error message.
    WARNING: Another warning.
    INFO: Another informational message.
    ERROR: Another error message.
    """
    
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".log") as tmp_log:
        tmp_log.write(log_content)
        temp_file_path = tmp_log.name
    
    with caplog.at_level(logging.INFO):
        parse_log(temp_file_path, False)
    
    os.remove(temp_file_path)
    
    assert "Found 2 errors and 2 warnings" in caplog.text

def test_parse_log_nonexistent_file(caplog):
    """Tests if the function handles a nonexistent file gracefully."""
    nonexistent_path = "/nonexistent/path/to/file.log"
    
    # We expect the function to raise a FileNotFoundError
    parse_log(nonexistent_path, False)

    # Assert that the correct error message was logged
    assert f"The file '{nonexistent_path}' was not found." in caplog.text