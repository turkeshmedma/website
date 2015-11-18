# -*- coding: utf-8 -*-

from openerp import http
from openerp.http import request

class website_homepage(http.Controller):

    @http.route(['/page/image_zoom_first'], type='http', auth="public", website=True)
    def image_zoom_first(self, **post):
        return request.website.render("website_homepage.image_zoom_first")

    @http.route(['/page/image_zoom_second'], type='http', auth="public", website=True)
    def image_zoom_second(self, **post):
        return request.website.render("website_homepage.image_zoom_second")

    @http.route(['/page/image_zoom_third'], type='http', auth="public", website=True)
    def image_zoom_third(self, **post):
        return request.website.render("website_homepage.image_zoom_third")

    @http.route(['/page/image_zoom_four'], type='http', auth="public", website=True)
    def image_zoom_four(self, **post):
        return request.website.render("website_homepage.image_zoom_four")

    @http.route(['/page/image_slider'], type='http', auth="public", website=True)
    def image_slider(self, **post):
        return request.website.render("website_homepage.image_slider")
