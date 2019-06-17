#!/usr/bin/env python3

# class for each application
class application:
   def __init__(self):
      self.company
      self.date_applied
      self.timeout_date
      self.last_contact_date
      self.last_contact_method
      self.interview_date
      self.in_process
   def update_last_contact(self, contact):
      self.last_contact_date = contact[0]
      self.last_contact_method = contact[1]
   def update_in_process_flag(self, flag):
      self.in_process = flag
   def update_interview(self, date):
      self.interview_date = date
   def set_all(self, all_data):
      self.company = all_data[0]
      self.date_applied = all_data[1]
      self.timeout_date = all_data[2]
      self.last_contact_date = all_data[3]
      self.last_contact_method = all_data[4]
      self.interview_date = all_data[5]
      self.in_process = all_data[6]
   def create_tuple_for_display(self):
      data = (self.company,
              self.date_applied,
              self.timeout_date,
              self.last_contact_date,
              self.last_contact_method,
              self.interview_date,
              self.in_process)

# argparse
# Argument for non-standard config path
# Arguments for overrides:
#  - content location
#  - timeout for no response
#  - color scheme
#     - waiting for response
#     - Expired by timeout
#     - Process completed
#     - Interviewing

# Load json file, grabbed from config

# Add new job

# Update job information

# display data
