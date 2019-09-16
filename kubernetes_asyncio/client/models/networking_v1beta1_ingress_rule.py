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


class NetworkingV1beta1IngressRule(object):
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
        'host': 'str',
        'http': 'NetworkingV1beta1HTTPIngressRuleValue'
    }

    attribute_map = {
        'host': 'host',
        'http': 'http'
    }

    def __init__(self, host=None, http=None):  # noqa: E501
        """NetworkingV1beta1IngressRule - a model defined in OpenAPI"""  # noqa: E501

        self._host = None
        self._http = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if http is not None:
            self.http = http

    @property
    def host(self):
        """Gets the host of this NetworkingV1beta1IngressRule.  # noqa: E501

        Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \"host\" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the    IP in the Spec of the parent Ingress. 2. The `:` delimiter is not respected because ports are not allowed.    Currently the port of an Ingress is implicitly :80 for http and    :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  # noqa: E501

        :return: The host of this NetworkingV1beta1IngressRule.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this NetworkingV1beta1IngressRule.

        Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \"host\" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the    IP in the Spec of the parent Ingress. 2. The `:` delimiter is not respected because ports are not allowed.    Currently the port of an Ingress is implicitly :80 for http and    :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  # noqa: E501

        :param host: The host of this NetworkingV1beta1IngressRule.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def http(self):
        """Gets the http of this NetworkingV1beta1IngressRule.  # noqa: E501


        :return: The http of this NetworkingV1beta1IngressRule.  # noqa: E501
        :rtype: NetworkingV1beta1HTTPIngressRuleValue
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this NetworkingV1beta1IngressRule.


        :param http: The http of this NetworkingV1beta1IngressRule.  # noqa: E501
        :type: NetworkingV1beta1HTTPIngressRuleValue
        """

        self._http = http

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
        if not isinstance(other, NetworkingV1beta1IngressRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
