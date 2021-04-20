# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class CompareResponse(object):
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
        'code': 'FaceRecognitionResultCode',
        'results': 'list[CompareImageResult]',
        'detections': 'list[CompareImageDetection]'
    }

    attribute_map = {
        'code': 'code',
        'results': 'results',
        'detections': 'detections'
    }

    def __init__(self, code=None, results=None, detections=None, local_vars_configuration=None):  # noqa: E501
        """CompareResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._results = None
        self._detections = None
        self.discriminator = None

        self.code = code
        if results is not None:
            self.results = results
        if detections is not None:
            self.detections = detections

    @property
    def code(self):
        """Gets the code of this CompareResponse.  # noqa: E501


        :return: The code of this CompareResponse.  # noqa: E501
        :rtype: FaceRecognitionResultCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CompareResponse.


        :param code: The code of this CompareResponse.  # noqa: E501
        :type code: FaceRecognitionResultCode
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def results(self):
        """Gets the results of this CompareResponse.  # noqa: E501


        :return: The results of this CompareResponse.  # noqa: E501
        :rtype: list[CompareImageResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CompareResponse.


        :param results: The results of this CompareResponse.  # noqa: E501
        :type results: list[CompareImageResult]
        """

        self._results = results

    @property
    def detections(self):
        """Gets the detections of this CompareResponse.  # noqa: E501


        :return: The detections of this CompareResponse.  # noqa: E501
        :rtype: list[CompareImageDetection]
        """
        return self._detections

    @detections.setter
    def detections(self, detections):
        """Sets the detections of this CompareResponse.


        :param detections: The detections of this CompareResponse.  # noqa: E501
        :type detections: list[CompareImageDetection]
        """

        self._detections = detections

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
        if not isinstance(other, CompareResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompareResponse):
            return True

        return self.to_dict() != other.to_dict()
