# -*- coding: utf-8 -*-

"""
PRISM Docstrings
================
Contains a collection of docstrings that are reused throughout the
documentation of the various functions in the *PRISM* package.

"""


# Write the string for indicating default values
ds = ". Default: "


# %% EMUL_I DOCSTRINGS
# Base description of emul_i parameter
base_emul_i_doc = "Number indicating the requested emulator iteration."

# Description of emul_i used in __call__/construct
call_emul_i_doc =\
        """emul_i : int or None. Default: None
            If int, {0}
            If *None*, the next iteration of the emulator will be
            constructed.""".format(base_emul_i_doc.lower())

# Description of emul_i used in the get_emul_i() method of the Emulator class
get_emul_i_doc =\
        """emul_i : int or None
            {0}""".format(base_emul_i_doc)

# Description of emul_i used in basically all standard hidden functions
std_emul_i_doc =\
        """emul_i : int
            {0}""".format(base_emul_i_doc)

# Description of emul_i used in all user functions except __call__/construct
user_emul_i_doc =\
        """emul_i : int or None. Default: None
            If int, {0}
            If *None*, the last iteration of the emulator will be
            used.""".format(base_emul_i_doc.lower())


# %% EMUL_S DOCSTRINGS
# Description of sequence of emul_s used in all standard hidden functions
emul_s_seq_doc =\
        """emul_s_seq : list of int
            List of numbers indicating the requested emulator systems."""

# Description of emul_s used in basically all standard hidden functions
lemul_s_doc =\
        """lemul_s : int or None
            Number indicating the requested local emulator system.
            If *None*, use the master emulator file instead."""


# %% PIPELINE DOCSTRINGS
# Docstrings for the call_model methods
call_model_doc =\
        """Obtain the output{3} corresponding to the provided `data_idx` that
        is generated by the model for a given model parameter sample{3} `{0}`.
        The current emulator iteration `emul_i` is also provided in case it is
        required by the :class:`~prism.modellink.ModelLink` subclass.
        {4}
        Parameters
        ----------
        %s
        {0} : {2} array_like
            Model parameter sample{3} to calculate the model output for.
        data_idx : list of tuples
            The list of data identifiers for which the model is requested to
            return the corresponding data values.

        Returns
        -------
        {1} : {2} :obj:`~numpy.ndarray` object
            Model output{3} corresponding to given `{0}`.""" % (std_emul_i_doc)
call_model_doc_s = call_model_doc.format("par_set", "mod_out", "1D", "", "")
call_model_doc_m = call_model_doc.format(
    "sam_set", "mod_set", "2D", " set",
    "\n\tThis is a multi-version of :meth:`~prism.Pipeline._call_model`.\n")

# Descriptions for the ext_real_set parameters
ext_mod_set_doc =\
        """ext_mod_set : 1D or 2D :obj:`~numpy.ndarray` object
            Array containing the model outputs of all specified externally
            provided model evaluation samples."""
ext_real_set_doc =\
        """ext_real_set : list, dict or None{0}{1}
            List of dicts containing an externally calculated set of model
            evaluation samples and its data values, a dict with keys
            ``['sam_set', 'mod_set']`` containing these dicts or *None* if no
            external set needs to be used."""
ext_real_set_doc_s = ext_real_set_doc.format("", "")
ext_real_set_doc_d = ext_real_set_doc.format(ds, "None")
ext_sam_set_doc =\
        """ext_sam_set : 1D or 2D :obj:`~numpy.ndarray` object
            Array containing the externally provided model evaluation
            samples."""

