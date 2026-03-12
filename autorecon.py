#!/usr/bin/env/ python3


"""
 __________________________________________
|                                          |
|       **** ---- AutoRecon ----- ****.    |
|                                          |
|  Author:Joynto Ghosh                     |
|  Purpose: Multi-mode recon on a single IP|
|___________________________________________ 

"""
import argparse
import subprocess
import sys
import os
import json
import datetime
from pathlib import Path

class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    BLUE   = "\033[94m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"
    