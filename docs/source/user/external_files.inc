.. _external_files:

External data files
+++++++++++++++++++
When using *PRISM*, there are three different cases where the path to an external data file can be provided.
As mentioned in :ref:`general_rules`, all external files are read-in as a Python dict, with the colon being the separator between the key and value.
Additionally, all lines are read as strings and converted back when assigned in memory, to allow for many different mark-ups to be used.
Depending on which of the three files is read-in, the keys and values have different meanings.
Here, the three different files are described.

PRISM parameters file
#####################
This file contains the non-default values that must be used for the :ref:`parameters`.
These parameters control various different functionalities of *PRISM*.
It is provided as the `prism_file` argument when initializing the :class:`~prism.Pipeline` class.
When certain parameters are read-in depends on their type:
    
    - Emulator parameters: Whenever a new emulator is created;
    - Pipeline parameters: When the :class:`~prism.Pipeline` class is initialized;
    - Implausibility parameters: When the :meth:`~prism.Pipeline.analyze` method is called (saved to HDF5) or when an emulator iteration is loaded that has not been analyzed yet (not saved to HDF5);
    - Projection parameters: When the :meth:`~prism.Pipeline.project` method is called.

The default *PRISM* parameters file can be found in the ``prism/data`` folder and is shown below:

.. literalinclude:: ../../../prism/data/prism.txt
    :language: none

In this file, the key is the name of the parameter that needs to be changed, and the value what it needs to be changed to.
*PRISM* itself does not require this default file, as all of the default values are hard-coded, and is therefore never read-in.
An externally provided *PRISM* parameters file is only required to have the non-default values.

Model parameters file
#####################
This file contains the non-default model parameters to use for a model.
It is provided as the `model_parameters` input argument when initializing the :class:`~prism.modellink.ModelLink` subclass (a dict or array-like can be provided instead as well).
Keep in mind that the :class:`~prism.modellink.ModelLink` subclass may not have default model parameters defined.

An example of the various different ways model parameter information can be provided is given below:

.. literalinclude:: data/model_parameters.txt
    :language: none

In this file, the key is the name of the model parameter and the value is a sequence of integers or floats, specifying the *lower* and *upper* boundaries of the parameter and, optionally, its estimate.
The contents of this file is equal to providing the following as `model_parameters` during initialization of a :class:`~prism.modellink.ModelLink` subclass::

    # As a dict
    model_parameters = {'A': [1, 5, 3],
                        'Bravo': [2, 7, None],
                        'C42': [3, 6.74]}

    # As an array_like
    model_parameters = [['A', [1, 5, 3]],
                        ['Bravo', [2, 7, None]],
                        ['C42', [3, 6.74]]]

    # As two array_likes zipped
    model_parameters = zip(['A', 'Bravo', 'C42'],
                           [[1, 5, 3], [2, 7, None], [3, 6.74]])

Providing :pycode:`None` as the parameter estimate or not providing it at all, implies that no parameter estimate (for the corresponding parameter) should be used in the projection figures.

Model data file
###############
This file contains the non-default model comparison data points to use for a model.
It is provided as the `model_data` input argument when initializing the :class:`~prism.modellink.ModelLink` subclass (a dict or array-like can be provided instead as well).
Keep in mind that the :class:`~prism.modellink.ModelLink` subclass may not have default model comparison data defined.

An example of the various different ways model comparison data information can be provided is given below:

.. literalinclude:: data/model_data.txt
    :language: none

Here, the key is the full sequence of the data identifier of a data point, where any character that is not a letter, number, minus/plus or period acts as a separator between the elements of the data identifier.
The corresponding value specifies the data value, data error(s) and data value space.
Braces, parentheses, brackets and many other characters can be used as mark-up in the data identifier, to make it easier for the user to find a suitable file lay-out.
A full list of all characters that can be used for this can be found in :attr:`prism._internal.aux_char_list`.

Similarly to the model parameters, the following is equal to the contents of this file::

    # As a dict
    model_data = {(1, 2): [1, 0.05, 0.05, 'lin'],
                  3.0: [2, 0.05, 'log'],
                  'A': [3, 0.05, 0.15],
                  (1, 'A', 1.0): [4, 0.05]}

    # As an array_like
    model_data = [[(1, 2), [1, 0.05, 0.05, 'lin']],
                  [3.0, [2, 0.05, 'log']],
                  ['A', [3, 0.05, 0.15]],
                  [(1, 'A', 1.0), [4, 0.05]]]

    # As two array_likes zipped
    model_data = zip([(1, 2), 3.0, 'A', (1, 'A', 1.0)],
                     [[1, 0.05, 0.05, 'lin'], [2, 0.05, 'log'], [3, 0.05, 0.15], [4, 0.05]])

It is necessary for the data value to be provided at all times.
The data error can be given as either a single value, where it assumed that the data point has a centered :math:`1\sigma`-confidence interval, or as two values, where they describe the *upper* and *lower* bounds of the :math:`1\sigma`-confidence interval.
The data value space can be given as a string or omitted, in which it is assumed that the value space is linear.

.. note::
    The parameter value bounds are given as [*lower bound*, *upper bound*], whereas the data errors are given as [*upper error*, *lower error*].
    The reason for this is that, individually, the order for either makes the most sense.
    Together however, it may cause some confusion, so extra care needs to be taken.