# Docstrings for the _make_call methods
make_call_doc =\
        """Sends the provided `exec_fn` to all worker ranks, if they are
        listening for calls, and tells them to execute it using the provided
        `args` and `kwargs`.{0}

        If used within the :class:`~prism._pipeline.WorkerMode` context
        manager, this function should only be called by the controller. If not,
        it should be called by all valid ranks that must execute `exec_fn`.

        Parameters
        ----------{1}
        exec_fn : str or callable
            If string, a callable attribute of this :obj:`~prism.Pipeline`
            instance or a callable object that the workers should execute if
            not.
        args : positional arguments
            Positional arguments that need to be provided to `exec_fn`.
        kwargs : keyword arguments
            Keyword arguments that need to be provided to `exec_fn`.

        Returns
        -------
        out : object
            The object returned by executing `exec_fn`. Note that only ranks
            that directly call this function return, as workers in worker mode
            cannot do so.

        Note
        ----
        .. versionchanged:: 1.2.0
            If any entry in `args` or `kwargs` is a string written as
            'pipe.XXX', it is assumed that 'XXX' refers to a
            :class:`~prism.Pipeline` attribute of the MPI rank receiving the
            call. It will be replaced with the corresponding attribute before
            `exec_fn` is called.

        """
make_call_pipeline_doc =\
        """pipeline_obj : :obj:`~prism.Pipeline` object
            The instance of the :class:`~prism.Pipeline` class that is making
            this call."""

make_call_doc_a = make_call_doc.format(
    " All ranks that call this function will execute `exec_fn` as well.", "")
make_call_doc_w = make_call_doc.format("", "")
make_call_doc_aw = make_call_doc.format(
    " All ranks that call this function will execute `exec_fn` as well.",
    "\n\t"+make_call_pipeline_doc)
make_call_doc_ww = make_call_doc.format("", "\n\t"+make_call_pipeline_doc)

# Docstrings for the different paths parameters
paths_doc =\
        """root_dir : str or None{0}{1}
            String containing the absolute path of the root directory where all
            working directories are stored. If *None*, root directory will be
            set to the directory this class was initialized in.
        working_dir : str, bool or None{0}{2}
            String containing the name of the working directory of the emulator
            in `root_dir`. If *True*, a new working directory will be created
            in `root_dir`. If *None* or *False*, working directory is set to
            the last one that was created in `root_dir` that starts with the
            given `prefix`. Note that providing an integer instead of a bool
            will not work here.
            If no directories are found, one will be created.
        prefix : str or None{0}{3}
            String containing a prefix that is used for naming new working
            directories or scan for existing ones. If *None*, all directories
            in `root_dir` are considered working directories and 'prism\\_'
            will be used as a prefix for new ones."""
paths_doc_s = paths_doc.format("", "", "", "")
paths_doc_d = paths_doc.format(ds, "None", "None", "None")


# %% EMULATOR DOCSTRINGS
# Description of adjusted expectation and variance values
adj_val_doc =\
        """adj_{0}_val : 1D :obj:`~numpy.ndarray` object
            Adjusted emulator {1} value for all requested emulator systems on
            this MPI rank."""
adj_exp_val_doc = adj_val_doc.format("exp", "expectation")
adj_var_val_doc = adj_val_doc.format("var", "variance")

# Docstrings for the _get_adj_exp and _get_adj_var methods
adj_doc =\
        """Calculates the adjusted emulator {0} values for requested emulator
        systems `emul_s_seq` at a given emulator iteration `emul_i` for
        specified parameter set `par_set` and corresponding covariance vector
        `cov_vec`.

        Parameters
        ----------
        {1}
        {2}
        par_set : 1D :obj:`~numpy.ndarray` object
            Model parameter value set to calculate the adjusted emulator {0}
            for.
        cov_vec : 2D :obj:`~numpy.ndarray` object
            Covariance vector corresponding to `par_set`.

        Returns
        -------
        {3}"""
adj_exp_doc = adj_doc.format("expectation", std_emul_i_doc, emul_s_seq_doc,
                             adj_exp_val_doc)
adj_var_doc = adj_doc.format("variance", std_emul_i_doc, emul_s_seq_doc,
                             adj_var_val_doc)

