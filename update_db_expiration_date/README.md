# Database Expiration Date Updater

## Overview
The **Database Expiration Date Updater** is a custom Odoo module for version 17.0 that automates the process of updating the database expiration date based on the system parameters. The module runs a scheduled task daily to check if the expiration date matches the current date and updates it accordingly.

## Features
- Automated scheduler to update the database expiration date.
- Easy integration with Odoo 17.0.

## Usage
- Once installed, the module will automatically run a scheduled task daily to update the expiration date based on the configuration.

## Installation
1. Copy the module to your Odoo custom addons directory.
2. Update the Odoo module list:
   ```bash
   sudo odoo -u update_db_expiration_date
