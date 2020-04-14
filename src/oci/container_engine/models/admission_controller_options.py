# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdmissionControllerOptions(object):
    """
    The properties that define supported admission controllers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdmissionControllerOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_pod_security_policy_enabled:
            The value to assign to the is_pod_security_policy_enabled property of this AdmissionControllerOptions.
        :type is_pod_security_policy_enabled: bool

        """
        self.swagger_types = {
            'is_pod_security_policy_enabled': 'bool'
        }

        self.attribute_map = {
            'is_pod_security_policy_enabled': 'isPodSecurityPolicyEnabled'
        }

        self._is_pod_security_policy_enabled = None

    @property
    def is_pod_security_policy_enabled(self):
        """
        Gets the is_pod_security_policy_enabled of this AdmissionControllerOptions.
        Whether or not to enable the Pod Security Policy admission controller.


        :return: The is_pod_security_policy_enabled of this AdmissionControllerOptions.
        :rtype: bool
        """
        return self._is_pod_security_policy_enabled

    @is_pod_security_policy_enabled.setter
    def is_pod_security_policy_enabled(self, is_pod_security_policy_enabled):
        """
        Sets the is_pod_security_policy_enabled of this AdmissionControllerOptions.
        Whether or not to enable the Pod Security Policy admission controller.


        :param is_pod_security_policy_enabled: The is_pod_security_policy_enabled of this AdmissionControllerOptions.
        :type: bool
        """
        self._is_pod_security_policy_enabled = is_pod_security_policy_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other