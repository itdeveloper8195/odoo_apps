# -*- encoding: utf-8 -*-

import logging
from datetime import datetime, timedelta

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def update_expiration_date(self):
        """
        - This method updates the expiration date stored
          in the 'database.expiration_date'
        - system parameter by adding 30 days to it,
          if it matches today's date.
        - It handles dates in both 'YYYY-MM-DD HH:MM:SS' and
          'YYYY/MM/DD HH:MM:SS' formats.
        """
        # Get today's date
        today = fields.Date.context_today(self)

        # Retrieve the expiration date parameter as a string
        param_str = self.env['ir.config_parameter'].sudo(
        ).get_param('database.expiration_date')

        if param_str:
            expiration_datetime = False

            # Convert the parameter string to a datetime object
            # based on the format
            if '-' in param_str:
                expiration_datetime = datetime.strptime(
                    param_str, '%Y-%m-%d %H:%M:%S')
            elif '/' in param_str:
                expiration_datetime = datetime.strptime(
                    param_str, '%Y/%m/%d %H:%M:%S')

            # Compare only the date part
            if expiration_datetime and expiration_datetime.date() == today:
                # Add 30 days to the expiration date
                new_expiration_datetime = expiration_datetime + \
                    timedelta(days=30)

                # Convert the new expiration datetime back to string format
                new_expiration_datetime_str = new_expiration_datetime.strftime(
                    "%Y-%m-%d %H:%M:%S")

                # Update the parameter with the new expiration date
                self.env['ir.config_parameter'].sudo().set_param(
                    'database.expiration_date', new_expiration_datetime_str)

                # Log the update for debugging and auditing purposes
                _logger.info("Updated expiration date: %s to %s" %
                             (param_str, new_expiration_datetime_str))
        else:
            _logger.info("database.expiration_date parameter not set.")
