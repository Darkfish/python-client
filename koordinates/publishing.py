# -*- coding: utf-8 -*-

"""
koordinates.publishing
======================

The Group Publishing API allows for draft versions of versioned objects
Documents, Layers, and Tables) to be scheduled for publishing together.
"""
import logging

from . import base
from .utils import is_bound


logger = logging.getLogger(__name__)


class PublishManager(base.Manager):
    URL_KEY = 'PUBLISH'

    def create(self, publish):
        target_url = self.client.get_url('PUBLISH', 'POST', 'create')
        r = self.client.request('POST', target_url, json=publish.serialize())
        return self.create_from_result(r.json())

class Publish(base.Model):
    """
    The Group Publishing API allows for draft versions of versioned objects
    (Documents, Layers, and Tables) to be scheduled for publishing together.

    A Publish object describes an active publishing group.
    """
    class Meta:
        manager = PublishManager
        attribute_filter_candidates = ('state', 'reference',)

    PUBLISH_STRATEGY_TOGETHER = 'together'
    PUBLISH_STRATEGY_INDIVIDUAL = 'individual'

    ERROR_STRATEGY_ABORT = 'abort'
    ERROR_STRATEGY_IGNORE = 'ignore'

    def __init__(self, **kwargs):
        self.items = []
        super(Publish, self).__init__(**kwargs)

    @is_bound
    def cancel(self):
        """ Cancel a pending publish task """
        target_url = self._client.get_url('PUBLISH', 'DELETE', 'single', {'id': self.id})
        r = self._client.request('DELETE', target_url)
        logger.info("cancel(): %s", r.status_code)
        return True

    def get_items(self):
        """
        Return the item models associated with this Publish group.
        """
        from .layers import Layer

        # no expansion support, just URLs
        results = []
        for url in self.items:
            if '/layers/' in url:
                r = self._client.request('GET', url)
                results.append(self._client.get_manager(Layer).create_from_result(r.json()))
            else:
                raise NotImplementedError("No support for %s" % url)
        return results

    def add_layer_item(self, layer):
        if not hasattr(layer, 'draft_version'):
            raise ValueError("Layer has no draft_version")

        self.items.append(layer.draft_version)

    def add_table_item(self, table):
        if not hasattr(table, 'draft_version'):
            raise ValueError("Table has no draft_version")

        self.items.append(table.draft_version)