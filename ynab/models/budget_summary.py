# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ynab.configuration import Configuration


class BudgetSummary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'last_modified_on': 'datetime',
        'first_month': 'date',
        'last_month': 'date',
        'date_format': 'DateFormat',
        'currency_format': 'CurrencyFormat',
        'accounts': 'list[Account]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'last_modified_on': 'last_modified_on',
        'first_month': 'first_month',
        'last_month': 'last_month',
        'date_format': 'date_format',
        'currency_format': 'currency_format',
        'accounts': 'accounts'
    }

    def __init__(self, id=None, name=None, last_modified_on=None, first_month=None, last_month=None, date_format=None, currency_format=None, accounts=None, _configuration=None):  # noqa: E501
        """BudgetSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._last_modified_on = None
        self._first_month = None
        self._last_month = None
        self._date_format = None
        self._currency_format = None
        self._accounts = None
        self.discriminator = None

        self.id = id
        self.name = name
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if first_month is not None:
            self.first_month = first_month
        if last_month is not None:
            self.last_month = last_month
        if date_format is not None:
            self.date_format = date_format
        if currency_format is not None:
            self.currency_format = currency_format
        if accounts is not None:
            self.accounts = accounts

    @property
    def id(self):
        """Gets the id of this BudgetSummary.  # noqa: E501


        :return: The id of this BudgetSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BudgetSummary.


        :param id: The id of this BudgetSummary.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BudgetSummary.  # noqa: E501


        :return: The name of this BudgetSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BudgetSummary.


        :param name: The name of this BudgetSummary.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this BudgetSummary.  # noqa: E501

        The last time any changes were made to the budget from either a web or mobile client  # noqa: E501

        :return: The last_modified_on of this BudgetSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this BudgetSummary.

        The last time any changes were made to the budget from either a web or mobile client  # noqa: E501

        :param last_modified_on: The last_modified_on of this BudgetSummary.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def first_month(self):
        """Gets the first_month of this BudgetSummary.  # noqa: E501

        The earliest budget month  # noqa: E501

        :return: The first_month of this BudgetSummary.  # noqa: E501
        :rtype: date
        """
        return self._first_month

    @first_month.setter
    def first_month(self, first_month):
        """Sets the first_month of this BudgetSummary.

        The earliest budget month  # noqa: E501

        :param first_month: The first_month of this BudgetSummary.  # noqa: E501
        :type: date
        """

        self._first_month = first_month

    @property
    def last_month(self):
        """Gets the last_month of this BudgetSummary.  # noqa: E501

        The latest budget month  # noqa: E501

        :return: The last_month of this BudgetSummary.  # noqa: E501
        :rtype: date
        """
        return self._last_month

    @last_month.setter
    def last_month(self, last_month):
        """Sets the last_month of this BudgetSummary.

        The latest budget month  # noqa: E501

        :param last_month: The last_month of this BudgetSummary.  # noqa: E501
        :type: date
        """

        self._last_month = last_month

    @property
    def date_format(self):
        """Gets the date_format of this BudgetSummary.  # noqa: E501


        :return: The date_format of this BudgetSummary.  # noqa: E501
        :rtype: DateFormat
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this BudgetSummary.


        :param date_format: The date_format of this BudgetSummary.  # noqa: E501
        :type: DateFormat
        """

        self._date_format = date_format

    @property
    def currency_format(self):
        """Gets the currency_format of this BudgetSummary.  # noqa: E501


        :return: The currency_format of this BudgetSummary.  # noqa: E501
        :rtype: CurrencyFormat
        """
        return self._currency_format

    @currency_format.setter
    def currency_format(self, currency_format):
        """Sets the currency_format of this BudgetSummary.


        :param currency_format: The currency_format of this BudgetSummary.  # noqa: E501
        :type: CurrencyFormat
        """

        self._currency_format = currency_format

    @property
    def accounts(self):
        """Gets the accounts of this BudgetSummary.  # noqa: E501

        The budget accounts (only included if `include_accounts=true` specified as query parameter)  # noqa: E501

        :return: The accounts of this BudgetSummary.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this BudgetSummary.

        The budget accounts (only included if `include_accounts=true` specified as query parameter)  # noqa: E501

        :param accounts: The accounts of this BudgetSummary.  # noqa: E501
        :type: list[Account]
        """

        self._accounts = accounts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BudgetSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BudgetSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BudgetSummary):
            return True

        return self.to_dict() != other.to_dict()
