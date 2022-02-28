"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from igtcloud.client.services.entities.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from igtcloud.client.services.entities.model.marvel_series_all_of import MarvelSeriesAllOf
    from igtcloud.client.services.entities.model.marvel_study import MarvelStudy
    from igtcloud.client.services.entities.model.series import Series
    globals()['MarvelSeriesAllOf'] = MarvelSeriesAllOf
    globals()['MarvelStudy'] = MarvelStudy
    globals()['Series'] = Series


class MarvelSeries(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'series_type': (str,),  # noqa: E501
            'study': (MarvelStudy,),  # noqa: E501
            'series_database_id': (str,),  # noqa: E501
            'created_on': (str,),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'last_updated_on': (str,),  # noqa: E501
            'last_updated_by': (str,),  # noqa: E501
            'instance_uid': (str,),  # noqa: E501
            'modality': (str,),  # noqa: E501
            'preview_url': (str,),  # noqa: E501
            'procedure_database_id': (str,),  # noqa: E501
            's3_prefix': (str,),  # noqa: E501
            'series_format': (str,),  # noqa: E501
            'study_database_id': (str,),  # noqa: E501
            'related_study_instance_uid': (str,),  # noqa: E501
            'related_series_instance_uid': (str,),  # noqa: E501
            'document_title': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'series_type': val}

    attribute_map = {
        'series_type': 'seriesType',  # noqa: E501
        'study': 'study',  # noqa: E501
        'series_database_id': 'seriesDatabaseId',  # noqa: E501
        'created_on': 'createdOn',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'last_updated_on': 'lastUpdatedOn',  # noqa: E501
        'last_updated_by': 'lastUpdatedBy',  # noqa: E501
        'instance_uid': 'instanceUid',  # noqa: E501
        'modality': 'modality',  # noqa: E501
        'preview_url': 'previewUrl',  # noqa: E501
        'procedure_database_id': 'procedureDatabaseId',  # noqa: E501
        's3_prefix': 's3Prefix',  # noqa: E501
        'series_format': 'seriesFormat',  # noqa: E501
        'study_database_id': 'studyDatabaseId',  # noqa: E501
        'related_study_instance_uid': 'relatedStudyInstanceUid',  # noqa: E501
        'related_series_instance_uid': 'relatedSeriesInstanceUid',  # noqa: E501
        'document_title': 'documentTitle',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, series_type, *args, **kwargs):  # noqa: E501
        """MarvelSeries - a model defined in OpenAPI

        Args:
            series_type (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            study (MarvelStudy): [optional]  # noqa: E501
            series_database_id (str): [optional]  # noqa: E501
            created_on (str): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            last_updated_on (str): [optional]  # noqa: E501
            last_updated_by (str): [optional]  # noqa: E501
            instance_uid (str): [optional]  # noqa: E501
            modality (str): [optional]  # noqa: E501
            preview_url (str): [optional]  # noqa: E501
            procedure_database_id (str): [optional]  # noqa: E501
            s3_prefix (str): [optional]  # noqa: E501
            series_format (str): [optional]  # noqa: E501
            study_database_id (str): [optional]  # noqa: E501
            related_study_instance_uid (str): [optional]  # noqa: E501
            related_series_instance_uid (str): [optional]  # noqa: E501
            document_title (str): [optional]  # noqa: E501
            display_name (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'series_type': series_type,
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              MarvelSeriesAllOf,
              Series,
          ],
          'oneOf': [
          ],
        }
