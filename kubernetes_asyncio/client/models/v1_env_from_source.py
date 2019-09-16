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


class V1EnvFromSource(object):
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
        'config_map_ref': 'V1ConfigMapEnvSource',
        'prefix': 'str',
        'secret_ref': 'V1SecretEnvSource'
    }

    attribute_map = {
        'config_map_ref': 'configMapRef',
        'prefix': 'prefix',
        'secret_ref': 'secretRef'
    }

    def __init__(self, config_map_ref=None, prefix=None, secret_ref=None):  # noqa: E501
        """V1EnvFromSource - a model defined in OpenAPI"""  # noqa: E501

        self._config_map_ref = None
        self._prefix = None
        self._secret_ref = None
        self.discriminator = None

        if config_map_ref is not None:
            self.config_map_ref = config_map_ref
        if prefix is not None:
            self.prefix = prefix
        if secret_ref is not None:
            self.secret_ref = secret_ref

    @property
    def config_map_ref(self):
        """Gets the config_map_ref of this V1EnvFromSource.  # noqa: E501


        :return: The config_map_ref of this V1EnvFromSource.  # noqa: E501
        :rtype: V1ConfigMapEnvSource
        """
        return self._config_map_ref

    @config_map_ref.setter
    def config_map_ref(self, config_map_ref):
        """Sets the config_map_ref of this V1EnvFromSource.


        :param config_map_ref: The config_map_ref of this V1EnvFromSource.  # noqa: E501
        :type: V1ConfigMapEnvSource
        """

        self._config_map_ref = config_map_ref

    @property
    def prefix(self):
        """Gets the prefix of this V1EnvFromSource.  # noqa: E501

        An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.  # noqa: E501

        :return: The prefix of this V1EnvFromSource.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this V1EnvFromSource.

        An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.  # noqa: E501

        :param prefix: The prefix of this V1EnvFromSource.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1EnvFromSource.  # noqa: E501


        :return: The secret_ref of this V1EnvFromSource.  # noqa: E501
        :rtype: V1SecretEnvSource
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1EnvFromSource.


        :param secret_ref: The secret_ref of this V1EnvFromSource.  # noqa: E501
        :type: V1SecretEnvSource
        """

        self._secret_ref = secret_ref

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
        if not isinstance(other, V1EnvFromSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
