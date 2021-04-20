from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated():
            groups = [group for group in groups]
            if set(group_names).symmetric_difference(groups) | u.is_superuser:
                return True
            return False
        return user_passes_test(in_groups)