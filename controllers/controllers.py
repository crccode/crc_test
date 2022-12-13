# -*- coding: utf-8 -*-
# from odoo import http


# class CrcTest(http.Controller):
#     @http.route('/crc_test/crc_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crc_test/crc_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crc_test.listing', {
#             'root': '/crc_test/crc_test',
#             'objects': http.request.env['crc_test.crc_test'].search([]),
#         })

#     @http.route('/crc_test/crc_test/objects/<model("crc_test.crc_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crc_test.object', {
#             'object': obj
#         })
