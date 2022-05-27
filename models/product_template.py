
from odoo import api, fields, models

from odoo.addons.website.models import ir_http


class ProductTemplate(models.Model):
    _inherit = "product.template"

    website_attachment_ids = fields.Many2many(
        string="Website attachments",
        comodel_name="ir.attachment",
        context={"default_public": True, "hide_attachment_products": True},
        domain=lambda self, *args, **kwargs: (
            self._domain_website_attachment_ids(*args, **kwargs)
        ),
        help="Files publicly downloadable from the product eCommerce page. Only public attachments can be used or created here. Removing one attachment from this list does not delete or unpublish it from your database.",
    )

    origin = fields.Many2one('res.country', string='Country of Origin', ondelete='restrict')

    @api.model
    def _domain_website_attachment_ids(self):
        """Get domain for website attachments."""
        domain = [
            # Only use public attachments
            ("public", "=", True),
            # Exclude Odoo asset files to avoid confusing the user
            "!",
            ("name", "=ilike", "%.assets%.js"),
            "!",
            ("name", "=ilike", "%.assets%.css"),
            "!",
            ("name", "=ilike", "web_editor%"),
            "!",
            ("name", "=ilike", "/web/content/%.assets%.js"),
            "!",
            ("name", "=ilike", "/web/content/%.assets%.css"),
            "!",
            ("name", "=ilike", r"/web/content/%/web\_editor.summernote%.js"),
            "!",
            ("name", "=ilike", r"/web/content/%/web\_editor.summernote%.css"),
        ]
        # Filter by website domain in frontend
        if ir_http.get_request_website():
            website = self.env["website"].get_current_website()
            domain += website.website_domain()
        return domain