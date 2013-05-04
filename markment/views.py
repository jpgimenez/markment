# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class TemplateContext(object):
    def __init__(self, **data):
        self.data = data
        self.static_prefix = './'

    def static_file(self, name):
        return "{0}{1}".format(self.static_prefix, name.lstrip('/'))

    def link(self, path):
        return path

    def ready_to_render(self, static_prefix=None):
        if static_prefix:
            self.static_prefix = static_prefix

        ctx = {}
        ctx['static_file'] = self.static_file
        ctx['link'] = self.link
        ctx.update(self.data)
        return ctx