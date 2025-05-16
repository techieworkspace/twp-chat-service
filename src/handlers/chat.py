"""
Chat request handler module.
"""

# Import the base handler class from custom modules.
from handlers.base import BaseHandler


class RootHandler(BaseHandler):
    """
    Handles requests to the root URL ("/") of the account service.

    The RootHandler is responsible for redirecting any requests to the root URL ("/")
    of the account service to the dashboard page ("/dashboard"). This ensures that employees
    accessing the account service are immediately redirected to their dashboard, which is
    typically the main interface for account-related actions.

    Methods:
        get: Processes GET requests to the root URL and redirects to the dashboard page.
    """

    def get(self):
        """
        Processes GET requests to the root URL ("/") of the account service.

        This method automatically redirects employees to the dashboard page ("/dashboard").
        It does not return any content directly but issues an HTTP 302 redirect.

        Returns:
            None: This method does not return a value.
        """
        self.vars['title'] = f"Chat - {self.config['app']['name']}"
        self.render('chat.html', **self.vars)
