// Copyright (c) 2017, DOKOS and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide('erpnext');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "Maia";

	frappe.help_feedback_link = '<p><a class="text-muted" \
		href="https://dokos.io">Feedback</a></p>'

	$('.navbar-home').html('<img class="erpnext-icon" src="'+
			frappe.urllib.get_base_url()+'/assets/maia/images/maia_squirrel.svg" />');
});
