from django.contrib import admin

from .models import Election

class ElectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    readonly_fields = (
        'election_id',
        'tmp_election_id',
        'election_type',
        'election_subtype',
        'poll_open_date',
        'organisation',
        'elected_role',
        'division',
        'seats_contested',
        'seats_total',
        'group',
    )

admin.site.register(Election, ElectionAdmin)
