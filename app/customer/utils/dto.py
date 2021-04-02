from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'email': fields.String(required=True, description='customer email address'),
        'first_name': fields.String(required=True, description='customer first name'),
        'last_name': fields.String(required=True, description='customer last name'),
        'created': fields.DateTime(required=False, description='created date time'),
        'modified': fields.DateTime(required=False, description='modified date time'),
        'id': fields.String(description='customer Identifier')
    })
