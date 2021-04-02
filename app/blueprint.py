from flask_restplus import Api
from flask import Blueprint

from customer.controller.customer_controller import api as customer_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='Customer API',
          version='1.0',
          description='Customer API Endpoints'
          )

api.add_namespace(customer_ns, path='/customer')
