from rest_framework.permissions import BasePermission

class IsBookingOwnerOrBusinessStaff(BasePermission):
    """
    Customer فقط بوکینگ خودش رو ببینه/کنسل کنه.
    Owner/Specialist فقط بوکینگ‌های Business خودشون رو ببینن/تغییر بدن.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the booking
        if request.user == obj.customer:
            return True

        # Check if the user is the owner of the business associated with the booking
        if hasattr(obj, 'availability') and hasattr(obj.availability, 'business'):
            return request.user == obj.availability.business.owner

        return False