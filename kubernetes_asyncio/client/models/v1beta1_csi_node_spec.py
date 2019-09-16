# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.14.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1beta1CSINodeSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'drivers': 'list[V1beta1CSINodeDriver]'
    }

    attribute_map = {
        'drivers': 'drivers'
    }

    def __init__(self, drivers=None):  # noqa: E501
        """V1beta1CSINodeSpec - a model defined in OpenAPI"""  # noqa: E501

        self._drivers = None
        self.discriminator = None

        self.drivers = drivers

    @property
    def drivers(self):
        """Gets the drivers of this V1beta1CSINodeSpec.  # noqa: E501

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :return: The drivers of this V1beta1CSINodeSpec.  # noqa: E501
        :rtype: list[V1beta1CSINodeDriver]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this V1beta1CSINodeSpec.

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :param drivers: The drivers of this V1beta1CSINodeSpec.  # noqa: E501
        :type: list[V1beta1CSINodeDriver]
        """
        if drivers is None:
            raise ValueError("Invalid value for `drivers`, must not be `None`")  # noqa: E501

        self._drivers = drivers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1CSINodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
