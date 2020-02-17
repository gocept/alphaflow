# -*- coding: iso-8859-1 -*-
# Copyright (c) 2004-2006 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id: instance.py 4614 2007-03-26 20:12:22Z ctheune $
"""AlphaFlow configlet"""

import Products.Five

import Products.AlphaFlow.interfaces


class Statistics(Products.Five.BrowserView):

    def cycle_time(self, begin, end):
        """Adds new process to process manager."""
        statistics = Products.AlphaFlow.interfaces.IProcessStatistics(
            self.context)
        return round(statistics.cycle_time(begin, end) * 60)
