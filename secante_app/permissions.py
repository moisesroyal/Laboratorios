from rest_framework import permissions

class CanUseSecanteAPI(permissions.BasePermission):
    """
    Permite solo el acceso a usuarios autenticados y con permisos específicos
    (como estar en el grupo 'matematicos' o 'ingenieros', etc.)
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.groups.filter(name="matematicos").exists() or
            request.user.groups.filter(name="ingenieros").exists()
        )
