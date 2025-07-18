app_name = "terrasuitehelpdesk"
app_title = "Terrasuite Helpdesk"
app_publisher = "Calterras Technologies"
app_description = "Customer Service Software"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "saifulloh.fadli@calterras.com"
app_license = "AGPLv3"

add_to_apps_screen = [
    {
        "name": "terrasuitehelpdesk",
        "logo": "/assets/terrasuitehelpdesk/desk/favicon.svg",
        "title": "Terrasuite Helpdesk",
        "route": "/terrasuitehelpdesk",
        "has_permission": "terrasuitehelpdesk.api.permission.has_app_permission",
    }
]

after_install = "terrasuitehelpdesk.setup.install.after_install"
after_migrate = [
    "terrasuitehelpdesk.search.build_index_in_background",
    "terrasuitehelpdesk.search.download_corpus",
]

scheduler_events = {
    "all": [
        "terrasuitehelpdesk.search.build_index_if_not_exists",
        "terrasuitehelpdesk.search.download_corpus",
    ],
    "daily": [
        "terrasuitehelpdesk.terrasuitehelpdesk.doctype.hd_ticket.hd_ticket.close_tickets_after_n_days"
    ],
}


website_route_rules = [
    {
        "from_route": "/terrasuitehelpdesk/<path:app_path>",
        "to_route": "terrasuitehelpdesk",
    },
]

doc_events = {
    "Contact": {
        "before_insert": "terrasuitehelpdesk.terrasuitehelpdesk.hooks.contact.before_insert",
    },
    "Assignment Rule": {
        "on_trash": "terrasuitehelpdesk.extends.assignment_rule.on_assignment_rule_trash",
    },
}

has_permission = {
    "HD Ticket": "terrasuitehelpdesk.terrasuitehelpdesk.doctype.hd_ticket.hd_ticket.has_permission",
}

permission_query_conditions = {
    "HD Ticket": "terrasuitehelpdesk.terrasuitehelpdesk.doctype.hd_ticket.hd_ticket.permission_query",
}

# DocType Class
# ---------------
# Override standard doctype classes
override_doctype_class = {
    "Contact": "terrasuitehelpdesk.overrides.contact.CustomContact",
}

ignore_links_on_delete = [
    "HD Notification",
    "HD Ticket Comment",
]

# setup wizard
# setup_wizard_requires = "assets/helpdesk/js/setup_wizard.js"
# setup_wizard_stages = "terrasuitehelpdesk.setup.setup_wizard.get_setup_stages"
setup_wizard_complete = "terrasuitehelpdesk.setup.setup_wizard.setup_complete"


website_route_rules = [
    {"from_route": "/terrasuitehelpdesk/<path:app_path>", "to_route": "terrasuitehelpdesk"},
]
