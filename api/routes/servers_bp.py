from flask import Blueprint

from ..controllers.server_controller import ServerController

servers_bp = Blueprint('servers_bp', __name__)

servers_bp.route('/server', methods = ['POST'])(ServerController.crear_sv)
servers_bp.route('/server', methods = ['GET'])(ServerController.obtener_servers)
