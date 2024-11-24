# admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import ContactForm
from .models import MembershipPlan
from .forms import MembershipPlanForm

class CustomAdminSite(admin.AdminSite):
    site_header = _("FitnVibe | Admin Dashboard")
    site_title = _("FitnVibe | Admin Portal")
    index_title = _("Welcome to the Admin Dashboard")

    def index(self, request, extra_context=None):
        # Custom context data
        total_users = User.objects.count()
        total_plans = MembershipPlan.objects.count()
        active_memberships = MembershipPlan.objects.filter(is_active=True).count()

        extra_context = extra_context or {}
        extra_context.update({
            'total_users': total_users,
            'total_plans': total_plans,
            'active_memberships': active_memberships,
        })

        return super().index(request, extra_context)

# Register your models and the custom AdminSite
admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(ContactForm)
admin_site.register(MembershipPlan)