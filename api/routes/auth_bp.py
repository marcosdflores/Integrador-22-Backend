from flask import Blueprint

from ..controllers.auth_controller import UserController

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(UserController.login)
auth_bp.route('/profile', methods=['GET'])(UserController.show_profile)
auth_bp.route('/logout', methods=['GET'])(UserController.logout)


users_bp = Blueprint('users', __name__)

users_bp.route('/usuarios/crear', methods=['GET', 'POST'])(UserController.crear_usuario)
users_bp.route('/usuarios/modificar/<int:id_usuario>', methods=['PUT'])(UserController.modificar_usuario)
users_bp.route('/usuarios/eliminar/<int:id_usuario>',methods=['DELETE'])(UserController.eliminar_usuario)