# Description for the parameters that the (regr_)cov() method takes
cov_doc =\
        """Parameters
        ----------
        %s
        %s
        par_set1, par_set2 : 1D :obj:`~numpy.ndarray` object or None
            If `par_set1` and `par_set2` are both not *None*, calculate
            {0}covariances for `par_set1` with `par_set2`.
            If `par_set1` is not *None* and `par_set2` is *None*, calculate
            {0}covariances for `par_set1` with
            :attr:`~Emulator.sam_set` (covariance vector).
            If `par_set1` and `par_set2` are both *None*, calculate
            {0}covariances for :attr:`~Emulator.sam_set` (covariance matrix).
            When not *None*, `par_set` is the model parameter value set to
            calculate the {0}covariances for.

        Returns
        -------
        {1}cov : 1D, 2D or 3D :obj:`~numpy.ndarray` object
            Depending on the arguments provided, a {0}covariance value, vector
            or matrix for requested emulator systems.""" % (std_emul_i_doc,
                                                            emul_s_seq_doc)
full_cov_doc = cov_doc.format("", "")
regr_cov_doc = cov_doc.format("regression ", "regr_")

# Docstring for _evaluate method
eval_doc =\
        """Evaluates the emulator systems `emul_s_seq` at iteration `emul_i`
        for given `par_set`.

        Parameters
        ----------
        {0}
        {1}
        par_set : 1D :obj:`~numpy.ndarray` object
            Model parameter value set to evaluate the emulator at.

        Returns
        -------
        {2}
        {3}""".format(std_emul_i_doc, emul_s_seq_doc, adj_exp_val_doc,
                      adj_var_val_doc)


# %% PROJECTION DOCSTRINGS
# Docstrings of draw_proj_fig methods
draw_proj_fig_doc =\
        """Draws the {0} projection figure for the provided `hcube`, given the
        `impl_min` and `impl_los` values.

        Parameters
        ----------
        hcube : 1D array_like of int of length {1}
            Array containing the internal integer identifiers of the main model
            parameters that require a projection figure.
        impl_min : 1D :obj:`~numpy.ndarray` object
            List containing the lowest implausibility value that can be reached
            in every single grid point on the given hypercube.
        impl_los : 1D :obj:`~numpy.ndarray` object
            List containing the fraction of the total amount of evaluated
            samples in every single grid point on the given hypercube, that
            still satisfied the implausibility cut-off criterion.
        proj_res : int
            Number of emulator evaluations used to generate the grid for the
            given hypercube."""

# Description of hcube
hcube_doc =\
        """hcube : 1D array_like of int of length {2, 3}
            Array containing the internal integer identifiers of the main model
            parameters that require a projection hypercube."""

# Descriptions of proj_data
proj_data_doc =\
        """impl_min_hcube : 1D :obj:`~numpy.ndarray` object
            List containing the lowest implausibility value that can be reached
            in every single grid point on the given hypercube.
        impl_los_hcube : 1D :obj:`~numpy.ndarray` object
            List containing the fraction of the total amount of evaluated
            samples in every single grid point on the given hypercube, that
            still satisfied the implausibility cut-off criterion."""

# Description of proj_par
proj_par_doc =\
        """proj_par : 1D array_like of {{int; str}} or None{0}{1}
            For which model parameters to construct the projection figures.
            If 1D array_like, construct projection figures for all combinations
            of provided model parameters that are active, with a string
            referring to the name of the model parameter and an integer
            referring to the position in which the model parameter is shown in
            the :meth:`~prism.Pipeline.details` method.
            If *None*, projection figures are made for all active model
            parameters."""
proj_par_doc_s = proj_par_doc.format("", "")
proj_par_doc_d = proj_par_doc.format(ds, "None")

# Descriptions of proj_depth and proj_res
proj_depth_doc = ("Number of emulator evaluations that will be used to "
                  "generate the samples in every grid point for the projection"
                  " figures.")
proj_res_doc = ("Number of emulator evaluations that will be used to generate "
                "the grid for the projection figures.")


# %% PROJECTION GUI DOCSTRINGS
# Docstring for the create_type_xxx methods in KwargsDictDialogPage
create_type_doc = "Creates the '{}' entry and returns it."

# Docstrings for the OverviewDockWidget class
list_items_optional_doc =\
        """Optional
        --------
        list_items : list of :obj:`~PyQt5.QtWidgets.QListWidgetItem` objects \
            or None. Default: None
            The list of items that contains the requested projection figures.
            If *None*, all currently selected list items are used instead."""
