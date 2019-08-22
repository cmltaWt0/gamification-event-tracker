"""
Exception types for Gamification operations.
"""
import logging
import json
import os
import time

from django.conf import settings


logger = logging.getLogger(__name__)


class GammaException(Exception):
    """
    Base exception class for Gamma application.
    """

    def __init__(self, message=None, *args):
        if message is None:
            self.message = 'An GammaException occurred without a specific message'
        super(GammaException, self).__init__(message, *args)


class GammaConnectionError(GammaException):
    """
    Base exception class for errors connecting to external services in Gamma application.
    """

    def __init__(self, message=None, *args):
        self.message = "External connection error in rg-gamification-traking application. {}".format(message)
        super(GammaConnectionError, self).__init__(self.message, *args)


class GammaLRSConnectionError(GammaConnectionError):
    """
    Exception class for problems connecting to an LRS.
    """

    def __init__(self, response=None, message=None, queue=None, *args):
        self.queue = queue
        if not message:
            self.message="Error connecting to remote storage at {}.".format(
                settings.RG_GAMIFICATION.get('RG_GAMIFICATION_ENDPOINT') if hasattr(settings, 'RG_GAMIFICATION') else None)
            if response:
                self.message+=" Requested resource was '{}'".format(response.request.resource)
        super(GammaLRSConnectionError, self).__init__(self.message, *args)


class GammaUserNotFoundError(GammaException):
    """
    Exception class for no LMS use found.
    """


class GammaStatementConversionError(GammaException):
    """
    Catch-all exception for bad Staements.
    """

    def __init__(self, event=None, message=None, *args):
        self.event = event
        self.message = message
        super(GammaStatementConversionError, self).__init__(self.message, *args)


class GammaStatementStorageError(GammaException):
    """
    Exception for Statements that are rejected by Storage
    """

    def __init__(self, statement=None, message=None, *args):
        self.statement = statement
        self.message = message
        super(GammaStatementStorageError, self).__init__(self.message, *args)


class GammaBackendResponseParseError(GammaException):
    """
    Exception for parsing information from backend error response.
    """

    def __init__(self, response_data='', *args):
        self.message = "Problem parsing problem from backend response: {}".format(response_data)
        super(GammaBackendResponseParseError, self).__init__(self.message, *args)


class GammaSkippedConversion(GammaException):
    """
    Raised if statement conversion is skipped due to some internal logic of Statement class.
    """
