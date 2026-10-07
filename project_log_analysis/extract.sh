#!/bin/bash
grep "Failed password" auth.log | awk '{print $11}' > suspicious_ips.txt