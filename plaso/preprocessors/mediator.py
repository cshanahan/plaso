# -*- coding: utf-8 -*-
"""The preprocess mediator."""

from plaso.containers import warnings


class PreprocessMediator(object):
  """Preprocess mediator."""

  def __init__(self, storage_writer, knowledge_base):
    """Initializes a preprocess mediator.

    Args:
      storage_writer (StorageWriter): storage writer, to store preprocessing
          information in.
      knowledge_base (KnowledgeBase): knowledge base, to fill with
          preprocessing information.
    """
    super(PreprocessMediator, self).__init__()
    self._knowledge_base = knowledge_base
    self._storage_writer = storage_writer

  @property
  def knowledge_base(self):
    """KnowledgeBase: knowledge base."""
    return self._knowledge_base

  def ProducePreprocessingWarning(self, plugin_name, path_spec, message):
    """Produces a preprocessing warning.

    Args:
      plugin_name (str): name of the preprocess plugin.
      path_spec (dfvfs.PathSpec): path specification.
      message (str): message of the warning.
    """
    if self._storage_writer:
      warning = warnings.PreprocessingWarning(
          message=message, path_spec=path_spec, plugin_name=plugin_name)
      self._storage_writer.AddPreprocessingWarning(warning)
