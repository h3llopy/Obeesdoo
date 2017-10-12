# -*- coding: utf8 -*-
from datetime import datetime
from itertools import groupby
from openerp import http
from openerp.http import request

from openerp.addons.beesdoo_shift.models.planning import float_to_time

class ShiftPortalController(http.Controller):

    @http.route('/shift_irregular_worker', auth='public', website=True)
    def shift_irregular_worker(self, **kwargs):
        # Get all the shifts in the future with no worker
        now = datetime.now()
        shifts = request.env['beesdoo.shift.shift'].sudo().search(
            [('start_time', '>', now.strftime("%Y-%m-%d %H:%M:%S")),
            ('worker_id', '=', False)],
            order="start_time, task_template_id, task_type_id",
        )

        shifts_and_count = []
        for _, val in groupby(shifts, lambda s: s.task_template_id):
            s = [v for v in val]
            shifts_and_count.append([len(s), s[0]])

        return request.render('beesdoo_portal_shift.shift_template',
            {'shift_templates': shifts_and_count}
        )

    @http.route('/shift_template_regular_worker', auth='public', website=True)
    def shift_template_regular_worker(self, **kwargs):
        # Get all the task template
        template = request.env['beesdoo.shift.template']
        task_templates = template.sudo().search([], order="planning_id, day_nb_id, start_time")

        return request.render('beesdoo_portal_shift.task_template',
            {
             'task_templates': task_templates,
             'float_to_time': float_to_time
            }
        )