list_item_optional_doc =\
        """Optional
        --------
        list_item : :obj:`~PyQt5.QtWidgets.QListWidgetItem` object or None. \
            Default: None
            The item that contains the requested projection figure.
            If *None*, the currently selected list item is used instead."""

# Docstring for mentioning that a function acts as a Qt slot
qt_slot_doc = "This function acts as a Qt slot."

# Docstrings for the start_gui() function/method
GUI_APP_NAME = 'Crystal'
start_gui_doc =\
        """Creates an instance of :class:`~PyQt5.QtWidgets.QApplication` or
        retrieves it if one already exists, and starts *{0}*, *PRISM*'s
        Projection GUI.

        *{0}* provides an interactive way of creating projection figures, as
        opposed to the static and linear method provided by
        :meth:`~prism.Pipeline.project`.
        It is made to make it easier to create; view; compare; and analyze
        large numbers of projection figures.
        All options available in the :meth:`~prism.Pipeline.project` method
        can also be accessed through *{0}*.

        As with all :class:`~prism.Pipeline` user methods, this function must
        be called by all MPI ranks.

        .. versionadded:: 1.2.0""".format(GUI_APP_NAME)

start_gui_doc_pars =\
        """Parameters
        ----------
        pipeline_obj : :obj:`~prism.Pipeline` object
            The instance of the :class:`~prism.Pipeline` class for which *{0}*
            must be initialized.

        Returns
        -------
        main_window_obj : :obj:`~prism._gui.widgets.MainViewerWindow` object
            The instance of the :class:`~prism._gui.widgets.MainViewerWindow`
            class that was created for drawing *{0}*.
            Can be used for debugging purposes.

        Note
        ----
        This function can also be accessed through the
        :meth:`~prism.Pipeline.{1}` method.""".format(
            GUI_APP_NAME, GUI_APP_NAME.lower())


# %% GENERAL DOCSTRINGS
# Docstrings for the various get_default_parameters methods
def_par_doc =\
        """Generates a dict containing default values for all {0}
        parameters.

        Returns
        -------
        par_dict : dict
            Dict containing all default {0} parameter values."""

# Descriptions for various implausibility parameters
impl_cut_doc =\
        """impl_cut : 1D :obj:`~numpy.ndarray` object
            Full list containing the impl_cut-offs for all data points provided
            to the emulator.
        cut_idx : int
            Index of the first impl_cut-off in the impl_cut list that is not
            0."""

# Descriptions for the args/kwargs arguments of many classes
kwargs_doc =\
        """Optional
        --------
        args : positional arguments
            The positional arguments that must be passed to the constructor of
            the :class:`~{0}` class.
        kwargs : keyword arguments
            The keyword arguments that must be passed to the constructor of the
            :class:`~{0}` class."""

# Docstrings for the various set_parameters methods
set_par_doc =\
        """Sets the {0} parameters from the :attr:`~prism.Pipeline.prism_dict`
        property and saves them in the current :obj:`~{0}` instance."""

# Description of the various save_data methods
save_data_doc =\
        """Parameters
        ----------
        {0}
        data_dict : dict
            Dict containing the data that needs to be saved to the HDF5-file.

        Dict variables
        --------------
        keyword : {1}
            String specifying the type of data that needs to be saved.
        data : {{int; float; str; array_like}} or dict
            The actual data that needs to be saved at data keyword `keyword`.
            If dict, save every item individually.

        Generates
        ---------
        The specified data is saved to the HDF5-file."""
save_data_doc_p = save_data_doc.format(
    "", "{'impl_par'; 'impl_sam'; 'n_eval_sam'}")
save_data_doc_e = save_data_doc.format(
    std_emul_i_doc+"\n\t"+lemul_s_doc+"\n\t", "{'active_par'; "
    "'active_par_data'; 'cov_mat'; 'exp_dot_term'; 'mod_real_set'; "
    "'regression'}")
save_data_doc_pr = save_data_doc.format(std_emul_i_doc+"\n\t",
                                        "{'nD_proj_hcube'}")
